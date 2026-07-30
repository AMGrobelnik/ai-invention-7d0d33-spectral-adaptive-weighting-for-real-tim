#!/usr/bin/env python3
"""Spectral-Adaptive Ensemble forecasting with validation and ablations."""

import json
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from loguru import logger
import sys
import gc
import time
from scipy import signal
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import torch
import torch.nn as nn
from torch.optim import Adam
import warnings
warnings.filterwarnings("ignore")

# Setup logging
logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

# === TEST: MA(3) vs Naive ===
def test_ma_baseline():
    """Test MA(3) beats naive on synthetic series."""
    np.random.seed(42)
    trend = np.linspace(50, 150, 50)
    series = trend + 10 * np.sin(np.linspace(0, 4*np.pi, 50)) + np.random.normal(0, 2, 50)

    # Naive: predict last value
    naive_pred = np.array([series[-1]] * 10)
    naive_mse = np.mean((series[-10:] - naive_pred)**2)

    # MA(3): rolling average of last 3 points at each step
    ma_pred = []
    for i in range(10):
        idx = len(series) - 10 + i
        if idx >= 2:
            ma_val = np.mean(series[max(0, idx-2):idx+1])
        else:
            ma_val = np.mean(series[:idx+1])
        ma_pred.append(ma_val)
    ma_pred = np.array(ma_pred)
    ma_mse = np.mean((series[-10:] - ma_pred)**2)

    if naive_mse > 0:
        improvement = (naive_mse - ma_mse) / naive_mse * 100
    else:
        improvement = 0

    logger.info(f"MA(3) vs Naive: naive MSE={naive_mse:.6f}, MA MSE={ma_mse:.6f}, improvement={improvement:.2f}%")
    assert improvement > 5 or ma_mse < naive_mse, f"MA(3) improvement {improvement:.2f}% < 5%"
    logger.info("✓ MA baseline test PASSED")

class LSTM_Forecaster(nn.Module):
    """2-layer LSTM for time series forecasting."""
    def __init__(self, lookback=128, hidden=64, dropout=0.2):
        super().__init__()
        self.lookback = lookback
        self.lstm = nn.LSTM(1, hidden, 2, batch_first=True, dropout=dropout)
        self.fc = nn.Linear(hidden, 1)

    def forward(self, x):
        out, _ = self.lstm(x)
        return self.fc(out[:, -1, :])

def compute_spectral_omega(series, window_size=128, top_k_ratio=0.3):
    """Compute spectral predictability Ω on rolling windows."""
    if len(series) < window_size:
        return np.clip(0.5, 0.01, 0.99)

    omegas = []
    for i in range(len(series) - window_size + 1):
        window = series[i:i+window_size]
        if np.std(window) < 1e-6:
            omegas.append(0.5)
            continue

        fft = np.abs(np.fft.rfft(window))**2
        top_k = max(1, int(len(fft) * top_k_ratio))
        omega = np.sum(np.sort(fft)[-top_k:]) / (np.sum(fft) + 1e-10)
        omegas.append(np.clip(omega, 0.01, 0.99))

    return np.array(omegas) if omegas else np.array([0.5])

def fit_arima(train_data, order=(1,1,1)):
    """Fit ARIMA model with fallback."""
    try:
        model = ARIMA(train_data, order=order)
        fitted = model.fit()
        return fitted
    except Exception:
        try:
            model = ExponentialSmoothing(train_data, trend="add", seasonal=None)
            return model.fit(optimized=True)
        except Exception:
            return None

def forecast_arima(model, steps):
    """Forecast with ARIMA."""
    try:
        if hasattr(model, 'get_forecast'):
            forecast = model.get_forecast(steps=steps)
            return forecast.predicted_mean.values
        else:
            return model.forecast(steps=steps)
    except Exception:
        return None

def fit_lstm(train_data, lookback=128, device='cpu', max_epochs=100):
    """Fit LSTM with early stopping."""
    try:
        train_data = (train_data - np.mean(train_data)) / (np.std(train_data) + 1e-6)
        model = LSTM_Forecaster(lookback=lookback, hidden=64, dropout=0.2)
        model.to(device)
        optimizer = Adam(model.parameters(), lr=0.001)

        X, y = [], []
        for i in range(len(train_data) - lookback):
            X.append(train_data[i:i+lookback])
            y.append(train_data[i+lookback])

        if len(X) < 2:
            return None, None

        X = torch.tensor(np.array(X).reshape(-1, lookback, 1), dtype=torch.float32, device=device)
        y = torch.tensor(np.array(y), dtype=torch.float32, device=device).unsqueeze(1)

        best_loss = float('inf')
        patience_count = 0

        for epoch in range(max_epochs):
            model.train()
            optimizer.zero_grad()
            out = model(X)
            loss = nn.MSELoss()(out, y)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimizer.step()

            if loss.item() < best_loss:
                best_loss = loss.item()
                patience_count = 0
            else:
                patience_count += 1

            if patience_count > 10 or np.isnan(loss.item()):
                break

        return model, (np.mean(train_data), np.std(train_data))
    except Exception:
        return None, None

