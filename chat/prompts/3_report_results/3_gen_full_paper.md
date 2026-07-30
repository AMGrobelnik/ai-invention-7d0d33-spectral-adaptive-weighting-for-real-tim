# gen_full_paper — report_results

> Phase: `gen_paper_repo` · `gen_full_paper`
> Run: `run_oxbmYex8-G2P` — Spectral Adaptive Weighting for Real-Time Ensemble Forecasting
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_full_paper` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-07-30 13:58:26 UTC

````
,
      "minLength": 12,
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "description": "Brief summary of the generated paper: sections written, figures included, compilation status",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/FullPaperExpectedFiles",
      "description": "All output files you created. Must include paper.tex, paper.pdf, references.bib, and paths to all figure files."
    }
  },
  "required": [
    "title",
    "summary",
    "out_expected_files"
  ],
  "title": "FullPaper",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `./.terminal_claude_agent_struct_out.json` exists and contains JSON matching the schema above.

Test whether a 3-point moving average beats a naive last-value forecast on a short synthetic series. Keep the investigation minimal.
</prompt><system-prompt>
<research_methodology>
Write like an experienced academic. Reviewers judge both the science and the writing.

- Claims must be proportional to evidence. Choose verbs carefully — "demonstrate," "observe," and "hypothesize" mean different things.
- Every result needs: what was measured, on what data, the numbers, and what they mean.
- Methodology must be specific enough to reproduce. Related work must be organized by theme, not a literature dump.
- State limitations honestly. Avoid both overclaiming and excessive hedging.
</research_methodology>

<system_reminder>
Do not ask follow up questions and do not ask the user anything. Execute all steps independently.
You must follow the todo list provided in each prompt exactly as written.
No placeholders, stubs, or incomplete code — all code must be complete and functional.
</system_reminder>

<process_isolation>
CRITICAL: Multiple pipeline runs may execute simultaneously on this machine. `ps aux | grep method.py` matches ALL runs, not just yours.
- NEVER kill processes by name (`killall`, `pkill -f`, `ps aux | grep ... | xargs kill`). This kills OTHER runs' processes.
- NEVER monitor processes by name (`ps aux | grep method.py`). You will see other runs' processes and get confused.
- ALWAYS use PID-based process management:
  Run: `uv run method.py & PID=$!` or `timeout <seconds> uv run method.py & PID=$!`
  Check: `kill -0 $PID 2>/dev/null && echo "Running" || echo "Ended"`
  Stop: `kill $PID`
  Wait: `wait $PID; echo "Exit code: $?"`
  Monitor: `tail -f logs/run.log & TAIL_PID=$!` then `kill $TAIL_PID` when done
</process_isolation>
</system-prompt>

<prompt>
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_oxbmYex8-G2P/4_gen_paper_repo/_4_assemble_paper/paper/workspace`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_oxbmYex8-G2P/4_gen_paper_repo/_4_assemble_paper/paper/workspace/`:
GOOD: `/ai-inventor/aii_data/runs/run_oxbmYex8-G2P/4_gen_paper_repo/_4_assemble_paper/paper/workspace/file.py`, `/ai-inventor/aii_data/runs/run_oxbmYex8-G2P/4_gen_paper_repo/_4_assemble_paper/paper/workspace/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>

<task>
Create a publication-ready top-conference LaTeX paper with BibTeX from <paper_text> and <available_figures>, compile to PDF.
</task>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<paper_text>
title: Spectral Adaptive Weighting for Real-Time Ensemble Forecasting
abstract: >-
  Time series forecasting accuracy depends on data regularity: smooth, periodic series favor linear models, while chaotic
  series benefit from nonlinear methods. Recent work demonstrates that spectral predictability Ω—a scalar metric quantifying
  power spectrum concentration—reliably indicates which model classes will succeed. However, Ω has been used only for offline
  model selection; this work operationalizes it for online dynamic weighting. We propose spectral-adaptive ensemble weighting:
  monitor Ω on a rolling window in real time and dynamically reweight a fixed two-component ensemble (ARIMA + LSTM) via a
  learned monotone function α(Ω). Experiments on 50 synthetic AR(1) series with controlled spectral properties validate the
  approach: spectral-adaptive achieves 0.284 MSE versus 0.472 for naive baseline (40% improvement, p < 0.0001, d = −0.494)
  and 0.284 MSE versus 0.322 for error-based dynamic weighting (12% improvement, p = 0.0003, d = −0.136). Strongest gains
  occur in medium-to-low regularity regimes where ensemble adaptation is most valuable. Computational overhead is 2.1% of
  LSTM inference time. We validate our core monotonicity assumption via ablation: a non-monotone neural network weighting
  function yields no statistically significant improvement, confirming that monotone weighting is appropriate. The method
  requires no model retraining and no labeled regime boundaries, making it practical for deployment. We identify univariate
  scope and two-component ensemble limitation as primary directions for future work.
