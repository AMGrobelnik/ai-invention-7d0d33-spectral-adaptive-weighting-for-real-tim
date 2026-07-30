# upd_hypo — test_idea

> Phase: `invention_loop` · round 2 · `upd_hypo`
> Run: `run_oxbmYex8-G2P` — Spectral Adaptive Weighting for Real-Time Ensemble Forecasting
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `upd_hypo` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-07-30 13:35:20 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A hypothesis reviser (Step 3.6: UPD_HYPO in the invention loop)

You received the current hypothesis, all artifacts, and the paper draft.
Revise the hypothesis based on what the evidence supports.

Honest revision → focused research. Inflated confidence → wasted iteration.
</your_role>
</ai_inventor_context>

You are revising a research hypothesis based on empirical evidence gathered
during an iterative invention loop. Your role is internal reflection — honest
assessment of what the evidence supports.

SCOPE: Your ONLY output is the revised hypothesis text. You do NOT run code,
produce artifacts, fix bugs, or otherwise act on the evidence yourself — the
next iteration of the invention loop will spawn fresh artifacts based on your
revised hypothesis. Reflect on the evidence and rewrite the hypothesis;
nothing else.

PRINCIPLES:
- Ground every revision in specific artifacts and results
- Treat negative and null results as valuable contributions. If the original
  approach failed, the null result IS often the contribution — frame it as
  such (e.g. "X does not improve Y under conditions Z"). Only pivot to a
  different positive claim when the evidence actually supports one; never
  fabricate a positive narrative to mask a failed approach.
- Increase specificity as evidence accumulates
- Don't inflate confidence without strong evidence
- Preserve the core AII prompt unless evidence clearly contradicts it
- Revise hypothesis text only — never attempt to address feedback by running
  code, proposing fixes, or producing artifacts; the next loop iteration
  handles all artifact generation

<current_hypothesis>
The hypothesis as it stands. Revise it based on the evidence below.

kind: hypothesis
title: Spectral-Predictability-Driven Online Weighting (Validation Study)
hypothesis: >-
  Time series where spectral predictability Ω correlates with optimal linear-vs-nonlinear ensemble weighting can be identified
  via spectral analysis on rolling windows. A monotone weighting function α(Ω) can be learned on held-out validation data
  and applied at test time without model retraining. However, this approach remains UNVALIDATED on real benchmarks; multivariate
  extension, superiority over error-based weighting, and optimality of monotone weighting are unproven. Core contribution
  is establishing feasibility via rigorous experiments on M4/PEMS/ETT with confidence intervals and statistical significance
  testing. Univariate scope only—multivariate is deferred.
motivation: >-
  Recent work (Wang et al. 2025, Feng et al. 2026) shows spectral predictability Ω and Spectral Coherence Predictability (SCP)
  reliably indicate which model TYPES work best (transformers beat baselines in high-Ω regimes). However, practitioners still
  deploy fixed ensembles, losing the ability to adapt as data characteristics shift. The core insight is: predictability doesn't
  just tell us which model to pick once—it tells us dynamically HOW to weight an ensemble. Linear methods exploit regularity
  efficiently; nonlinear methods handle chaos. This bridges recent theoretical advances in forecastability with practical
  online forecasting, enabling zero-retrain adaptation.
assumptions:
- >-
  Spectral properties of short windows (e.g., 100-200 points) are stable enough to predict the next forecast horizon's difficulty
- >-
  Linear and nonlinear forecasters make meaningfully different errors on regular vs. irregular data (no redundancy in predictions)
- >-
  Computational cost of spectral analysis (O(N log N)) is negligible compared to model inference
- >-
  The optimal weighting function between linear and nonlinear methods is approximately monotone in Ω (higher Ω → higher linear
  weight)
investigation_approach: >-
  Construct a minimal two-component ensemble: (1) Auto-ARIMA or exponential smoothing as the linear baseline, (2) a small
  LSTM or ResNet as the nonlinear expert. For each forecast step, compute Ω (spectral predictability) on a rolling 128-point
  window. Map Ω ∈ [0,1] to blend weights α(Ω) ∈ [0,1] via a monotone function (e.g., logistic curve). Aggregate forecasts
  as α(Ω)·linear + (1−α(Ω))·nonlinear. Evaluate on standard benchmarks (M4, PEMS, ETTm datasets) with hold-out test periods
  where data properties shift. Compare against: (a) fixed 0.5/0.5 ensemble, (b) static per-series optimal weights, (c) recent
  adaptive ensembles (error-based weighting).
success_criteria: >-
  The spectral-adaptive ensemble achieves ≥3% lower test MSE than fixed-weight (0.5/0.5) ensemble on ≥70% of test sequences,
  especially on sequences where Ω shifts >0.2 between train and test. Gains are largest (≥5%) on 'regime-change' sequences
  (e.g., stationary→trending or vice versa). Computational overhead is <5% vs. static ensemble due to spectral computation.
related_works:
- >-
  Wang et al. (2025, arXiv:2511.08884): Spectral Predictability Ω as a model-selection indicator showing zero-shot transformers
  beat baselines when Ω is high. **Differs from our work**: Uses Ω for pre-training model selection, not for in-inference
  adaptive weighting within a single ensemble.
- >-
  Feng et al. (2026, arXiv:2509.23074): Spectral Coherence Predictability (SCP) with band-specific and time-varying difficulty
  estimates; shows predictability drift. **Differs**: SCP is diagnostic (evaluation framework), not prescriptive for online
  forecasting; we use related principles operationally for real-time weighting.
- >-
  Catt (2026, arXiv:2603.20546): Forecastability profiles via mutual information across horizons; theoretical bounds on achievable
  loss. **Differs**: Information-theoretic framing; no algorithmic contribution to adapt methods.
- >-
  Hammam et al. (2025): Adaptive ensemble weighting (ARIMA + XGBoost) via convex optimization. **Differs**: Their weighting
  is static per-series, trained offline; ours is dynamic, responding to in-stream spectral drift.
- >-
  Adhikari & Jain (2015): Neural network combining weights for linear/nonlinear forecasts. **Differs**: Offline learned combiner;
  no spectral-property-based adaptation.
- >-
  Elliott & Timmermann (2002): Optimal forecast combination under regime switching. **Differs**: Assumes discrete regimes;
  our approach is continuous, spectral-grounded.
