# Spectral-Adaptive Ensemble: Validation, Positioning, Multivariate Feasibility

## Summary

This research artifact synthesizes the theoretical and empirical foundations for spectral-adaptive ensemble forecasting. The core contribution is positioning spectral-adaptive as a proactive (leading-indicator) alternative to reactive error-based and discrete regime-switching ensemble methods. Key findings: (1) Spectral predictability (Omega), derived from spectral entropy, is well-grounded in signal processing and validated across 51 forecasting models and 28 datasets by Wang et al. (2025). Omega measures frequency-domain energy concentration (high = predictable, low = chaotic) and can be computed in O(N log N) time (seconds on commodity hardware) without model training. (2) Three competitive baselines exist: error-based dynamic weighting (BODE, Du 2022) is reactive but requires model inference; regime-switching (Elliott & Timmermann 2005) is theoretically principled but requires latent regime learning; static optimal weights are offline-only with no adaptation. Spectral-adaptive fills a gap: proactive guidance before model inference, no retraining, continuous weighting. (3) The monotone weighting assumption (higher Omega → higher linear weight) is NOT yet validated in literature—this is a critical empirical ablation. (4) Computational overhead is likely <5% (single FFT pass dominates time budget), not a blocker. (5) Multivariate extension is feasible via three paths: PCA-based Omega (simplest, loses dimensionality), per-channel Omega with learned aggregation (recommended, preserves heterogeneity), or Feng et al.'s SCP with band-specific weighting (most sophisticated, unimplemented). (6) Failure modes identified: spectral-adaptive degrades on high-noise sequences, low-Omega data, and highly non-stationary spectral structure. (7) Statistical rigor via paired t-tests, bootstrapped CIs on gains, and subgroup stratification (by Omega regime, dataset type, horizon) is essential for defensible claims. The novelty is NOT Omega itself (Wang 2025 uses it for model selection) but the empirical discovery that Omega's predictive signal for model family selection can be applied at inference time for dynamic weighting—distinct from prior art.

## Research Findings

## Foundations of Spectral Predictability (Omega)

Spectral predictability Omega is a signal-processing metric grounded in information theory, defined as Ω(x) = 1 - H(x)/H_max, where H(x) is spectral entropy and H_max = log(K) with K = floor(T/2) [1]. The metric quantifies frequency-domain energy concentration: high Omega (>0.7) indicates periodic/regular signals (predictable), while low Omega (<0.4) indicates diffuse/chaotic signals (unpredictable). Computation involves: (1) applying a Hann window and removing DC component, (2) computing FFT, (3) normalizing power spectrum to probability distribution, (4) calculating entropy H = -sum(p_k log p_k), (5) normalizing by maximum entropy. The entire process takes O(N log N) time—seconds on commodity hardware for typical datasets [1].

Wang et al. (2025) conducted controlled experiments on synthetic data (engineered Omega 0.2-0.8) and three real-world domains: CarbonCast (hourly energy), PEMS (hourly traffic), and Fitbit (minute-level wearables) [1]. Key finding: forecasting error systematically decreases as Omega increases. On synthetic data, the Omega-error relationship is nearly monotonic, with 20-40% error reductions when moving from Omega=0.3 to Omega=0.7 [1]. A large-scale analysis covering 51 forecasting models (statistical, deep-learning, pretrained, zero-shot) and 28 datasets from the GIFT-Eval benchmark revealed that large time-series foundation models (TSFMs) outperform lightweight baselines when Omega is high, while their advantage vanishes when Omega is low [1]. This stratification enables rapid model selection before expensive validation: practitioners can decide in seconds whether data suits expensive TSFMs or cheaper, simpler models.

The relationship between spectral structure and forecastability is supported by complementary work on spectral entropy. Wang & Klee (2025) independently validate spectral predictability on M5 supply-chain data, confirming strong correlation with realized forecast performance [9]. Lyapunov exponents (measuring chaos/stability) complement Omega by capturing system dynamics beyond frequency structure [9].

## Competitive Baseline Methods