paper_text: |-
  # Introduction

  Time series forecasting is a foundational problem across domains: energy grids predict demand, traffic systems forecast congestion, and financial institutions estimate market movements. The diversity of time series—from smooth periodic patterns to chaotic volatility—makes no single forecasting method universally optimal. While individual methods excel on specific data types, practitioners typically deploy fixed ensembles that weight multiple models equally or via offline optimization, losing the ability to adapt as data characteristics change.

  Recent advances in forecastability measurement offer a new opportunity. Wang et al. [1] introduce spectral predictability Ω—a scalar metric derived from power spectrum entropy that quantifies data regularity on a scale [0,1]. Ω is computed in O(T log T) time via FFT and serves as a reliable pre-training model-selection indicator. Their large-scale validation across 28 datasets and 51 models (Spearman ρ = −0.65, p < 1e−20) confirms that high-Ω series (regular, periodic) benefit from any model, while low-Ω series (chaotic, irregular) prove difficult for all methods. Complementary work by Feng et al. [2] develops Spectral Coherence Predictability (SCP), refining the diagnostic framework to reveal frequency-band-specific and time-varying difficulty.

  These advances unlock a practical insight: spectral properties not only indicate which model to choose once—they indicate dynamically how much to trust each model type as data difficulty changes. A simple observation motivates the approach: when data is regular (high Ω), linear models efficiently exploit structure and require minimal parameters; when data is chaotic (low Ω), linear methods saturate and flexible nonlinear models become more valuable. This principle has deep roots in signal processing (adaptive filtering responds to signal statistics) and ecology (organisms partition effort based on environmental harshness).

  However, existing adaptive ensemble methods fall short of operationalizing this insight. Error-based weighting (adjusting inversely to recent forecast error) is reactive and provides no leading indicator of when to shift strategies [3]. Convex-optimized static weights [4, 5] are fixed per-series and break under distribution shift. Neural combiners [6, 7] require supervised training. Regime-switching ensembles [8] assume discrete regimes, missing continuous drift. None directly leverage the continuous, model-agnostic forecastability signal that spectral analysis provides.

  This paper proposes spectral-adaptive ensemble weighting: monitor Ω in real time on a rolling window and dynamically reweight a fixed two-component ensemble (ARIMA + LSTM) via a learned monotone weighting function α(Ω). High-Ω regimes favor linear components (parsimonious, efficient); low-Ω regimes favor nonlinear components (expressive, flexible). The key innovation is operationalizing Ω from a diagnostic (Wang et al. use it for model selection; Feng et al. use it for evaluation) into a prescriptive signal for online weighting, with zero model retraining or labeled regime data.

  ## Summary of Contributions

  - **Spectral-adaptive ensemble weighting:** First real-time dynamic reweighting application of Ω within a fixed ensemble, operationalizing recent theoretical advances in forecastability as a prescriptive online signal, distinct from prior uses in model selection or post-hoc diagnosis. No retraining required.
  - **Validated monotone weighting assumption:** Core assumption (higher Ω → higher linear weight) tested via ablation against non-monotone neural network weighting; results confirm monotonicity is appropriate (p = 0.851), providing empirical grounding for the functional form.
  - **Statistically rigorous evaluation:** Experiments on 50 synthetic AR(1) sequences with controlled spectral properties demonstrate 40% MSE reduction versus naive baseline and 12% improvement over error-based adaptive weighting, both with p < 0.001 and Cohen's d effect sizes.
  - **Online Ω computation:** Efficient rolling-window spectral analysis enabling per-forecast-step adaptation; 2.1% computational overhead of LSTM inference time.
  - **Zero retraining, no labeled regimes:** Practical for deployment; weighting function learned on held-out validation data, then applied at inference with zero adaptation overhead per forecast step beyond Ω computation.

  # Related Work

  ## Spectral Predictability Metrics

  Wang et al. [1] introduce spectral predictability Ω = 1 − H(x)/H_max, where H(x) is Shannon entropy of the normalized power spectral density. Ω concentrates power (high → periodic, predictable; low → diffuse, chaotic). Large-scale analysis (28 datasets, 51 models) yields strong negative correlation between Ω and MSE (Spearman ρ = −0.65, p = 1.9×10^−21). Zero-shot foundation model forecasters (e.g., TimeLLM) gain 60% advantage over baselines in high-Ω regimes but lose edge at low Ω, demonstrating model-family-specific responses.

  Feng et al. [2] extend this with Spectral Coherence Predictability (SCP), using Welch spectral estimation to compute frequency-band-resolved difficulty. SCP isolates task difficulty (inherent in data) from model capability (how models exploit it), revealing time-varying predictability drift and enabling stratified evaluation that exposes complementary architectural strengths. Unlike Ω (which requires only history), SCP requires paired history-future segments, making it suitable for validation analysis.

  ## Ensemble Weighting Strategies

  Error-based dynamic weighting adjusts weights inversely to recent MSE: w_i(t) ∝ 1/MSE_i(t−k:t) [3]. Advantages include simplicity and responsiveness to short-term drift; disadvantages include purely reactive behavior with no leading indicator of regime shifts.

  Convex-optimized static weights solve min ||y − Σ w_i·f_i||² on training data [4, 5]. Hammam et al. [5] integrate ARIMA with XGBoost using grid-search weight optimization, achieving MAPE < 13% on most datasets and up to 80% improvement over ARIMA-only on high-variability patterns. However, static weights break under distribution shift.

  Neural combiners train small neural networks to learn weights given model predictions [6, 7]. Adhikari & Jain [6] propose a linear combination method via neural networks; Kourentzes et al. [7] show ensemble-of-networks outperforms single models. These require supervised training and remain static per-series.

  Regime-switching ensembles assume discrete regimes (trending vs. stationary) [8]. Interpretable but requires regime boundaries or Markov switching; misses continuous drift.

  ## Novelty and Positioning

  Spectral-adaptive is the first application of Ω for real-time dynamic weighting within a fixed ensemble. Unlike Wang et al. [1] using Ω for pre-training model selection (offline decision: pick best model class for this series), we use Ω for in-inference weighting (online: adjust blend as data difficulty changes moment-by-moment). Unlike error-based approaches [3], we use a leading indicator (spectral properties) rather than reactive error accumulation, potentially enabling faster response to regime shifts. Unlike static or regime-switching methods [4, 8], we enable continuous, online adaptation without discrete boundaries or offline convex optimization. The insight—that forecastability should directly inform ensemble weighting—bridges recent theoretical advances in forecastability with practical online adaptation.

  # Methods

  ## Core Algorithm

  The spectral-adaptive ensemble combines two fixed forecasters:
  - **Linear component:** ARIMA(1,1,1), fitted once per series on training data
  - **Nonlinear component:** 2-layer LSTM with 64 hidden units per layer, dropout=0.2, look-back window T_in=128

  At each forecast step t, the ensemble (1) computes spectral predictability Ω(t) on a rolling window of recent history, (2) maps Ω(t) to blend weight α ∈ [0,1] via a learned weighting function, (3) outputs combined forecast ŷ_t = α·ARIMA(t) + (1−α)·LSTM(t).

  **Spectral Predictability Computation:**
  For a rolling window of T_w recent points, compute FFT power spectrum P_k, normalize by total power, compute Shannon entropy H(x) = −Σ (P_k / ΣP_j) log(P_k / ΣP_j), and set Ω = 1 − H(x) / log(T_w/2). Ω ∈ [0,1]; high indicates concentrated power (regular patterns), low indicates diffuse spectrum (chaotic patterns). Complexity: O(T_w log T_w) ≈ milliseconds for typical T_w ∈ {100, 128, 256}.

  **Weighting Function:**
  We evaluated four functional forms:
  - **Logistic (default):** α(Ω) = 1 / (1 + exp(−a(Ω − b))), where a controls steepness and b is inflection point. Smooth, differentiable, interpretable.
  - **Linear:** α(Ω) = c·Ω + d with α ∈ [0,1]; simplest, no hyperparameters if normalized.
  - **Power law:** α(Ω) = Ω^p for flexible concavity.
  - **Step:** α(Ω) = 1 if Ω > threshold, else 0; interpretable but discontinuous.

  We recommend logistic as default: smooth transition at inflection point (typically b ≈ 0.5), tunable steepness (a), and no discontinuities. Ablation results confirm logistic is appropriate.

  **Hyperparameter Tuning:**
  Weighting function parameters (a, b for logistic) are tuned on a held-out validation set (10% of training data) by minimizing ensemble MSE against true labels. Grid search over (a, b) ∈ [0.1, 50] × [0.1, 0.9] with granularity 0.1 yields optimal weighting. Computational cost: negligible (O(1) evaluation per forecast step). Validation error vs. grid size showed 10% split optimal; 5% undershoots (0.8% worse), 15% overshoots (0.6% worse).

  ## Model Architectures

  **ARIMA (Linear Component):**
  Fit ARIMA(1,1,1) via statsmodels. Fit cost: 0.1–1s per series; forecast: ~1ms. Competitive, interpretable baseline capturing linear trends efficiently. This fixed order was chosen for consistency across experiments; data-dependent order selection via AIC is a straightforward extension.

  **LSTM (Nonlinear Component):**
  2 LSTM blocks, 64 units each, dropout=0.2. Look-back window T_in=128 points. Batch 32, Adam optimizer (lr=0.001), MSE loss, up to 100 epochs with early stopping (patience=10). Train cost: 5–30s on CPU; inference: ~5ms. Captures complex nonlinear dependencies; requires sufficient training data.

  ## Datasets and Experimental Setup

  **Synthetic AR(1) Series:**
  50 time series generated as AR(1) processes: x_t = ρ·x_{t−1} + ε_t, where ρ ∈ [0.2, 0.95] (autoregressive coefficient proxy for spectral properties) and ε_t ∼ N(0, σ²) with σ ∈ [0.1, 0.5]. Each series: 200 training points, 50 test points. Ω estimated as ρ (true spectral regularity). This controlled experimental setup enables precise hypothesis testing: higher ρ should favor ARIMA; lower ρ should favor LSTM.

  **Regime-Shift Quantification:**
  Compute rolling Ω over training period (100-point windows), then Ω on test set. Shift metric: ΔΩ = Ω_test − Ω_train_mean. Hypothesis assumes largest gains when ΔΩ > 0.2 (substantive shift).

  # Experiments

  ## Baselines and Metrics

  **Baselines:**
  1. **Naive last-value:** Repeat final training point for all test steps.
  2. **MA(3):** 3-point moving average; updates recursively on rolling window.
  3. **ARIMA(1,0,0):** Autoregressive fit via regression on lag-1.
  4. **LSTM-simple:** Weighted average of look-back window (weights linear in recency).
  5. **Error-adaptive:** Inverse-error weighting over MA(3), ARIMA, LSTM.
  6. **Spectral-adaptive:** Logistic α(Ω) learned on validation set.
  7. **Oracle optimal:** Offline oracle weights minimizing test MSE.

  **Metrics:**
  Primary: Mean Squared Error (MSE). Secondary: Mean Absolute Percentage Error (MAPE) for interpretability. Report mean and 95% bootstrapped confidence intervals (2000 resamples) across all test sequences. Statistical testing: paired t-tests with Bonferroni correction (α=0.01), Cohen's d effect sizes.

  ## Main Results

  [FIGURE:fig_results_comparison]

  Spectral-adaptive ensemble achieves 0.284 MSE [0.214, 0.358] (95% CI from 2000-resample bootstrap), significantly outperforming naive baseline 0.472 MSE [0.351, 0.603] with p < 0.0001 and Cohen's d = −0.494 (medium effect). The ensemble improves on 76% of test sequences (Wilson score CI [0.626, 0.857]).

  Comparison to error-based dynamic weighting (0.322 MSE [0.244, 0.408]): spectral-adaptive achieves 12% lower MSE with p = 0.0003 and d = −0.136 (small effect), validating the proactive leading-indicator approach. Spectral-adaptive shows no statistically significant difference vs. ARIMA-only (0.265 MSE [0.187, 0.352], p = 0.831), suggesting the learned weighting neither adds nor subtracts value in this controlled setting, but stratified results (below) reveal value in specific regimes.

  ## Stratified Analysis by Spectral Regime

  [FIGURE:fig_regime_stratified]

  Dividing sequences into spectral regimes (high Ω > 0.7, medium 0.4 ≤ Ω ≤ 0.7, low Ω < 0.4):

  - **High-Ω regime (20 sequences):** Spectral-adaptive MSE = 0.400, naive baseline = 0.722. Spectral-adaptive matches ARIMA (both favor linear weights at high Ω).
  - **Medium-Ω regime (24 sequences):** Spectral-adaptive MSE = 0.242, naive baseline = 0.489. **Largest gains here** (51% improvement over baseline). Balanced linear-nonlinear weighting is most valuable.
  - **Low-Ω regime (6 sequences):** Spectral-adaptive MSE = 0.064, naive baseline = 0.144. Spectral-adaptive favors LSTM (nonlinear weights at low Ω), achieving 56% improvement.

  This stratification validates the core hypothesis: ensemble adaptation is most valuable in medium-to-low regularity regimes where neither pure linear nor pure nonlinear methods dominate.

  ## Ablation Studies

  **Monotone vs. Non-Monotone Weighting:**
  We trained a non-monotone weighting function f_θ(Ω) using a 2-layer neural network (32 hidden units, ReLU activation) on the same validation data. Results: non-monotone f_θ achieves 0.285 MSE (test), virtually identical to monotone logistic 0.284 MSE (t = −0.188, p = 0.851, d = −0.009, negligible effect). This ablation confirms the monotone assumption is empirically justified—the additional flexibility of a non-monotone function provides no benefit. We conclude monotone weighting is appropriate for this task.

  **Rolling Window Size T_w:**
  Test T_w ∈ {32, 50, 64, 100, 128, 256}. Results: T_w=128 achieves lowest MSE (0.284) with lowest variance. T_w=100 performs within 0.3% of optimal; T_w=256 lags by ~2% (increased smoothing). T_w=50 is ~1% worse. Recommendation: T_w=128 balances responsiveness and stability; practitioners should validate on their data.

  **Weighting Function Form:**
  Ablation on functional forms: Logistic MSE=0.284, Linear MSE=0.290 (2.4% worse), Power-law (p=2) MSE=0.292 (2.9% worse), Step function MSE=0.316 (11% worse, high variance). Logistic recommended as default.

  **Validation Split Size:**
  Using 5%, 10%, 15%, 20% of training data for parameter tuning: 10% yields optimal results (0.284 MSE); 5% undershoots (0.289 MSE, 1.8% worse), 15% overshoots (0.285 MSE, 0.3% worse). Recommendation: 10% validation split.

  ## Computational Overhead

  Rolling Ω computation (T_w=128): ~2.5ms per forecast step (FFT via scipy.fftpack). Weighting function evaluation α(Ω): ~0.8ms (sigmoid evaluation). Ensemble averaging: ~1.2ms. Total overhead: ~4.5ms, or 2.1% relative to LSTM inference (~210ms on CPU). Overhead is negligible and well within practical limits for real-time deployment.

  # Discussion

  ## Strengths

  **Operationalizes recent theory:** Recent advances in spectral forecastability (Wang et al., Feng et al.) remain primarily diagnostic. Spectral-adaptive translates them into actionable online weighting, bridging theory and practice. This is the first application of Ω as an in-inference prescriptive signal.

  **Proactive over reactive:** Unlike error-based weighting which accumulates forecast errors before adapting (lag inherent in approach), spectral-adaptive uses a leading indicator (spectral properties shift before error accumulates). Experiments validate 12% advantage over error-based on this dataset, with potential for larger gains during sharp regime shifts not tested here.

  **Zero retraining:** Unlike neural combiners or regime-switching models, no supervised training of the weighting mechanism required after initial parameter tuning. Applicable to any fixed ensemble of forecasters.

  **Validated core assumption:** We empirically tested monotonicity via non-monotone neural network ablation, confirming the functional form is appropriate (p = 0.851). This grounds the method's design in evidence rather than intuition.

  **Consistent improvements:** Across synthetic data with controlled spectral properties, spectral-adaptive shows 40% improvement over naive baseline and 12% over error-based weighting, both with p < 0.001. Stratified results reveal value is concentrated in medium-to-low regularity regimes where ensemble adaptation is most beneficial.

  ## Limitations

  **Univariate scope:** Ω is defined for univariate signals. Multivariate extension is non-trivial. Modern forecasting benchmarks (PEMS traffic with multiple sensors, ETT with multiple energy channels) require per-channel analysis or PCA-based approximation; neither is implemented here. This is the primary barrier to applying spectral-adaptive to realistic multivariate forecasting tasks.

  **Two-component ensemble limitation:** Method applies only to two-component ensembles (ARIMA + LSTM). Extension to >2 components (e.g., ARIMA + LSTM + Transformer + ExponentialSmoothing) requires learning a weight vector α(Ω) over all pairs, increasing complexity and validation data requirements.

  **Controlled experimental setting:** Evaluation uses synthetic AR(1) series with spectral properties encoded in autoregressive coefficient. Real-world time series have richer spectral structure (multiple frequencies, non-stationary features) not captured here. Transfer to M4, PEMS, ETT benchmarks remains to be validated.

  **Hyperparameter sensitivity:** Window size T_w, weighting function form, and validation split size affect performance. Ablations show robustness (T_w ∈ {100, 128, 256} all perform well), but practitioners should validate on their data.

  ## Failure Modes and Open Questions

  When is spectral-adaptive worse than fixed ensemble?
  1. If both ARIMA and LSTM are poor models for the task (spectral weighting cannot overcome fundamental model mismatch).
  2. If Ω does not correlate with actual forecast accuracy for the specific models used (e.g., if domain-specific features matter more than spectral properties).
  3. If regime shifts are too rapid for rolling Ω to track (T_w too large for the drift rate).

  Diagnostic analysis via SCP [2] could reveal these cases post-hoc.

  ## Comparison to Existing Methods

  **vs. Wang et al. [1]:** Wang uses Ω for pre-training model selection (offline decision: pick best model class for this series, once). We use Ω for in-inference weighting (online: adjust blend as data difficulty changes moment-by-moment).

  **vs. Feng et al. [2]:** Feng uses SCP for post-hoc evaluation (diagnostic framework revealing model-specific strengths). We use Ω for prescriptive weighting (actionable signal). Feng's approach is complementary: SCP could enhance spectral-adaptive by providing frequency-band-specific weights.

  **vs. Error-based dynamic [3]:** Error-based reacts to past forecast error (inherent lag). Spectral-adaptive uses leading indicator (spectral properties shift before error accumulates); 12% improvement on our synthetic benchmark, with potential for larger gains during sharp transitions.

  **vs. Hammam et al. [5]:** Hammam optimizes ensemble weights offline via convex optimization (static per-series). We optimize weighting function on validation data, then apply dynamically based on real-time Ω (adaptive). Hammam achieves strong results on specific datasets (MAPE < 13%), but no adaptation across regime changes.

  # Conclusion

  We introduce spectral-adaptive ensemble weighting, operationalizing spectral predictability metrics into real-time online forecasting. By monitoring Ω and dynamically reweighting a fixed two-component ensemble, we achieve 40% MSE reduction over naive baselines and 12% improvement over reactive error-based methods on controlled synthetic data. The method requires no model retraining and no labeled regimes, making it practical for real-world deployment.

  Our validation of the monotone weighting assumption via ablation (p = 0.851) provides empirical grounding for the functional form. Stratified analysis reveals ensemble adaptation is most valuable in medium-to-low regularity regimes, where neither pure linear nor pure nonlinear methods dominate.

  Primary limitations are univariate scope and two-component ensemble restriction. Future work includes:
  - **Multivariate extension:** Per-channel Ω with learned aggregation (recommended), or SCP-based band-specific weighting (sophisticated but unimplemented).
  - **Ensemble generalization:** Learn weight vectors over >2 components.
  - **Benchmark validation:** Transfer to M4 (100k series), PEMS (traffic), and ETT (energy) to validate on realistic heterogeneous data.
  - **Adaptive window sizing:** Automatically adjust T_w based on detected drift rate (CUSUM-triggered).
  - **Theoretical analysis:** Characterize when spectral-adaptive outperforms error-based (prediction: during rapid regime shifts) and when it matches fixed ensemble (stable Ω).

  The core insight—that forecastability should directly inform ensemble weighting—is broadly applicable. We hope this work motivates extensions to multivariate data and larger ensemble combinations, unlocking the full potential of spectral analysis for adaptive forecasting.

  # References

  [1] O. Wang, P. Quan, K. Yang, and M. Srivastava. Spectral predictability as a fast reliability indicator for time series forecasting model selection. arXiv preprint arXiv:2511.08884, 2025.

  [2] W. Feng, Y. Yuan, J. Ding, and Y. Li. Beyond model ranking: Predictability-aligned evaluation for time series forecasting. arXiv preprint arXiv:2509.23074, 2025.

  [3] X. Sun, J. Yin, and Y. Zhao. Using the inverse of expected error variance to determine weights of individual ensemble members: Application to temperature prediction. Journal of Meteorological Research, 31(4):502–513, 2017.

  [4] L. Shen et al. Adaptive ensemble weight optimization for natural gas forecasting. Mathematics, 14(5):900, 2024.

  [5] I. M. Hammam, A. K. El-Kharbotly, and Y. Sadek. Adaptive demand forecasting framework with weighted ensemble of regression and machine learning models along life cycle variability. Scientific Reports, 15:23352, 2025.

  [6] R. Adhikari and A. K. Jain. A neural network based linear ensemble framework for time series forecasting. Neurocomputing, 157:231–242, 2015.

  [7] N. Kourentzes, D. K. Barrow, and S. F. Crone. Neural network ensemble operators for time series forecasting. Expert Systems with Applications, 41(9):4235–4244, 2014.

  [8] Z. Xu et al. Twin learning for domain agnostic time series analysis: A regime-switch perspective. Pattern Recognition, 165:111111, 2025.

  [9] S. Aminikhanghahi and D. Cook. A survey of methods for time series change point detection. Knowledge and Information Systems, 51(2):339–367, 2016.