inspiration: >-
  The inspiration spans three cross-domain sources: (1) **Signal Processing** — spectral coherence and frequency-domain regularity
  have long been used in control theory to diagnose system stability; here we apply the same principle to forecast method
  selection. (2) **Adaptive Filtering** — from control/signal processing, the idea that when the input signal's statistics
  change (captured by spectral shift), the optimal filter structure changes too. (3) **Ecologically-inspired adaptation**
  — in ecology, organisms partition effort based on environmental harshness; similarly, an ensemble can partition effort (weight)
  between conservative (linear) and exploratory (nonlinear) strategies based on data 'roughness' (low Ω = rough/chaotic; high
  Ω = smooth/regular).
terms:
- term: Spectral Predictability (Ω)
  definition: >-
    A scalar metric (Wang et al., 2025) quantifying the concentration of a time series' power spectrum. High Ω (close to 1)
    indicates strong frequency-domain structure (periodic, regular); low Ω (close to 0) indicates diffuse, irregular signal.
    Computed in O(N log N) via Fast Fourier Transform.
- term: Spectral Coherence Predictability (SCP)
  definition: >-
    An extension of Ω (Feng et al., 2026) that measures predictability separately within each frequency band and across time
    windows, revealing which frequency bands and time periods are forecastable, and which are chaotic.
- term: Adaptive Ensemble Weighting
  definition: >-
    Dynamically adjusting the contribution of different forecasting models based on real-time data characteristics, rather
    than using a fixed pre-computed weight.
- term: Regime Shift / Concept Drift
  definition: >-
    A change in the underlying statistical properties or generating process of a time series over time (e.g., shift from stationary
    to trending, or change in variance), captured by a shift in spectral properties Ω or SCP.
- term: Linear Forecaster
  definition: >-
    A forecasting method that captures only linear dependencies in the data (e.g., ARIMA, exponential smoothing). Computationally
    efficient and interpretable; excels on regular, periodic series.
- term: Nonlinear Forecaster
  definition: >-
    A neural network or machine learning method that learns nonlinear patterns (e.g., LSTM, ResNet, Transformer). More expressive
    but requires more data and computation; excels on chaotic or complex series.
summary: >-
  We propose a spectral-adaptive ensemble that monitors the spectral predictability (Ω or SCP) of incoming data in real time
  and dynamically reweights a fixed two-component ensemble (linear + nonlinear forecasters) without retraining. High-predictability
  regimes favor linear components (efficient, parsimonious); low-predictability regimes favor nonlinear components (flexible,
  expressive). This leverages recent advances in forecastability measurement (Wang 2025, Feng 2026) operationally, enabling
  zero-retrain online adaptation across regime changes.
_relation_rationale: >-
  Refined from claimed solution to validation framework; narrowed to univariate; made assumptions explicit
_confidence_delta: decreased
_key_changes:
- >-
  Reframed as VALIDATION STUDY, not validated solution. All paper results are currently placeholders without error bars, confidence
  intervals, or statistical significance tests.
- >-
  Narrowed scope to UNIVARIATE time series only. Multivariate extension (needed for PEMS/ETT proper) explicitly deferred as
  future work, not addressed by current method.
- >-
  Made core UNVALIDATED assumptions explicit: (1) Monotone weighting relationship in Ω (no ablation vs. non-monotone neural
  network), (2) T_w=128 optimal (no data-dependent justification; needs empirical grid search), (3) Hyperparameter tuning
  strategy underspecified (no explicit grid bounds, validation methodology).
- >-
  Repositioned novelty honestly. Spectral-adaptive is a proactive leading-indicator alternative to reactive error-based weighting
  (Sun et al.), not 'first in-inference application'—Wang et al. already use Ω for pre-training selection; applying at inference
  is incremental.
- >-
  Revised success criteria from specific claims (3% MSE on 70% of sequences) to demonstrating the hypothesis structure: (1)
  Does Ω correlate with optimal weighting on target models? (2) Can we learn α(Ω) on validation data? (3) Does it beat fixed
  0.5/0.5 and error-based baselines? Require 95% CIs, paired t-tests with Bonferroni correction, effect sizes.
- >-
  Added urgent experimental validation agenda: (1) Execute actual M4/PEMS/ETT experiments with explicit dataset specification
  (M4 sample seed, PEMS sensors, ETT target), reported confidence intervals and p-values; (2) Ablate monotone vs. non-monotone
  (neural network f_θ(Ω)) weighting to test core assumption; (3) Empirically justify rolling window size via grid sweep {32,50,100,128,256,512};
  (4) Benchmark computational overhead on real hardware (CPU: Intel/AMD; GPU: A100/RTX).
- >-
  Acknowledge major limitation upfront: Method handles univariate input only. Modern forecasting benchmarks (PEMS as multivariate
  traffic, ETT as multivariate energy) require per-channel Ω or SCP-based aggregation not implemented. Treating as separate
  univariate series loses spatial/correlative structure.
relation_type: evolution
</current_hypothesis>

<all_artifacts>
Complete set of research artifacts across all iterations.

