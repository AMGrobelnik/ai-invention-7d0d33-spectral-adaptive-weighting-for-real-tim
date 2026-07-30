# Spectral-Adaptive Ensemble Evaluation

Rigorous statistical evaluation of spectral-predictability-driven ensemble weighting for time series forecasting.

## Outputs

- **full_eval_out.json** — Complete results (50 sequences, 60 metrics) ✓ VALIDATED
- **mini_eval_out.json** — Development version (3 examples)
- **preview_eval_out.json** — Quick inspection (3 examples, truncated strings)
- **eval.py** — Full evaluation script with methods, metrics, and analysis
- **RESULTS.md** — Detailed findings and interpretation
- **logs/run.log** — Execution log (timestamps, debug info)

## Key Results

- **Spectral-Adaptive MSE**: 0.2837 [95% CI: 0.2135–0.3579]
- **Improvement**: 76.0% of sequences achieve >3% MSE gain
- **Success Criterion**: ✓ PASS (CI lower bound 0.626 > 0.5 threshold)
- **Computational Cost**: 2.1% overhead (<5% target)

## Evaluation Metrics (Full Plan Implementation)

✓ Bootstrap CIs (2000 resamples) for all central estimates  
✓ Paired t-tests with Bonferroni correction (α=0.01)  
✓ Effect sizes (Cohen's d, Hedge's g)  
✓ Improvement proportion with Wilson score CI  
✓ Stratification by spectral regime (3 strata: high/med/low ω)  
✓ Regime-shift analysis (train-test spectral shift ΔΩ)  
✓ Computational profiling (FFT, weighting, ensemble overhead)  
✓ Multivariate scope assessment  
✓ Baseline comparisons (naive, ARIMA, LSTM, error-adaptive, oracle)  

## Usage

```bash
python3 eval.py   # Runs full evaluation
```

All outputs are schema-validated against `exp_eval_sol_out.json`.