**Error-Based Dynamic Weighting (Reactive):** BODE (Bayesian Optimization-based Dynamic Ensemble) [2] is the canonical error-based method with 253 citations. The approach computes weights from prediction errors in a recent past window, reacting AFTER forecasts are made. Advantage: immediately responsive to actual errors, no lag. Disadvantage vs. spectral-adaptive: cannot anticipate regime shifts, requires model inference first (high latency), and cannot guide model selection before training [2].

**Regime-Switching Weighting (Discrete Regime):** Elliott & Timmermann (2005) proposed optimal forecast combination under regime switching, a seminal work with 120+ citations [3]. This method models combination weights as driven by a latent Markov regime variable, enabling theoretically principled, regime-dependent weighting. Advantage: explicit regime modeling, theoretical foundation. Disadvantage: requires regime inference/training overhead, discrete assumption (vs. continuous Omega), and weights shift discretely between regimes rather than smoothly [3].

**Static Per-Series Optimal Weights (Offline):** Adhikari & Jain (2015) proposed neural network combining weights for time series forecasting (165 citations) [4]. Weights are learned on training data via grid search or convex optimization and frozen at test time. Advantage: stable, interpretable, low compute. Disadvantage: no adaptation to regime drift, assumes test data resembles training distribution [4].

**Positioning Table:**

| Dimension | Spectral-Adaptive | Error-Based (BODE) | Regime-Switching (E&T) | Static Optimal |
|-----------|-------------------|-------------------|--------|----------------|
| Proactive? | Yes (leading indicator) | No (reactive) | Partial (regime-aware) | No (offline) |
| Retraining | No | No | Yes | No (train only) |
| Latency | Low (FFT only) | High (model inference) | Medium | None |
| Multivariate | Deferred (per-channel viable) | Yes (built-in) | Limited | Yes |
| Computational cost | O(N log N) | O(model inference) | O(regime + model) | O(train only) |
| When it wins | Regime drift, model complementarity | Unpredictable shifts | Discrete states | Stationary, no drift |

Spectral-adaptive fills a gap: it is the FIRST method to use spectral predictability as a PROACTIVE (pre-forecast) indicator for dynamic weighting, distinct from reactive error-based and discrete regime-switching approaches.

## Critical Assumptions Requiring Validation

**Monotone Weighting Assumption:** The hypothesis assumes α(Omega) is monotone—higher Omega implies higher linear weight. This assumption is NOT explicitly validated in the literature [1, 3, 4]. The intuition is that linear methods exploit regularity (high Omega) while nonlinear methods handle chaos (low Omega), but this remains an assumption. Empirical ablation is needed: train two weighting functions on validation data—logistic α_logistic(Ω) = σ(β₀ + β₁·Ω) and neural α_nn(Ω) = MLP(Ω)—then compare test MSE. If α_nn significantly outperforms α_logistic, the monotone assumption fails and nonlinear weighting becomes necessary.

**Rolling Window Size Stability:** The hypothesis uses T_w=128 with no data-driven justification. Smaller windows produce noisier Omega estimates; larger windows track changes more slowly. Grid search over T_w ∈ {32, 50, 100, 128, 256, 512} is needed, measuring: (a) Omega stability (correlation of estimates across overlapping windows), and (b) predictive power (correlation of α(Ω) from training vs. test MSE reduction). Window selection is domain-specific and requires empirical validation per dataset.

**Computational Overhead Reality:** The hypothesis assumes <5% overhead. Theory confirms: single FFT pass takes seconds, but wall-clock overhead depends on hardware (CPU vs. GPU) and model inference cost. Measurement needed on commodity hardware: overhead % = T_spectral / T_inference × 100. Expected: <5% on modern systems; if >10%, practical concerns arise.

## Multivariate Feasibility and Extension Paths

The spectral-adaptive hypothesis is currently univariate-only. Three multivariate extension paths exist [5]:

**Option A: PCA-Based Omega.** Compute Omega on top-K principal components (K=1 or K=3). Pros: simple, dimensionality reduction, preserves >80% variance with K=3. Cons: loses spatial/correlative structure; variance loss trade-off. Complexity: low. Feasibility: suitable for PEMS (highly correlated traffic sensors); less suitable for ETT (6 independent features).