--- Item 1 ---
id: art_RQ_kBRIORdTK
type: research
title: Spectral Forecasting Metrics and Adaptive Ensemble Design
summary: |-
  Recent literature (Wang et al. 2025, Feng et al. 2026, Hammam et al. 2025) establishes spectral predictability metrics as model-selection indicators and proposes adaptive ensemble approaches for time series forecasting.

  Ω (Spectral Predictability) [Wang et al., 2511.08884] is Ω = 1 - H(x)/H_max, where H(x) is Shannon entropy of normalized FFT power spectrum. Ω ∈ [0,1]; high indicates periodic/predictable; low indicates chaotic/irregular. O(T log T) FFT computation takes seconds. Controlled experiments show error decreases 20-40% as Ω rises 0.3→0.7. Large-scale validation (28 datasets, 51 models, Spearman ρ = -0.65, p < 1e-20) confirms utility. Zero-shot LLM forecasters outperform baselines by ~60% at high Ω; gap vanishes at low Ω.

  SCP (Spectral Coherence Predictability) [Feng et al., 2509.23074] uses Welch spectral estimation (window=0.25×T, overlap=50%, Hann taper) to compute squared coherence γ²(f) and residual spectrum, yielding MSE lower bound = Δ² + Σ Ŝ_e(f). O(N log N) computation. Reveals frequency-band-specific difficulty and predictability drift. SCP requires history-future pairs; Ω requires only history.

  Adaptive Ensemble Methods: (1) Error-based dynamic (w_i ∝ 1/MSE_i; reactive, simple), (2) Convex-optimized static (min ||y - w₀·linear - w₁·nonlinear||²; Hammam et al. achieve 13% MAPE, 80% improvement over ARIMA), (3) Neural combiner (learned weights; Adhikari 2015, Kourentzes 2014), (4) Regime-switching (discrete regimes; Xu et al. 2025), (5) Spectral-adaptive (novel: real-time Ω/SCP-driven weighting with logistic α(Ω) = 1/(1+exp(-a(Ω-b)))—first in-inference application, zero retraining).

  Benchmark Datasets: M4 (100k series, 6 frequencies/domains; heterogeneous spectral properties), PEMS (CA traffic, 5-min, multivariate; strong seasonality, weather/accident regime shifts), ETT (transformer temp/load, 15-min/1-hr, ~70k obs; controlled, ideal for staged validation).

  Model Architectures: Auto-ARIMA (grid (p,d,q)∈[0,2]³, AIC; 0.1-1s fit, 1ms forecast), LSTM (2×64 units, dropout=0.2, look-back=128; 5-30s train, 5ms inference), ResNet (2-3 blocks, 32-64 filters; 3-20s train, 3ms inference).

  Regime-Shift Detection: Ω drift metric ΔΩ = Ω_test - Ω_train_mean (largest gains when ΔΩ > 0.2); CUSUM on Ω samples flags deviations >1σ (Aminikhanghahi 2016; Ghezzi et al. 2025).

  Novelty: Spectral-adaptive is first real-time dynamic weighting application—distinct from Wang's pre-training selection and Feng's post-hoc diagnosis. No retraining or labeled regimes required. Projected <5% computational overhead. Open questions: optimal rolling Ω window size {50,100,128,256}; logistic α(Ω) optimality; multivariate extension; failure modes; parameter sensitivity.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_oxbmYex8-G2P/3_invention_loop/iter_1/gen_art/gen_art_research_1
out_expected_files:
- research_out.json

--- Item 2 ---
id: art_A4Sp9OGyoBQ9
type: dataset
title: Spectral-Adaptive Ensemble Time Series Dataset
summary: >-
  Successfully prepared spectral-adaptive ensemble time series dataset with 440 examples across 4 domains (transportation,
  energy, weather, finance) and 5 temporal frequencies (daily, hourly, 15-min, weekly, monthly). Dataset exhibits heterogeneous
  spectral properties (power ratio range 0.61-0.90), natural regime shifts (>0.2 spectral divergence between train/test),
  and series lengths 250-800 points. All examples standardized to exp_sel_data_out.json schema with comprehensive metadata
  including spectral statistics, train/test splits, and source provenance. Transportation domain dominates (260 examples,
  PEMS-like traffic) with energy/weather/finance balanced at 60 examples each. Validation: schema-compliant, no NaN values,
  file size 4.2MB (under 100MB limit), baseline forecast confirms data utility (MA(3) beats naive by 4.3%).
workspace_path: >-
  /ai-inventor/aii_data/runs/run_oxbmYex8-G2P/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 3 ---
id: art_hTphpd0tK14s
type: experiment
in_dependencies:
- id: art_A4Sp9OGyoBQ9
  label: dataset
title: Spectral-Adaptive Ensemble Validation
summary: >-
  Implements and validates spectral-predictability-driven online weighting for ARIMA+LSTM ensemble forecasting. Core hypothesis:
  spectral predictability Ω (concentration of power spectrum) correlates with optimal linear-vs-nonlinear blend weights α(Ω).
  Executed on 9 time series across 4 domains (energy, finance, transportation, weather) with full methodology: (1) Spectral
  Ω computation via rolling FFT; (2) ARIMA and LSTM baseline forecasters with proper train/test isolation; (3) Logistic weighting
  function α(Ω) tuned on held-out validation; (4) Test-time ensemble blending with 6 comparison methods; (5) Statistical rigor
  with 95% CIs and paired t-tests; (6) Regime-shift sensitivity analysis stratified by Ω quartiles; (7) Ablations on window
  size (32/64/128/256) and weighting forms (logistic/linear/power-law/neural). Results show spectral-adaptive ensemble achieves
  mean test MSE 50.08 vs fixed 0.5/0.5 baseline 168.76 (70% reduction), with paired t-test p=0.0012 (highly significant).
  Regime-shift analysis confirms largest improvements in high-Ω-shift quartiles (0% vs 75% in low-shift). Produces method_out.json
  with per-series metrics, aggregated statistics, and 2 diagnostic figures (MSE distribution, regime-shift scatter).
workspace_path: >-
  /ai-inventor/aii_data/runs/run_oxbmYex8-G2P/3_invention_loop/iter_2/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 4 ---
id: art_8fo8jCSnb_aM
type: evaluation
title: Spectral-Adaptive Ensemble Statistical Evaluation
summary: >-
  Comprehensive evaluation of spectral-predictability-driven ensemble weighting via 2000-resample bootstrap confidence intervals,
  paired t-tests with Bonferroni correction (α=0.01), Cohen's d and Hedge's g effect sizes, improvement proportion with Wilson
  score CI, stratification by spectral regime (3 strata: high ω>0.7, medium 0.4≤ω≤0.7, low ω<0.4), multivariate scope assessment,
  and computational profiling. Evaluated 7 methods (naive last-value, MA(3), ARIMA(1,0,0), LSTM-like, error-adaptive, spectral-adaptive,
  oracle optimal) on 50 synthetic AR(1) sequences (200-step training, 50-step test). Key findings: spectral-adaptive achieves
  MSE 0.2837 [0.2135, 0.3579], outperforms naive (0.4725) with 76% improvement proportion (CI [0.626, 0.857]), passes success
  criterion. Paired hypothesis tests show significant improvement vs. naive (p<0.0001, d=-0.494), LSTM (p<0.0001, d=-0.397),
  error-adaptive (p=0.0003, d=-0.136), but not vs. ARIMA or oracle. Stratified analysis shows strongest gains in medium-to-low
  spectral regimes where ensemble adaptation is most valuable. Computational overhead 2.1% of LSTM inference time (<5% target).
  All results schema-validated against exp_eval_sol_out.json. Outputs: eval.py script, full/mini/preview JSON files, execution
  logs.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_oxbmYex8-G2P/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json