summary: >-
  This paper operationalizes spectral predictability (Ω) as a real-time prescriptive signal for online ensemble weighting.
  We propose spectral-adaptive weighting: dynamically reweight a fixed ARIMA + LSTM ensemble by monitoring Ω on rolling windows
  via a learned monotone function α(Ω). On 50 synthetic AR(1) series with controlled spectral properties, spectral-adaptive
  achieves 40% MSE reduction over naive baseline (p < 0.0001) and 12% improvement over reactive error-based weighting (p =
  0.0003). Ablation confirms the monotone weighting assumption (p = 0.851). Stratified analysis reveals gains are concentrated
  in medium-to-low regularity regimes where ensemble adaptation is most beneficial. Computational overhead is 2.1% of LSTM
  inference time. The method requires no model retraining and no labeled regime boundaries. Primary limitations are univariate
  scope and two-component restriction; multivariate extension and larger ensemble generalization are identified as key future
  work.
</paper_text>

<available_figures>
--- Item 1 ---
id: fig_results_comparison
title: MSE Comparison Across Methods
caption: >-
  Mean squared error (MSE) across seven forecasting methods on 50 synthetic AR(1) sequences. Error bars show 95% bootstrapped
  confidence intervals (2000 resamples). Spectral-adaptive (0.284 MSE, CI [0.214, 0.358]) significantly outperforms naive
  last-value baseline (0.472 MSE, p < 0.0001, Cohen's d = −0.494) and error-adaptive weighting (0.322 MSE, p = 0.0003, d =
  −0.136). Performance is comparable to ARIMA-only (0.265 MSE, p = 0.831) in aggregate, but stratified results reveal value
  in specific spectral regimes.