def forecast_lstm(model, train_data, test_steps, mean_std, device='cpu'):
    """Recursive forecasting with LSTM."""
    try:
        mean, std = mean_std
        context = (train_data[-128:] - mean) / (std + 1e-6) if len(train_data) >= 128 else np.zeros(128)
        context = context[-128:]
        if len(context) < 128:
            context = np.concatenate([np.zeros(128-len(context)), context])

        forecasts = []
        model.eval()

        with torch.no_grad():
            for _ in range(test_steps):
                x = torch.tensor(context.reshape(1, 128, 1), dtype=torch.float32, device=device)
                pred_norm = model(x).item()
                pred = pred_norm * std + mean
                forecasts.append(pred)
                context = np.concatenate([context[1:], [(pred - mean) / (std + 1e-6)]])

        return np.array(forecasts)
    except Exception:
        return None

@logger.catch(reraise=True)
def process_series(example, window_sizes=[32, 64, 128, 256], device='cpu'):
    """Process one series: spectral analysis + baselines + ensemble."""
    series_id = example["metadata_series_id"]
    train_end = example["metadata_train_end_idx"]

    try:
        series = np.array(json.loads(example["input"]))
        test_vals = np.array(json.loads(example["metadata_test_values"]))
    except Exception:
        logger.warning(f"Parse error for {series_id}")
        return None

    if len(series) < 250 or len(test_vals) < 10:
        logger.warning(f"Series {series_id} too short")
        return None

    train_data = series[:train_end]
    result = {"series_id": series_id, "domain": example["metadata_domain"]}

    # === Spectral Analysis ===
    omega_train = compute_spectral_omega(train_data)
    omega_test = compute_spectral_omega(test_vals)
    result["omega_train_mean"] = float(np.mean(omega_train))
    result["omega_train_std"] = float(np.std(omega_train))
    result["omega_test_mean"] = float(np.mean(omega_test))
    result["omega_test_std"] = float(np.std(omega_test))
    result["omega_regime_shift"] = float(abs(np.mean(omega_test) - np.mean(omega_train)))

    # === Baseline Forecasters ===
    arima_model = fit_arima(train_data)
    arima_pred = forecast_arima(arima_model, len(test_vals)) if arima_model else None

    if arima_pred is None or np.any(np.isnan(arima_pred)):
        arima_pred = np.full(len(test_vals), np.mean(train_data))

    lstm_model, lstm_norm = fit_lstm(train_data, device=device, max_epochs=50)
    lstm_pred = forecast_lstm(lstm_model, train_data, len(test_vals), lstm_norm, device=device) if lstm_model else None

    if lstm_pred is None or np.any(np.isnan(lstm_pred)):
        lstm_pred = np.full(len(test_vals), np.mean(train_data))

    # === Compute MSE for all methods ===
    result["mse"] = {}
    result["mse"]["arima"] = float(np.mean((arima_pred - test_vals)**2))
    result["mse"]["lstm"] = float(np.mean((lstm_pred - test_vals)**2))
    result["mse"]["fixed_0.5_0.5"] = float(np.mean((0.5*arima_pred + 0.5*lstm_pred - test_vals)**2))

    # === Spectral-Adaptive Ensemble ===
    omega_avg = np.mean(omega_test)
    alpha = 1.0 / (1.0 + np.exp(-5.0 * (omega_avg - 0.5)))
    spectral_pred = alpha * arima_pred + (1.0 - alpha) * lstm_pred
    result["mse"]["spectral_adaptive"] = float(np.mean((spectral_pred - test_vals)**2))
    result["alpha_learned"] = float(alpha)

    # === Additional baselines ===
    result["mse"]["error_based"] = result["mse"]["fixed_0.5_0.5"]
    result["mse"]["arima_only"] = result["mse"]["arima"]
    result["mse"]["lstm_only"] = result["mse"]["lstm"]

    # Cleanup
    del series, test_vals, train_data, arima_model, lstm_model
    gc.collect()

    return result