--- Item 5 ---
id: art_am-gboEXSe7v
type: research
title: 'Spectral-Adaptive Ensemble: Validation, Positioning, Multivariate Feasibility'
summary: >-
  This research artifact synthesizes the theoretical and empirical foundations for spectral-adaptive ensemble forecasting.
  The core contribution is positioning spectral-adaptive as a proactive (leading-indicator) alternative to reactive error-based
  and discrete regime-switching ensemble methods. Key findings: (1) Spectral predictability (Omega), derived from spectral
  entropy, is well-grounded in signal processing and validated across 51 forecasting models and 28 datasets by Wang et al.
  (2025). Omega measures frequency-domain energy concentration (high = predictable, low = chaotic) and can be computed in
  O(N log N) time (seconds on commodity hardware) without model training. (2) Three competitive baselines exist: error-based
  dynamic weighting (BODE, Du 2022) is reactive but requires model inference; regime-switching (Elliott & Timmermann 2005)
  is theoretically principled but requires latent regime learning; static optimal weights are offline-only with no adaptation.
  Spectral-adaptive fills a gap: proactive guidance before model inference, no retraining, continuous weighting. (3) The monotone
  weighting assumption (higher Omega → higher linear weight) is NOT yet validated in literature—this is a critical empirical
  ablation. (4) Computational overhead is likely <5% (single FFT pass dominates time budget), not a blocker. (5) Multivariate
  extension is feasible via three paths: PCA-based Omega (simplest, loses dimensionality), per-channel Omega with learned
  aggregation (recommended, preserves heterogeneity), or Feng et al.'s SCP with band-specific weighting (most sophisticated,
  unimplemented). (6) Failure modes identified: spectral-adaptive degrades on high-noise sequences, low-Omega data, and highly
  non-stationary spectral structure. (7) Statistical rigor via paired t-tests, bootstrapped CIs on gains, and subgroup stratification
  (by Omega regime, dataset type, horizon) is essential for defensible claims. The novelty is NOT Omega itself (Wang 2025
  uses it for model selection) but the empirical discovery that Omega's predictive signal for model family selection can be
  applied at inference time for dynamic weighting—distinct from prior art.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_oxbmYex8-G2P/3_invention_loop/iter_2/gen_art/gen_art_research_1
out_expected_files:
- research_out.json
</all_artifacts>

<new_artifacts_this_iteration>
These 3 artifacts were created THIS iteration.

id: art_hTphpd0tK14s
type: experiment
in_dependencies:
- id: art_A4Sp9OGyoBQ9
  label: dataset
title: Spectral-Adaptive Ensemble Validation
summary: >-
  Implements and validates spectral-predictability-driven online weighting for ARIMA+LSTM ensemble forecasting. Core hypothesis:
  spectral predictability Ω (concentration of power spectrum) correlates with optimal linear-vs-nonlinear blend weights α(Ω).
  Executed on 9 time series across 4 domains (energy, finance, transportation, weather) with full methodology: (1) Spectral
  Ω computation via rolling FFT; (2) ARIMA and LSTM baseline forecasters with proper train/test isolation; (3) Logistic weighting
  function α(Ω) tuned on held-out validation; (4) Test-time ensemble blending with 6 comparison methods; (5) Statistical rigor
  with 95% CIs and paired t-tests; (6) Regime-shift sensitivity analysis stratified by Ω quartiles; (7) Ablations on window
  size (32/64/128/256) and weighting forms (logistic/linear/power-law/neural). Results show spectral-adaptive ensemble achieves
  mean test MSE 50.08 vs fixed 0.5/0.5 baseline 168.76 (70% reduction), with paired t-test p=0.0012 (highly significant).
  Regime-shift analysis confirms largest improvements in high-Ω-shift quartiles (0% vs 75% in low-shift). Produces method_out.json
  with per-series metrics, aggregated statistics, and 2 diagnostic figures (MSE distribution, regime-shift scatter).
workspace_path: >-
  /ai-inventor/aii_data/runs/run_oxbmYex8-G2P/3_invention_loop/iter_2/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

id: art_8fo8jCSnb_aM
type: evaluation
title: Spectral-Adaptive Ensemble Statistical Evaluation
summary: >-
  Comprehensive evaluation of spectral-predictability-driven ensemble weighting via 2000-resample bootstrap confidence intervals,
  paired t-tests with Bonferroni correction (α=0.01), Cohen's d and Hedge's g effect sizes, improvement proportion with Wilson
  score CI, stratification by spectral regime (3 strata: high ω>0.7, medium 0.4≤ω≤0.7, low ω<0.4), multivariate scope assessment,
  and computational profiling. Evaluated 7 methods (naive last-value, MA(3), ARIMA(1,0,0), LSTM-like, error-adaptive, spectral-adaptive,
  oracle optimal) on 50 synthetic AR(1) sequences (200-step training, 50-step test). Key findings: spectral-adaptive achieves
  MSE 0.2837 [0.2135, 0.3579], outperforms naive (0.4725) with 76% improvement proportion (CI [0.626, 0.857]), passes success
  criterion. Paired hypothesis tests show significant improvement vs. naive (p<0.0001, d=-0.494), LSTM (p<0.0001, d=-0.397),
  error-adaptive (p=0.0003, d=-0.136), but not vs. ARIMA or oracle. Stratified analysis shows strongest gains in medium-to-low
  spectral regimes where ensemble adaptation is most valuable. Computational overhead 2.1% of LSTM inference time (<5% target).
  All results schema-validated against exp_eval_sol_out.json. Outputs: eval.py script, full/mini/preview JSON files, execution
  logs.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_oxbmYex8-G2P/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json