image_gen_detailed_description: >-
  Bar chart with error bars. X-axis: seven methods (Naive-LastValue, MA(3), ARIMA, LSTM, Error-Adaptive, Spectral-Adaptive,
  Oracle). Y-axis: MSE (0.0 to 0.75, increments 0.1). Bar heights and error bars: Naive-LastValue=0.472 CI[0.351,0.603], MA3=0.449
  CI[0.325,0.580], ARIMA=0.265 CI[0.187,0.352], LSTM=0.432 CI[0.313,0.559], Error-Adaptive=0.322 CI[0.244,0.408], Spectral-Adaptive=0.284
  CI[0.214,0.358], Oracle=0.229 CI[0.169,0.298]. Colors: Naive=red, MA3=orange, ARIMA=blue, LSTM=purple, ErrorAdapt=yellow,
  SpectralAdapt=green (highlighted), Oracle=gray. Sans-serif font, white background, horizontal gridlines at 0.1 increments.
aspect_ratio: '21:9'
summary: >-
  Bar chart comparing MSE of seven forecasting methods with 95% confidence intervals, showing spectral-adaptive significantly
  outperforms reactive error-based weighting and naive baseline.
figure_path: figures/fig_results_comparison_v0.jpg

--- Item 2 ---
id: fig_regime_stratified
title: Performance Gains by Spectral Regime
caption: >-
  Spectral-adaptive MSE stratified by spectral regularity regime (high Ω > 0.7, medium 0.4 ≤ Ω ≤ 0.7, low Ω < 0.4). Largest
  gains occur in medium-regularity regime (51% improvement: 0.242 vs. 0.489 naive baseline) where neither pure linear nor
  pure nonlinear methods dominate, validating the core hypothesis that ensemble adaptation is most valuable in mixed-difficulty
  data.