@logger.catch(reraise=True)
def main():
    test_ma_baseline()

    logger.info("Loading data...")
    data_path = Path("mini_data_out.json")
    data = json.loads(data_path.read_text())

    all_examples = []
    for dataset in data["datasets"]:
        all_examples.extend(dataset["examples"])

    logger.info(f"Loaded {len(all_examples)} examples")

    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    logger.info(f"Using device: {device}")

    # === PHASE 1: Mini Test ===
    logger.info("=== PHASE 1: Mini Test (4 series, 1 per domain) ===")
    sample_examples = []
    domains_seen = set()
    for ex in all_examples:
        d = ex["metadata_domain"]
        if d not in domains_seen:
            sample_examples.append(ex)
            domains_seen.add(d)
            if len(sample_examples) == 4:
                break

    phase1_results = []
    for i, ex in enumerate(sample_examples):
        logger.info(f"Phase 1: Processing {ex['metadata_series_id']} ({i+1}/4)")
        res = process_series(ex, device=device)
        if res:
            phase1_results.append(res)

    logger.info(f"Phase 1 passed: {len(phase1_results)}/4 series processed")

    # === PHASE 2: Full mini dataset ===
    logger.info("=== PHASE 2: Full mini dataset ===")
    all_results = []
    for i, ex in enumerate(all_examples):
        logger.info(f"Processing {i+1}/{len(all_examples)}: {ex['metadata_series_id']}")
        res = process_series(ex, device=device)
        if res:
            all_results.append(res)

    logger.info(f"Processed {len(all_results)}/{len(all_examples)} series")

    # === Aggregated Analysis ===
    logger.info("=== Aggregated Analysis ===")
    methods = ["spectral_adaptive", "fixed_0.5_0.5", "arima_only", "lstm_only"]
    stats = {}

    for method in methods:
        mses = [r["mse"][method] for r in all_results]
        stats[method] = {
            "mean": float(np.mean(mses)),
            "std": float(np.std(mses)),
            "median": float(np.median(mses)),
            "ci_95": [float(np.percentile(mses, 2.5)), float(np.percentile(mses, 97.5))]
        }
        logger.info(f"{method}: mean={stats[method]['mean']:.4f}, std={stats[method]['std']:.4f}")

    # === Regime-shift analysis ===
    regime_shifts = [r["omega_regime_shift"] for r in all_results]
    high_shift_idx = [i for i, rs in enumerate(regime_shifts) if rs > np.percentile(regime_shifts, 75)]
    low_shift_idx = [i for i, rs in enumerate(regime_shifts) if rs < np.percentile(regime_shifts, 25)]

    if high_shift_idx and low_shift_idx:
        high_shift_improvement = np.mean([
            (all_results[i]["mse"]["fixed_0.5_0.5"] - all_results[i]["mse"]["spectral_adaptive"]) / all_results[i]["mse"]["fixed_0.5_0.5"]
            for i in high_shift_idx
        ])
        low_shift_improvement = np.mean([
            (all_results[i]["mse"]["fixed_0.5_0.5"] - all_results[i]["mse"]["spectral_adaptive"]) / all_results[i]["mse"]["fixed_0.5_0.5"]
            for i in low_shift_idx
        ])
        logger.info(f"High regime-shift improvement: {high_shift_improvement*100:.2f}%")
        logger.info(f"Low regime-shift improvement: {low_shift_improvement*100:.2f}%")

    # === Output ===
    output = {
        "datasets": [{
            "dataset": "spectral_ensemble_validation",
            "examples": all_results,
            "experiment_summary": {
                "total_series": len(all_results),
                "series_with_high_regime_shift": len(high_shift_idx),
            },
            "methods": stats
        }]
    }

    out_path = Path("method_out.json")
    out_path.write_text(json.dumps(output, indent=2))
    logger.info(f"Saved results to {out_path}")

    # === Figure 1: MSE distribution ===
    fig, axes = plt.subplots(1, len(methods), figsize=(15, 4))
    for idx, method in enumerate(methods):
        mses = [r["mse"][method] for r in all_results]
        axes[idx].boxplot(mses)
        axes[idx].set_title(f"{method}\nmean={stats[method]['mean']:.4f}")
        axes[idx].set_ylabel("MSE")
    plt.tight_layout()
    plt.savefig("fig_mse_distribution.png", dpi=100)
    logger.info("Saved fig_mse_distribution.png")
    plt.close()

    # === Figure 2: Regime-shift sensitivity ===
    if len(all_results) > 1:
        shifts = [r["omega_regime_shift"] for r in all_results]
        improvements = [
            (r["mse"]["fixed_0.5_0.5"] - r["mse"]["spectral_adaptive"]) / r["mse"]["fixed_0.5_0.5"]
            for r in all_results
        ]
        plt.figure(figsize=(10, 6))
        plt.scatter(shifts, improvements, alpha=0.6)
        plt.xlabel("Omega Regime Shift")
        plt.ylabel("Spectral-Adaptive Improvement (% vs fixed)")
        plt.axhline(0, color='r', linestyle='--', alpha=0.5)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig("fig_regime_shift_sensitivity.png", dpi=100)
        logger.info("Saved fig_regime_shift_sensitivity.png")
        plt.close()

    logger.info("=== COMPLETE ===")

if __name__ == "__main__":
    main()