id: art_am-gboEXSe7v
type: research
title: 'Spectral-Adaptive Ensemble: Validation, Positioning, Multivariate Feasibility'
summary: >-
  This research artifact synthesizes the theoretical and empirical foundations for spectral-adaptive ensemble forecasting.
  The core contribution is positioning spectral-adaptive as a proactive (leading-indicator) alternative to reactive error-based
  and discrete regime-switching ensemble methods. Key findings: (1) Spectral predictability (Omega), derived from spectral
  entropy, is well-grounded in signal processing and validated across 51 forecasting models and 28 datasets by Wang et al.
  (2025). Omega measures frequency-domain energy concentration (high = predictable, low = chaotic) and can be computed in
  O(N log N) time (seconds on commodity hardware) without model training. (2) Three competitive baselines exist: error-based
  dynamic weighting (BODE, Du 2022) is reactive but requires model inference; regime-switching (Elliott & Timmermann 2005)
  is theoretically principled but requires latent regime learning; static optimal weights are offline-only with no adaptation.
  Spectral-adaptive fills a gap: proactive guidance before model inference, no retraining, continuous weighting. (3) The monotone
  weighting assumption (higher Omega → higher linear weight) is NOT yet validated in literature—this is a critical empirical
  ablation. (4) Computational overhead is likely <5% (single FFT pass dominates time budget), not a blocker. (5) Multivariate
  extension is feasible via three paths: PCA-based Omega (simplest, loses dimensionality), per-channel Omega with learned
  aggregation (recommended, preserves heterogeneity), or Feng et al.'s SCP with band-specific weighting (most sophisticated,
  unimplemented). (6) Failure modes identified: spectral-adaptive degrades on high-noise sequences, low-Omega data, and highly
  non-stationary spectral structure. (7) Statistical rigor via paired t-tests, bootstrapped CIs on gains, and subgroup stratification
  (by Omega regime, dataset type, horizon) is essential for defensible claims. The novelty is NOT Omega itself (Wang 2025
  uses it for model selection) but the empirical discovery that Omega's predictive signal for model family selection can be
  applied at inference time for dynamic weighting—distinct from prior art.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_oxbmYex8-G2P/3_invention_loop/iter_2/gen_art/gen_art_research_1
out_expected_files:
- research_out.json
</new_artifacts_this_iteration>

<current_paper>
The paper draft from this iteration — represents the current state of the research story.

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
</current_paper>

<reviewer_feedback>
Feedback from the paper reviewer this iteration.

- [MAJOR] (scope) Univariate-only limitation severely restricts real-world applicability. Modern forecasting benchmarks and practical deployments are predominantly multivariate (PEMS: 307 traffic sensors, ETT: 6 energy/load channels, M4 has multivariate variants). The paper uses univariate AR(1) series with engineered Ω ∈ [0.2, 0.95], which do not capture multivariate correlation structure, cross-channel information flow, or spatial dependencies. Feng et al.'s SCP is multivariate-native but is not adopted here. The paper acknowledges multivariate as 'primary limitation' and proposes three extension paths (PCA, per-channel, SCP) but implements none. This leaves the core contribution unvalidated on realistic data.
  Action: Implement and validate at least one multivariate extension: (1) Recommend per-channel Ω aggregation—compute Ω independently per channel, learn aggregation weights w_c via validation-set MSE minimization, set Ω_agg = Σ w_c · Ω_c. (2) Test on ETT (6 channels, 1-year hourly data, highly correlated) or PEMS (307 sensors, 4-week 15-min data, spatial structure). (3) Report MSE/MAPE with 95% CIs and paired t-tests vs. ARIMA-only, fixed 0.5/0.5, and error-based on both univariate and multivariate versions. (4) Quantify channel heterogeneity: report distribution of learned w_c across channels. Show the method exploits per-channel differences, not just averaging them away. **Expected score impact: +1-2 points.** Multivariate validation would elevate this from narrow/specialist to broadly applicable.
- [MAJOR] (scope) Two-component ensemble limitation restricts generality. The method learns α(Ω) for binary weighting (ARIMA + LSTM). Extension to >2 components (e.g., ARIMA + LSTM + Prophet + Transformer + ExponentialSmoothing—common in practice) requires learning a weight vector α(Ω) over all pairs with simplex constraint (Σα = 1). This increases complexity (more hyperparameters, larger validation data requirement) and is not addressed. Real-world ensemble methods often combine 5-10 models; the paper's approach does not scale or validate on this.
  Action: (1) Extend to 3-component ensemble: ARIMA + LSTM + ExponentialSmoothing. (2) Learn α(Ω) = [α₁(Ω), α₂(Ω), α₃(Ω)] with α_i(Ω) = logistic(a_i(Ω - b_i)) for each i, constrained to simplex. (3) Tune on validation set (grid search over [a₁, b₁, a₂, b₂, a₃, b₃]). (4) Test on synthetic AR(1) and one realistic dataset. (5) Compare with oracle (offline simplex weights). Report MSE/variance vs. 2-component. **Expected score impact: +0.5-1 point.** Demonstrates scalability without requiring full K-component generalization.
- [MAJOR] (evidence) Evaluation limited to synthetic AR(1) sequences with engineered spectral properties. While rigorous (50 sequences, statistical tests, stratified analysis), the synthetic setting does not capture real-world complexity: multiple frequencies, non-stationary spectral structure, mode-switching, correlated noise, outliers, and missing values. The paper claims 'operationalizing spectral predictability' but only validates on data where Ω directly encodes the autoregressive coefficient (AR(1) processes where ρ ≈ Ω). Real time series have richer spectral structure. Transfer to M4 (100k series, 6 frequencies/domains, highly heterogeneous), PEMS (multivariate traffic with weather/accident shocks), ETT (non-stationary energy patterns) is unvalidated. This is the largest gap between claimed scope ('practical deployment') and actual scope ('controlled AR(1) synthetic data').
  Action: (1) Run on M4 univariate subset (random sample of 200-300 series using fixed random seed; stratify by frequency [daily/weekly/monthly/yearly] and domain [finance/econ/industry/other]). (2) Full protocol: train ARIMA + LSTM on first 60% of each series, tune α(Ω) on middle 10%, test on final 30%. (3) Report per-domain results (e.g., 'Financial series: 50 sequences, spectral-adaptive MSE 0.123, error-based 0.145, p = 0.02'). (4) Stratify by spectral regime (high Ω from training: >0.7, medium, low) and regime shift (ΔΩ = Ω_test - Ω_train; compare <0.1, 0.1-0.2, >0.2). (5) Report Cohen's d effect sizes and failure cases (where spectral-adaptive loses). (6) Compare time to forecast (does low computational overhead hold on multi-step forecasting?). **Expected score impact: +2-3 points.** Single realistic benchmark would materially strengthen evidence and credibility.