image_gen_detailed_description: >-
  Grouped bar chart. X-axis: three spectral regimes (High ω>0.7, Medium 0.4≤ω≤0.7, Low ω<0.4). Y-axis: MSE (0.0 to 0.8, increments
  0.1). For each regime, show two bars (Naive Baseline, Spectral-Adaptive). High regime: Naive=0.722 (red), Spectral=0.400
  (green). Medium regime: Naive=0.489 (red), Spectral=0.242 (green). Low regime: Naive=0.144 (red), Spectral=0.064 (green).
  Legend: red=Naive, green=Spectral-Adaptive. Sample size labels below: n=20, n=24, n=6. Sans-serif font, white background,
  horizontal gridlines.
aspect_ratio: '21:9'
summary: >-
  Grouped bar chart showing spectral-adaptive MSE versus naive baseline stratified by spectral regime, with largest relative
  improvements in medium-regularity regime.
figure_path: figures/fig_regime_stratified_v0.jpg
</available_figures>

<figure_requirements>
CRITICAL: Include ALL figures from <available_figures>. No exceptions.

- Every figure MUST use \includegraphics{figures/filename.jpg}
- Do NOT skip, convert to tables, or describe without inserting
- Each needs: \begin{figure*|figure}[placement], \includegraphics, \caption, \label, \end{...} — pick env + placement by the figure's `aspect_ratio` field (see PLACEMENT below). Constrain every \includegraphics with `width=\linewidth,height=0.4\textheight,keepaspectratio` (single-column) or `width=\textwidth,height=0.45\textheight,keepaspectratio` (figure*). Use exactly these option keys — `max height=` is NOT valid LaTeX
- Use the `caption` field from each figure for \caption{...} — do NOT invent new captions
- Place figures where their [FIGURE:fig_id] markers appear in paper_text
- VERIFICATION: paper.tex MUST have exact same number of \includegraphics as <available_figures>
- Do NOT generate new figure images (no matplotlib, no PIL, no image generation). Use ONLY the pre-generated figures from <available_figures>. They were already created by a previous pipeline step.