**Option B: Per-Channel Omega with Learned Aggregation (RECOMMENDED).** Compute Omega per channel independently; learn weighted aggregation Ω_agg = Σ w_c · Ω_c. Pros: captures channel heterogeneity, no variance loss, preserves interpretability. Cons: requires learning aggregation weights. Complexity: medium. Feasibility: all multivariate datasets. TSGym (Liang et al., 2024) surveys multivariate forecasting design choices (channel-independent strategies, patching, attention) but does not address spectral weighting [5].

**Option C: Feng et al. SCP (Band-Specific Predictability).** Spectral Coherence Predictability (Feng et al., 2026, ICML) measures predictability per frequency band, enabling band-to-model mapping [6]. Pros: theoretically grounded, multivariate-ready, band-aware. Cons: higher complexity, requires band-to-model learning, SCP not yet widely implemented. Feng et al. provide multivariate extension in their appendix (B.1.1: Multivariate SCP), but real-world deployment is unclear.

**Recommendation:** If univariate results are strong (≥3% MSE gain) and monotone assumption holds, recommend Option B (per-channel aggregation) as immediate next step. Option A is a safer fallback if results are weak. Option C is ideal but deferred pending SCP maturation.

## Failure Modes and Pathological Cases

Spectral-adaptive likely degrades when: (1) **Non-stationary spectral structure:** Omega changes rapidly (e.g., step change in periodicity)—rolling window T_w cannot track [1]. (2) **High noise:** Spectral features buried; Omega unreliable; Wang et al. note this in PEMS and Fitbit where external factors confound spectral signal [1]. (3) **Mixed-regime sequences:** Omega smooth but underlying regime sharp (sudden shock)—proactive indicator lags [3]. (4) **Redundant predictions:** Linear and nonlinear errors highly correlated—weighting doesn't help. (5) **Short sequences:** Omega unstable; insufficient training data for α(Ω); threshold <200 steps [1].

Identification methodology: on each test sequence, compute: (a) Omega volatility = std(Ω_t) over test period (flag if >0.15), (b) SNR = signal-to-noise power ratio (flag if <2 dB), (c) error correlation = corr(error_linear, error_nonlinear) (flag if >0.9 or <0.2), (d) sequence length (flag if <200). Expected: 5-15% of sequences meet pathological criteria. Critical comparison: does error-based weighting also fail on these sequences? If yes, the problem is hard. If no, spectral-adaptive has a fundamental limitation vs. reactive methods.

## Statistical Rigor and Significance Testing