- [MAJOR] (novelty) Conceptual novelty is limited and positioned ambiguously. The paper claims 'first real-time dynamic reweighting application of Ω.' However, (1) Ω itself is from Wang et al. (2025)—not new. (2) Dynamic weighting is standard (BODE 2022, Elliott & Timmermann 2005, many others). (3) The contribution is combining Ω + dynamic weighting—a natural extension of Wang's work, not a conceptual leap. (4) Relative to error-based weighting (BODE), the main difference is using Ω instead of MSE_i(t-k:t) as the adaptive signal. This is incremental. (5) The paper does not articulate why spectral properties should outperform error accumulation theoretically—the advantage is empirical on synthetic AR(1) data (12% over BODE, p = 0.0003) but the mechanism is not explained. The paper would be stronger if it clarified: 'Spectral-adaptive wins when (a) regime shifts are gradual (Ω transitions smoothly) and (b) linear/nonlinear model performance is complementary (errors uncorrelated). It loses when (c) shifts are abrupt (step change in Ω) and (d) model errors are redundant.'
  Action: (1) Reframe novelty more precisely in abstract/intro: 'We propose spectral-adaptive weighting, which uses spectral predictability Ω as a proactive (leading-indicator) signal for dynamic ensemble weighting. Unlike reactive error-based weighting (which accumulates past forecast errors), spectral-adaptive predicts whether incoming data favors linear or nonlinear models WITHOUT waiting for forecasts to be generated. This enables faster response to gradual regime shifts and lower computational latency.' (2) Add theoretical justification: 'Spectral properties (frequency-domain energy concentration) change more slowly than forecast errors under gradual regime drift. We hypothesize spectral-adaptive responds faster to such shifts. (3) Design experiment: inject synthetic regime shift (gradual: Ω drift 0.5→0.7 over 20 steps, or abrupt: step change) and measure response lag (forecast steps until weighting adapts). Compare with error-based. Quantify advantage as 'spectral-adaptive adapts in 3±1 steps; error-based in 8±2 steps on gradual drift.' (4) Characterize failure modes: 'Spectral-adaptive degrades on abrupt shifts (error-based adapts faster) and high-noise sequences (Ω unreliable).' This honesty strengthens novelty positioning. **Expected score impact: +0.5-1 point.** Better positioning clarifies the actual novelty and removes vague claims.
- [MINOR] (methodology) Hyperparameter tuning details, while explicit (grid search bounds a ∈ [0.1, 50], b ∈ [0.1, 0.9], granularity 0.1), are not justified. Why these bounds? Are they domain-specific or universal? The paper recommends T_w=128 based on ablation results shown in the Ablation Studies section, but the choice appears arbitrary—why 128 and not 100 or 150? The ablation table shows T_w=128 achieves lowest MSE with lowest variance, but the improvement over T_w=100 is marginal (0.3%). For practitioners, a principled approach to selecting T_w based on data properties (e.g., autocorrelation decay, spectral clustering) would be more useful than 'T_w=128 is recommended'.
  Action: (1) Justify grid search bounds: 'Steepness parameter a controls transition sharpness; bounds [0.1, 50] span sharp (<1-unit transition) to smooth (>10-unit transition). Inflection point b ∈ [0.1, 0.9] covers the full Ω range; we exclude boundary values [0, 1] to avoid degenerate solutions.' (2) For T_w selection, propose a data-driven heuristic: 'Compute autocorrelation function (ACF) of y_t; find lag k where ACF drops below 0.3 (weak dependence threshold). Set T_w = 2k to capture ~2 decorrelation cycles.' Validate this on datasets and compare with fixed T_w=128. (3) Provide sensitivity analysis: run full pipeline with T_w ∈ {64, 100, 128, 150, 200} on M4 subset; plot MSE vs. T_w and show variance. Identify if 128 is optimal for all domains or if there is domain-specific variation. **Expected score impact: +0.3-0.5 point.** Methodological justification improves confidence in recommendations.
- [MINOR] (evidence) Computational overhead is measured on CPU (~2.1% of LSTM inference) but hardware diversity is not explored. The paper reports 'FFT ~2.5ms, weighting ~0.8ms, total ~4.5ms, LSTM ~210ms, overhead 2.1%' on CPU. However, LSTM inference time varies dramatically by hardware: GPU (A100) ~5ms, older GPU (RTX3090) ~15ms, CPU (Intel Xeon) ~200ms, edge devices (ARM) ~500ms+. The relative overhead scales with hardware; on fast GPUs, spectral overhead becomes proportionally larger (4.5ms / 5ms = 90% overhead on A100 vs. 2% on CPU). The paper should clarify this trade-off.
  Action: (1) Benchmark on three hardware targets: (a) CPU (Intel Xeon or similar multi-core); (b) GPU (NVIDIA A100 or RTX3090); (c) mobile/edge if relevant (ARM CPU or TPU). (2) For each, measure wall-clock time for LSTM inference and Ω+weighting separately. Use torch.profiler or equivalent. (3) Report overhead % for each hardware. (4) Discuss implications: 'On A100 GPU where LSTM runs in 5ms, spectral overhead of 4.5ms is substantial (90%). On CPU (200ms LSTM), overhead is negligible (2%). Practitioners should profile on their target hardware.' (5) Propose optimization if overhead is high on GPU: 'FFT could be batched (compute Ω for multiple sequences simultaneously) or fused with LSTM via custom CUDA kernel to amortize overhead.' **Expected score impact: +0.2-0.3 point.** Hardware-aware analysis prevents false claims of 'negligible overhead' on all platforms.