PLACEMENT BY ASPECT RATIO (use the `aspect_ratio` field on each figure):
- `21:9` (architecture diagrams / hero figures): \begin{figure*}[!t] (full two-column width, top of page). The hero architecture diagram should appear EARLY in the paper — typically at the top of page 2. Marker placement in paper_text already determines this; preserve it.
- `16:9` (comparisons, multi-panel results): \begin{figure*}[!t] for full-width or \begin{figure}[!htbp] for single-column.
- `4:3` / `1:1` / `3:2` / `3:4` / `9:16`: \begin{figure}[!htbp] (single-column).
</figure_requirements>

<artifact_links>
The paper_text contains \footnote{Code: \url{...}} references linking to artifact source code
on GitHub. Include \usepackage{hyperref} and \usepackage{url}.
Preserve these exactly as-is — do not remove, rewrite, or convert them to plain text.
The URLs will not resolve yet (the repo is deployed after compilation) — do NOT try to verify or fix them.
</artifact_links>

<headings>
NEVER use inline math (``$...$``) inside ``\section{...}`` / ``\subsection{...}`` / ``\subsubsection{...}`` arguments — hyperref's bookmark builder errors out (``Token not allowed in a PDF string``) and the PDF outline breaks. If a section heading needs a math-looking term, use the text equivalent (``d star`` not ``$d^*$``, ``alpha-equivalent`` not ``$\alpha$-equivalent``) or wrap it in ``\texorpdfstring{$math$}{plain}``. Inline math inside body paragraphs is fine.
</headings>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-to-latex, aii-semscholar-bib.
TODO 2. Review <paper_text> and <available_figures>. Copy all figure images into ./figures/ in your workspace. Count figures — MUST include every one. Plan placements per section. Build `./references.bib` via aii_semscholar_bib__fetch — collect DOIs/ArXiv IDs from <paper_text> and batch-fetch all BibTeX in one call. Do NOT fabricate entries.
TODO 3. Create `./paper.tex` per aii-paper-to-latex skill's setup, write ALL sections, insert ALL figures from <available_figures>, include `./references.bib` via \bibliography. Compile to PDF per skill's process. Fix errors.
TODO 4. CRITICAL VERIFICATION: Run `grep -c 'includegraphics' paper.tex`, confirm count equals figures in <available_figures>. If not, add missing figures. Verify `./paper.pdf` was created.
TODO 5. VISUAL REVIEW: Write Python script to convert EVERY page of paper.pdf to PNG at 150 DPI (use pdf2image or pymupdf). Then read ALL page screenshots — each page image costs ~1,600 tokens so a 15-page paper is only ~24K tokens. You MUST read every page. The ONLY exception is if all page images would not fit in your remaining context — in that case, read as many as fit and state which pages you are skipping and why. Check every page for layout issues, overlapping figures, cut-off text, bad spacing, formatting problems. Fix issues and recompile.
TODO 6. FINAL READ: Check page count (`pdfinfo paper.pdf` or pymupdf). Read entire paper.pdf — check for missing sections, unclear explanations, inconsistencies, typos. Fix and recompile. The ONLY exception is if all pages would not fit in your remaining context — in that case, read as many pages as fit and state which pages you are skipping and why.
</todos>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "FullPaperExpectedFiles": {
      "description": "All expected output files from full paper generation.",
      "properties": {
        "paper_tex_path": {
          "description": "Path to LaTeX source file. Example: 'paper.tex'",
          "title": "Paper Tex Path",
          "type": "string"
        },
        "paper_pdf_path": {
          "description": "Path to compiled PDF. Example: 'paper.pdf'",
          "title": "Paper Pdf Path",
          "type": "string"
        },
        "references_bib_path": {
          "description": "Path to BibTeX bibliography file. Example: 'references.bib'",
          "title": "References Bib Path",
          "type": "string"
        },
        "figure_paths": {
          "description": "Paths to all figure image files. Example: ['figures/fig1_v0.jpg', 'figures/fig2_v0.jpg']",
          "items": {
            "type": "string"
          },
          "title": "Figure Paths",
          "type": "array"
        }
      },
      "required": [
        "paper_tex_path",
        "paper_pdf_path",
        "references_bib_path",
        "figure_paths"
      ],
      "title": "FullPaperExpectedFiles",
      "type": "object"
    }
  },
  "description": "Full paper \u2014 structured output from paper generation.",
  "properties": {
    "title": {
      "description": "Paper title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance. Aim for about 4-8 words (~40 characters).",
      "maxLength": 90
````

### [2] SKILL-INPUT — aii-paper-to-latex · 2026-07-30 13:58:32 UTC

The agent loaded the **aii-paper-to-latex** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-paper-to-latex
description: LaTeX paper assembly and compilation. Covers document setup, figure inclusion from pre-generated JPEGs, compilation process, and output files. Use when assembling a paper from pre-written text and pre-generated figures into a compiled PDF.
---

## LaTeX Paper Assembly

Assembles a research paper from paper text, pre-generated figure JPEGs, and bibliography into a compiled PDF.

### Document Setup

```latex
\documentclass[11pt,letterpaper]{article}
\usepackage{graphicx, geometry, amsmath, hyperref, natbib, booktabs, xcolor, listings}
\geometry{margin=1in}
\hypersetup{colorlinks=true, linkcolor=black, citecolor=black, urlcolor=black}
```

### Figure Inclusion

CRITICAL: Include ALL figures. Every figure MUST appear in the paper.

```latex
\begin{figure}[!htbp]
  \centering
  \includegraphics[width=0.92\textwidth,keepaspectratio]{figures/filename.jpg}
  \caption{Descriptive caption.}
  \label{fig:label}
\end{figure}
```

Rules:
- ALWAYS use `[!htbp]` float placement (NOT `[t]` or `[h]` alone)
- ALWAYS constrain with `width` and `keepaspectratio` to prevent page takeover
- Every figure needs `\caption`, `\label`, and a `\ref` in the text
- Do NOT convert figures to tables or describe them without inserting the image
- Do NOT skip any figures

### Compilation Process

Run each command separately (do NOT chain with `&&` — pdflatex often exits non-zero on warnings, which would skip bibtex and leave citations as `??`):

```bash
pdflatex -interaction=nonstopmode paper.tex
bibtex paper
pdflatex -interaction=nonstopmode paper.tex
pdflatex -interaction=nonstopmode paper.tex
```

All four commands are required. Skipping bibtex causes `??` in all citations.
Fix any errors between runs. Verify `./paper.pdf` was created.

### Output Files

- `./paper.tex` — LaTeX source
- `./references.bib` — bibliography file
- `./paper.pdf` — compiled PDF
- `./figures/*.jpg` — all figure images (pre-generated, copied into workspace)
````

### [3] SKILL-INPUT — aii-semscholar-bib · 2026-07-30 13:58:32 UTC

The agent loaded the **aii-semscholar-bib** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-semscholar-bib
description: Build bibliographies using Semantic Scholar. Batch-fetch BibTeX for papers by DOI, ArXiv ID, or title. Use when writing papers, generating reference lists, or building .bib files.
---

## Tool: `aii_semscholar_bib__fetch`

Batch-fetch BibTeX entries from Semantic Scholar. Pass all references in a single call — the tool handles batching internally.

### How it works

1. **DOI/ArXiv refs** → batched into POST /paper/batch calls (up to 500 per API call, auto-chunked)
2. **Title-only refs** → individual GET /paper/search/match (1s delay between)
3. **Post-process** → fix entry type, fix citation key (AuthorYYYY), inject DOI

The ability server runs a single worker (`max_threads: 1`). Multiple concurrent tool calls are queued — each runs independently (no cross-request aggregation). Batching happens within each request.

### Input format

```json
{
  "references": [
    {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
    {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
    {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
  ]
}
```

Each reference object can have:
- `doi` — DOI string (ArXiv DOIs like `10.48550/arXiv.XXXX.XXXXX` auto-convert to ArXiv IDs)
- `arxiv` — ArXiv ID (e.g. `"2305.14325"`)
- `title` — Paper title (used for search/match when no DOI/ArXiv)
- `author` — First author last name (for cleaner citation key)
- `year` — Publication year (int, for citation key)

At least one of `doi`, `arxiv`, or `title` is required per reference.

### Output format

```json
{
  "success": true,
  "bib_text": "@inproceedings{Vaswani2017, ...}\n\n@article{Wei2022, ...}",
  "total": 3,
  "found": 3,
  "failed_count": 0,
  "entries": [{"citation_key": "Vaswani2017", "bibtex": "...", "title": "...", "doi": "...", "arxiv": ""}],
  "failed": []
}
```

### Workflow

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Call `aii_semscholar_bib__fetch` with the full list in **one call**
3. Save `bib_text` from the response to your `references.bib` file
4. Check `failed` — for any missed papers, follow the **fallback procedure** below

### Fallback for failed references (MANDATORY)

NEVER fabricate BibTeX. For each failed reference:
1. **WebSearch** for `"Title" author year` (try `site:arxiv.org` too)
2. **WebFetch** the paper page → extract title, authors, year, venue, DOI/ArXiv ID
3. If DOI/ArXiv found → retry `aii_semscholar_bib__fetch` with it
4. Last resort: write BibTeX by hand using **only verified info from the actual paper page**

---

### CLI (for manual use / debugging)

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-semscholar-bib" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_semscholar_bib__fetch.py --refs '[
  {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
  {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
  {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
]'
```

`--json, -j` — output raw JSON instead of .bib text

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````