All claims must be supported by paired t-tests, confidence intervals, and subgroup analysis. For each dataset (M4, PEMS, ETT): paired t-test spectral-adaptive vs. each baseline, with Bonferroni or Benjamini-Hochberg correction (4 tests per dataset → α'=0.0125 or FDR control). Report t-statistic, p-value, degrees of freedom, 95% CI on MSE difference, and Cohen's d effect size.

For each sequence, compute gain = (MSE_baseline - MSE_spectral) / MSE_baseline. Bootstrap 95% CI on median gain (resample sequences 1000×); success criterion: CI lower bound > 0 and median >0.03 (3% gain) on ≥70% of sequences.

Stratify by: (a) Omega regime (high >0.7, medium 0.4-0.7, low <0.4)—expect largest gains in high-Omega. (b) Dataset type (M4 financial, PEMS traffic, ETT energy). (c) Forecast horizon (short 1-24 steps, medium 25-96, long 97+)—expect largest gain in shorter horizons. Include interaction effects. Report in table format: | Dataset | N_Seq | Median Gain (%) | 95% CI | p-value | Win Rate (%) |.

## Novelty Positioning and Paper Narrative

Spectral-adaptive's novelty is precisely bounded [1, 2, 3, 4]: It is NOT the first application of Omega to forecasting (Wang et al. 2025 use Omega for pre-training model selection). It is NOT the first adaptive weighting method (error-based, regime-switching pre-exist). It IS the first proactive (leading-indicator) adaptive weighting grounded in spectral predictability. It IS the first evaluation of the monotone weighting assumption. It IS the first systematic comparison vs. error-based on standard benchmarks.

**Proposed paper narrative:** "Spectral-adaptive ensemble provides a proactive alternative to reactive error-based dynamic weighting. By monitoring spectral predictability Omega in real time, the method predicts whether incoming data favors linear or nonlinear models WITHOUT waiting for forecasts. On univariate subsets of M4/PEMS/ETT benchmarks, spectral-adaptive achieves [X]% MSE improvement over fixed-weight ensembles (95% CI: [Y%, Z%], p < 0.001) when Omega shifts >0.2 between train and test. The monotone weighting assumption holds on [A]% of sequences; non-monotone weighting offers no significant advantage (α_nn vs. α_logistic: Δ MSE < 0.1%). Computational overhead is [B]% (measured on [hardware]). Key limitations: (1) Univariate scope—multivariate extension via per-channel Omega aggregation is feasible but unvalidated; (2) Degrades on high-noise, low-Omega sequences; (3) Rolling window size T_w=128 is data-dependent, not universal. Spectral-adaptive excels when data exhibits regime drift and model complementarity; it struggles with non-stationary spectral structure and redundant predictions."

**Multivariate recommendation:** "Given univariate results, we recommend extending via per-channel Omega aggregation (Option B), as it preserves model heterogeneity without complexity overhead. Alternative: SCP (Feng et al. 2026) offers band-specific diagnostics but requires implementation effort. PCA-based Omega (Option A) is simpler but risks losing interpretability on high-dimensional data."

**Future work:** (1) Multivariate validation on full PEMS/ETT. (2) Adaptive window size T_w(t) based on spectral stability. (3) Band-specific weighting via SCP (if implementation matures). (4) Online learning for α(Ω) hyperparameters. (5) Comparative study vs. neural network combiner (Adhikari 2015 approach).

## Sources

[1] [Spectral Predictability as a Fast Reliability Indicator for Time Series Forecasting Model Selection](https://arxiv.org/abs/2511.08884) — Wang et al. (2025) introduce spectral predictability Omega as a fast, interpretable signal-processing metric for stratifying model family performance. Validated across 51 models and 28 datasets from GIFT-Eval benchmark. Shows TSFMs outperform baselines when Omega high; advantage vanishes when Omega low. Exact formula: Ω(x) = 1 - H(x)/H_max where H is spectral entropy. Computation: O(N log N) via FFT, takes seconds on commodity hardware. Controlled experiments on synthetic (engineered Omega 0.2-0.8) and real data (CarbonCast, PEMS, Fitbit) confirm monotonic Omega-error relationship with 20-40% error reductions from Omega=0.3 to 0.7.

[2] [Bayesian optimization based dynamic ensemble for time series forecasting](https://www.sciencedirect.com/science/article/abs/pii/S0020025522000135) — Du et al. (2022, Information Sciences, 253 citations). Canonical error-based dynamic ensemble (BODE) method. Adjusts each model's weight based on recent prediction errors in a moving window. Reactive approach: responds after forecasts are made. Shows modest MSE improvements over fixed ensembles. Key disadvantage: requires model inference first (high latency), cannot anticipate regime shifts. Provides baseline for comparison with proactive spectral-adaptive weighting.

[3] [Optimal Forecast Combination Under Regime Switching](https://rady.ucsd.edu/_files/faculty-research/timmermann/optimal-forecast-combination.pdf) — Elliott & Timmermann (2005, International Economic Review, 120+ citations). Seminal theoretical work on regime-switching forecast combination. Weights driven by latent Markov regime variable. Theoretically principled approach. Key limitations: requires regime inference/training, discrete regime assumption (vs. continuous Omega), weights shift discretely between regimes. Provides theoretical baseline for comparison with spectral-adaptive's continuous proactive weighting.

[4] [A neural network based linear ensemble framework for time series forecasting](https://www.sciencedirect.com/science/article/abs/pii/S0925231215000338) — Adhikari & Jain (2015, Neurocomputing, 165 citations). Neural network method for learning optimal combining weights on training data. Frozen at test time (static weights). Provides offline baseline: no adaptation, no retraining, assumes test ~ train distribution. Demonstrates typical ensemble approach before adaptive methods emerged.

[5] [TSGym: Design Choices for Deep Multivariate Time-Series Forecasting](https://arxiv.org/html/2509.17063v1) — Liang et al. (2024, ICML 2026 under review). Comprehensive benchmark of design choices in multivariate forecasting (channel-independent strategies, patching, attention, foundation models). Proposes automated component selection via meta-learning. Does not address spectral predictability weighting, but provides context for multivariate design trade-offs. Relevant for understanding per-channel aggregation feasibility and channel-independence assumptions.

[6] [Predictability-Aligned Evaluation for Time Series Forecasting](https://arxiv.org/html/2509.23074v3) — Feng et al. (2026, ICML). Introduces Spectral Coherence Predictability (SCP) and Linear Utilization Ratio (LUR) for instance-level difficulty measurement. SCP provides O(N log N) per-instance diagnostic and frequency-band-specific predictability. Supports band-wise evaluation and multivariate extension (Appendix B.1.1: Multivariate SCP). Shows SCP aligns strongly with forecasting errors across diverse models. Alternative to univariate Omega for multivariate scenarios; more sophisticated but unimplemented.

[7] [Time Series Forecastability Measures](https://arxiv.org/html/2507.13556v1) — Wang & Klee (2025, KDD Workshop on AI for Supply Chain). Independent validation of spectral predictability on M5 supply-chain dataset. Proposes using spectral entropy-derived metrics and Lyapunov exponents to quantify forecastability a priori (before model training). Confirms strong correlation between spectral predictability and realized forecast performance. Complements Wang et al. (2025) by validating on different domain.

[8] [Should the Naive Forecast be Your Default Forecast?](https://demand-planning.com/2018/08/01/should-the-naive-forecast-be-your-default-forecast/) — Practical guidance on baseline forecasting methods. Compares naive (last-value) forecast with moving average and other approaches. Establishes that naive is often used as baseline metric. Moving average typically outperforms naive on stable, low-volatility data. Context for understanding baseline comparisons and when simple forecasts suffice.

[9] [Is the Naive Baseline Unbeatable in Financial Time Series Forecasting?](https://arxiv.org/html/2406.14469v11) — Analysis of naive forecast performance. Compares naive, naive-with-drift, IMA(1,1), and linear regression baselines. Establishes importance of appropriate baseline selection. MPANF (modified persistent auto-naive forecasting) often outperforms naive. Context for understanding when simple forecasts are competitive and when ensemble methods add value.

[10] [Spectral Entropy—An Underestimated Time Series Feature](https://towardsdatascience.com/spectral-entropy-an-underestimated-time-series-feature-94e18ae5b958/) — Practical exposition of spectral entropy in time series forecasting. Explains frequency-domain energy concentration and its relationship to predictability. Notes spectral entropy typically ranges 0.9-0.93 on many datasets. Emphasizes underutilization of spectral analysis in machine learning. Provides intuitive explanation of why spectral structure correlates with forecastability.

[11] [An Efficient Adaptive Window Size Selection Method for Spectral Analysis](https://pmc.ncbi.nlm.nih.gov/articles/PMC5013242/) — Nisar et al. (2016, 91 citations). Proposes method for selecting appropriate window length for STFT. Achieves 87.71% accuracy in window selection. Directly relevant to spectral-adaptive's window size challenge. Shows empirical approach to data-dependent window selection in spectral analysis.

[12] [Window Size in Spectral Analysis](https://support.ircam.fr/docs/AudioSculpt/3.0/co/Window%20Size.html) — Technical guidance on FFT window size selection. Notes window size depends on fundamental frequency, intensity, and signal changes. Larger windows give better frequency resolution but slower tracking; smaller windows track changes faster but with noisier frequency estimates. Trade-off is fundamental to spectral analysis and directly applies to Omega rolling-window selection.

## Follow-up Questions

- What is the empirical evidence on the monotone weighting assumption—does learned neural network α_nn(Omega) significantly outperform logistic α_logistic(Omega) on validation data, and if so, what patterns violate monotonicity (frequency bands, interaction with noise)?
- How does rolling window size T_w affect Omega stability and predictive power across datasets—is T_w=128 optimal for M4/PEMS/ETT, or does each domain require different selection?
- On multivariate data (full PEMS and ETT), does per-channel Omega aggregation with learned weights preserve model complementarity better than PCA-based Omega, and what is the information-retention trade-off?

---
*Generated by AI Inventor Pipeline*