- [MINOR] (clarity) Figures are specified as placeholders [FIGURE:fig_results_comparison] and [FIGURE:fig_regime_stratified] but not generated. These are central to evaluating the paper—readers cannot visually assess MSE comparisons or stratification patterns without seeing the plots. The paper's claims (e.g., '51% improvement in medium-Ω regime') are quantitative but lack visual support. Additionally, figure specifications in the paper are vague (e.g., 'Box plot or bar chart' for fig_results_comparison). What should the plot show? Error bars as CI? Individual sequences or aggregate? Panel layout?
  Action: (1) Generate Fig 1 (Results Comparison): Bar chart with baseline methods (naive, MA3, ARIMA, LSTM, error-adaptive, spectral-adaptive, oracle) on x-axis, MSE on y-axis. Include 95% CI error bars. Add text annotations with effect sizes (Cohen's d vs. spectral-adaptive). Use color coding (spectral-adaptive=blue, baselines=gray). (2) Generate Fig 2 (Regime Stratification): Panel A: Box plots of MSE for spectral-adaptive, error-adaptive, ARIMA-only stratified by Ω regime (high, medium, low). Panel B: Scatter plot of improvement% (y) vs. ΔΩ train→test (x), colored by Ω regime, with trend line. (3) In Methods, add figure specifications: 'Figure 1 shows MSE (mean and 95% CI) for each method on the full test set of 50 sequences. Figure 2 reveals that largest gains occur in medium-Ω regimes (panel A); gains correlate with spectral regime shift magnitude (panel B).' **Expected score impact: +0.5 point.** Visual confirmation of quantitative claims strengthens clarity and credibility.
- [MINOR] (clarity) Related work comparison lacks a structured summary table. The paper cites 15 papers covering spectral metrics, ensemble methods, and baselines but does not provide a direct comparison of how spectral-adaptive differs from error-based (BODE), regime-switching (Elliott & Timmermann), and static optimal methods. Readers must infer differences from scattered text references (e.g., 'error-based is reactive' in intro vs. 'regime-switching assumes discrete regimes' in related work).
  Action: Add a comparison table in Related Work section (before or after the detailed baseline descriptions). Suggested format:

| Method | Proactive | Retrains | Input | Multivariate | Computational Cost |
|--------|-----------|----------|-------|--------------|-------------------|
| Error-based (BODE) | No | No | Recent errors | Yes | ~0ms |
| Regime-switching (E&T) | Partial | Yes | Regime state | Yes | ~10ms |
| Static optimal (Adhikari) | No | Yes (offline) | Train MSE | Yes | 0 (test) |
| Spectral-adaptive (this work) | Yes | No | Rolling Ω | No (univariate) | <5% |

Add footer: 'Spectral-adaptive is unique in using spectral predictability (pre-forecast signal) for proactive weighting without retraining. Trade-off: univariate-only (multivariate extension deferred).' **Expected score impact: +0.3 point.** Clarity and positioning of contribution improve.
- [MINOR] (rigor) Ablation on weighting function forms is incomplete. The paper compares logistic vs. linear vs. power-law vs. step function (Methods section) and reports results in Ablations (e.g., 'Logistic MSE=0.284, Linear MSE=0.290, Power-law MSE=0.292, Step MSE=0.316'). However, the ablation does not test whether these functions are significantly different—no statistical tests (paired t-tests, confidence intervals) are reported. The differences are small (logistic vs. linear: 2.4% MSE difference, d=-0.036 estimated). Are these practically significant or noise? The paper should report p-values and effect sizes for each comparison.
  Action: (1) For each weighting function comparison, run paired t-test on the 50 sequences: t-stat, p-value, 95% CI on MSE difference, Cohen's d. (2) Use Bonferroni correction (4 functions → 6 pairwise comparisons, α'=0.0083). (3) Report in a table: | Comparison | MSE diff | 95% CI | t-stat | p-value | d | Reject | Logistic vs. Linear | 0.006 | [−0.005, 0.017] | 0.42 | 0.68 | −0.036 | No | ... | (4) Interpret: 'Logistic and linear weighting are not significantly different (p = 0.68). Logistic is recommended as default for its smooth transition and interpretability (inflection point b ≈ Ω_median), but practitioners may substitute linear weighting without loss of performance.' This honesty is stronger than claiming logistic is 'optimal.' **Expected score impact: +0.2-0.3 point.** Statistical rigor on ablations increases confidence.
- [MINOR] (methodology) Failure mode characterization is mentioned (Discussion section) but not empirically validated. The paper lists three failure modes: (1) both ARIMA and LSTM poor for task, (2) Ω uncorrelated with actual accuracy, (3) regime shifts too rapid for rolling Ω to track. These are plausible but unquantified. The paper should identify actual failure cases in the 50-sequence evaluation and explain them.
  Action: (1) Retrospective failure analysis on the 50 test sequences: (a) identify sequences where spectral-adaptive underperforms error-based (e.g., improvement < 0% or spectral MSE > error-adaptive MSE), (b) for each, compute: Ω stability (std of rolling Ω), error correlation corr(error_arima, error_lstm), sequence noise (SNR), and sequence length. (c) Create a failure-mode profile: '2 sequences had high error correlation (>0.7); spectral-adaptive MSE 0.41 vs. error-adaptive 0.35 (−17% performance). These are the model-redundancy failure mode.' (2) Report as table: Sequence | Failure Mode | Reason | MSE Spectral | MSE Error-Adaptive | ... (3) Quantify: 'Out of 50 sequences, 4 (8%) are failure-mode sequences (high error correlation or low Ω stability). On these, spectral-adaptive loses to error-based by avg 5-15%.' (4) Propose mitigation: 'Practitioners could pre-screen data for corr(error_linear, error_nonlinear) and fall back to error-based weighting if >0.7.' **Expected score impact: +0.3-0.5 point.** Empirical characterization of failure modes strengthens methodology and provides actionable insights.
</reviewer_feedback>



<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for the field's landscape, prior work, crowded lanes, and the novelty bar — consult it while revising so the updated hypothesis stays genuinely novel and well-positioned.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>

<task>
IMPORTANT: Your ONLY output is the revised hypothesis text. Do NOT run code, produce artifacts,
fix bugs, or attempt to address the evidence yourself — the next iteration of the invention loop
will generate fresh artifacts based on your revised hypothesis. Reflect and rewrite; nothing else.

Do NOT generate a completely new hypothesis. Take the current hypothesis and REVISE it
to incorporate new evidence. Keep the core idea — refine, narrow, or strengthen it.

1. Does the evidence support the hypothesis? Narrow or broaden scope as needed.
2. Which claims now have strong evidence? Which are still unsupported?
3. Should the hypothesis become more specific based on what we've learned?
4. If reviewer feedback is provided, address the critiques directly.

STABILITY IS OK: If progress is good and evidence supports the current direction, keep the
hypothesis similar or identical. Only make substantive changes when evidence clearly calls for
them — e.g., contradictory results, fundamental reviewer critiques, or findings that refine scope.

You must also classify two kinds of edges in the research trace:

(A) The H↔H edge — how does this revised hypothesis relate to the previous one?
    Set `relation_type` (Moulines's structuralist typology) to one of:
    - "evolution": refining specialised claims, same conceptual frame
    - "embedding": previous hypothesis is now a special case of a broader frame
    - "replacement": rejecting the previous frame entirely (Kuhnian shift)
    Set `relation_rationale` to a brief justification (≤120 chars).

(B) The A↔A edges — for each artifact created THIS iteration, classify each of its
    `in_dependencies` (predecessor → dependent) using MultiCite's citation-function
    typology (Lauscher et al., NAACL 2022) — emit one entry in `artifact_relations`
    per (predecessor, dependent) pair. Predecessors are ALWAYS artifacts from EARLIER
    iterations — artifacts within one iteration run in parallel and cannot depend on
    each other, so never emit a relation between two same-iteration artifacts (it
    will be dropped):
    - "background": predecessor is treated as background context
    - "motivation": predecessor motivated this artifact's research
    - "uses": this artifact uses the predecessor's data, method, or output
    - "extends": this artifact extends the predecessor
    - "similarities": this artifact's results agree with the predecessor's
    - "differences": this artifact's results disagree with the predecessor's
    Each `relation_rationale` must be ≤120 characters.

Output the COMPLETE revised hypothesis (with the H↔H relation fields) AND the full
list of A↔A `artifact_relations` for this iteration's new artifacts.
</task><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_oxbmYex8-G2P/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ArtifactRelation": {
      "description": "One typed A\u2194A edge between a dependent artifact and one of its in_dependencies.\n\nMultiCite citation-function typology (Lauscher et al., NAACL 2022),\nreduced to 6 plain-English types.",
      "properties": {
        "from_id": {
          "description": "ID of the predecessor artifact (the one being depended on)",
          "title": "From Id",
          "type": "string"
        },
        "to_id": {
          "description": "ID of the dependent artifact (the new artifact this iteration)",
          "title": "To Id",
          "type": "string"
        },
        "relation_type": {
          "description": "MultiCite citation-function type for the predecessor\u2192dependent edge: 'background' \u2014 predecessor is treated as background context; 'motivation' \u2014 predecessor motivated this artifact's research; 'uses' \u2014 this artifact uses the predecessor's data, method, or output; 'extends' \u2014 this artifact extends the predecessor; 'similarities' \u2014 this artifact's results agree with the predecessor's; 'differences' \u2014 this artifact's results disagree with the predecessor's.",
          "enum": [
            "background",
            "motivation",
            "uses",
            "extends",
            "similarities",
            "differences"
          ],
          "title": "Relation Type",
          "type": "string"
        },
        "relation_rationale": {
          "description": "Brief rationale for this relation type (one short line, max 120 characters).",
          "maxLength": 120,
          "title": "Relation Rationale",
          "type": "string"
        }
      },
      "required": [
        "from_id",
        "to_id",
        "relation_type",
        "relation_rationale"
      ],
      "title": "ArtifactRelation",
      "type": "object"
    }
  },
  "description": "Revised hypothesis after reviewing iteration results.\n\nOutput matches the hypothesis dict structure so it can replace the\noriginal hypothesis in subsequent iterations.",
  "properties": {
    "title": {
      "description": "Revised hypothesis title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters); may be unchanged if still accurate.",
      "title": "Title",
      "type": "string"
    },
    "hypothesis": {
      "description": "Revised hypothesis statement \u2014 what we now believe based on evidence",
      "title": "Hypothesis",
      "type": "string"
    },
    "relation_rationale": {
      "description": "Brief rationale for the H\u2194H revision type (one short line, max 120 characters).",
      "maxLength": 120,
      "title": "Relation Rationale",
      "type": "string"
    },
    "confidence_delta": {
      "description": "How confidence changed: 'increased', 'decreased', or 'unchanged'",
      "title": "Confidence Delta",
      "type": "string"
    },
    "key_changes": {
      "description": "Bullet list of specific changes made to the hypothesis",
      "items": {
        "type": "string"
      },
      "title": "Key Changes",
      "type": "array"
    },
    "relation_type": {
      "description": "Moulines's structuralist typology of this hypothesis revision: 'evolution' \u2014 refining specialised claims while keeping the same conceptual frame; 'embedding' \u2014 the previous hypothesis is now a special case of a broader frame; 'replacement' \u2014 rejecting the previous frame entirely (incommensurable, Kuhnian revolution).",
      "enum": [
        "evolution",
        "embedding",
        "replacement"
      ],
      "title": "Relation Type",
      "type": "string"
    },
    "artifact_relations": {
      "description": "Typed A\u2194A edges for this iteration's new artifacts. Emit one entry per (predecessor \u2192 dependent) edge for every in_dependency on each artifact produced this iteration.",
      "items": {
        "$ref": "#/$defs/ArtifactRelation"
      },
      "title": "Artifact Relations",
      "type": "array"
    }
  },
  "required": [
    "title",
    "hypothesis",
    "relation_rationale",
    "confidence_delta",
    "key_changes",
    "relation_type"
  ],
  "title": "RevisedHypothesis",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `./.terminal_claude_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-07-30 13:35:20 UTC

```
Test whether a 3-point moving average beats a naive last-value forecast on a short synthetic series. Keep the investigation minimal.
```

### [3] SYSTEM-USER prompt · 2026-07-30 13:36:45 UTC

```
<validation-feedback>
Attempt 1 failed validation.

The output file `.terminal_claude_agent_struct_out.json` does not exist yet. Produce it as JSON matching the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```

### [4] SYSTEM-USER prompt · 2026-07-30 13:37:25 UTC

```
<validation-feedback>
Attempt 2 failed validation.

Schema validation found 3 problems — fix ALL of them at once:
  - at `artifact_relations.0.relation_rationale`: 'Experiment uses dataset artifact (440 examples across 4 domains) for baseline comparison; actual experiments run on 50 synthetic AR(1) sequences separately.' is too long (at most 120 characters, got 156)
  - at `artifact_relations.1.relation_rationale`: 'Research artifact extends iter1 theoretical foundations (spectral metrics, adaptive ensemble methods) with empirical validation of monotone weighting and multivariate feasibility analysis.' is too long (at most 120 characters, got 188)
  - at `relation_rationale`: 'Mechanism confirmed on synthetic, real-world applicability constrained by univariate limitation. Reframing honest about validated scope and critical blockers.' is too long (at most 120 characters, got 158)
Every required field must be present and every field type must match the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```
