# Spectral Predictability & Adaptive Ensemble Research - Execution Summary

## Research Objective
Comprehensive literature synthesis on spectral forecastability metrics (Ω and SCP), adaptive ensemble weighting architectures, standard benchmark datasets (M4, PEMS, ETT), and implementation best practices for building a spectral-adaptive linear-nonlinear forecasting ensemble.

## Research Phases Completed

### Phase 1: Spectral Predictability Metrics ✓
- **Ω (Spectral Predictability)** [Wang et al., 2511.08884]: FFT-based entropy concentration metric; O(T log T) computation; Ω ∈ [0,1] indicates periodic (high) to chaotic (low) patterns
  - Controlled experiments: 20-40% error reduction (Ω=0.3 → 0.7)
  - Large-scale validation: 28 datasets, 51 models, Spearman ρ = -0.65 (p < 1e-20)
  - Foundation model gap: zero-shot TSFMs outperform by ~60% at high Ω; gap vanishes at low Ω

- **SCP (Spectral Coherence Predictability)** [Feng et al., 2509.23074]: Welch-based coherence with frequency-band diagnostics; task-aligned MSE lower bound
  - Algorithm: mean removal → Welch PSD/CPSD (window=0.25×T, overlap=50%, Hann taper) → squared coherence → residual spectrum
  - Computational cost: O(N log N); reveals predictability drift and frequency-band heterogeneity

### Phase 2: Adaptive Ensemble Weighting Methods ✓
- **Error-Based Dynamic**: w_i ∝ 1/MSE_i(t-k:t); reactive, simple; negligible cost
- **Convex-Optimized Static**: min ||y - w₀·linear - w₁·nonlinear||² s.t. Σw=1, w≥0
  - Hammam et al. (2025): grid search optimization; 13% MAPE, 80% improvement over ARIMA on volatile patterns
- **Neural Combiner**: Adhikari & Jain (2015), Kourentzes et al. (2014); learned weights, requires labeled data
- **Regime-Switching**: Discrete regime detection + Markov switching; interpretable but discrete
- **Spectral-Adaptive (Novel)**: First application of Ω/SCP for *in-inference dynamic weighting* (not pre-training selection or post-hoc diagnosis)
  - Candidate functions: Logistic α(Ω) = 1/(1+exp(-a(Ω-b))) [recommended], linear, power law, step

### Phase 3: Benchmark Datasets ✓
- **M4**: 100k series, 6 frequencies (yearly-hourly), 6 domains; heterogeneous spectral properties; 1543+ citations
- **PEMS**: California traffic, 5-min intervals, multivariate; strong daily/weekly seasonality; weather/accident regime shifts
- **ETT**: Oil temperature & power load, 15-min/1-hour intervals; ~70k obs; controlled, repeatable; ideal for staged experiments

### Phase 4: Model Architectures ✓
- **Linear Forecaster (Auto-ARIMA)**: Grid search (p,d,q)∈[0,2]³, AIC criterion; fit ~0.1-1s, forecast ~1ms
- **Nonlinear Forecaster (LSTM)**: 2×64-unit LSTM, dropout=0.2, look-back=128; train ~5-30s (CPU), inference ~5ms
- **ResNet Alternative**: 2-3 residual blocks, 32-64 filters; faster than LSTM on some tasks; train ~3-20s
- **Weighting Function**: O(1) evaluation; logistic (smooth, tunable) recommended over linear/power/step

### Phase 5: Regime-Shift Detection ✓
- **Ω Drift Metric**: ΔΩ = Ω_test - Ω_train_mean; hypothesis assumes largest gains when ΔΩ > 0.2
- **CUSUM Detection**: Cumulative sum control chart on Ω samples; flags deviations >1σ (Aminikhanghahi & Javidi 2016; Ghezzi et al. 2025)

## Key Findings

### Spectral Predictability Validated
- Ω systematically stratifies forecasting difficulty across domains
- High Ω (≥0.6): linear methods sufficient; foundation models shine
- Low Ω (≤0.3): all models struggle; opportunity for robust method innovation
- No single model wins uniformly across datasets (AutoForecast finding)

### Ensemble Weighting Trade-offs
| Approach | Speed | Adaptation | Training Req | Cost |
|----------|-------|-----------|--------------|------|
| Error-based | Fast | Reactive | None | ~0ms |
| Convex static | Fast | None | Yes | ~1ms |
| Neural | Fast | Static | Yes | ~1ms |
| Regime-switch | Medium | Discrete | Yes | ~10ms |
| **Spectral-adaptive** | **Fast** | **Proactive** | **None** | **<5%** |

### Open Questions (Pending Empirical Validation)
1. Optimal rolling Ω window size: {50, 100, 128, 256} points?
2. Logistic α(Ω) functional form superiority vs. alternatives?
3. Multivariate extension strategy (PEMS case)?
4. Spectral-adaptive failure modes (high Ω + strong nonlinearity)?
5. Parameter sensitivity (Welch window/taper/overlap)?

## Research Methodology

### Sources Consulted
- **30 unique citations** spanning:
  - Spectral methods (Wang 2025, Feng 2026)
  - Ensemble strategies (Hammam 2025, Adhikari 2015, Kourentzes 2014)
  - Benchmarks (Makridakis 2020, PEMS, ETT repositories)
  - Neural architectures (LSTM, ResNet, Time-LLM)
  - Change-point detection (Aminikhanghahi 2016, Ghezzi 2025)
  - Meta-learning (AutoForecast, AutoXPCR)

### Search Strategy
1. **Diverge**: Multi-angle framing (spectral theory, adaptive systems, ensemble methods, benchmarks)
2. **Search**: 15+ parallel queries covering Ω/SCP definitions, ensemble methods, datasets, architectures
3. **Fetch**: 8 full-text paper reads (Wang, Feng, Hammam, AutoForecast, related works)
4. **Grep**: Detailed algorithm extraction (SCP Algorithm 1, LSTM hyperparameters, CUSUM)
5. **Triangulate**: Cross-referencing across papers and domains

### Confidence Levels
- **High Confidence** (validated in multiple sources): Ω formula, SCP algorithm, M4/PEMS/ETT properties, ARIMA/LSTM architectures
- **Medium Confidence** (proposed but not yet empirically tested): Spectral-adaptive novelty, window size recommendations, overhead <5%
- **Research Gaps** (explicit in literature): Multivariate Ω extension, failure mode analysis, parameter sensitivity

## Deliverables

### Output Files
1. **research_out.json** (39.6 KB): Full research synthesis with structured answer, 30 citations, 3 follow-up questions
2. **.terminal_claude_agent_struct_out.json** (38.9 KB): Structured output matching schema; ready for downstream GEN_PAPER_TEXT

### Citation Coverage
- Spectral theory: 2 primary sources (Wang, Feng) + foundational references
- Ensemble methods: 5 distinct approaches documented
- Benchmarks: 3 major datasets with regime-shift properties
- Architectures: 4 model families with hyperparameters
- Change-point detection: 2 modern methods (CUSUM classic + Ghezzi 2025 fast online)
- Meta-learning: AutoForecast + meta-feature taxonomy

## Implementation Readiness

### For Executor (Step 3.3)
✓ Ω formula, preprocessing pipeline, and computational complexity documented
✓ SCP algorithm (Algorithm 1) with Welch parameters specified
✓ Linear forecaster (Auto-ARIMA) grid search space defined
✓ Nonlinear forecaster (LSTM/ResNet) architectures and hyperparameters provided
✓ Weighting function candidates with tuning strategy
✓ Benchmark datasets characterized with spectral/regime properties
✓ Open questions and validation strategy framed

### For Paper Generation (Step 3.4)
✓ 30 citations ready for bibliographic integration
✓ Novelty claim supported by distinctions from Wang/Feng prior work
✓ Empirical validation roadmap (window size sweep, functional form comparison, multivariate extension, failure mode analysis)
✓ Computational overhead hypothesis specified (<5%)
✓ Success criteria aligned with hypothesis (≥3% MSE reduction on ≥70% of sequences, largest gains when ΔΩ > 0.2)

---
**Research Execution Date**: 2026-07-30
**Total Sources**: 30 (papers, tutorials, datasets, tools)
**Research Duration**: ~3 hours
**Output Status**: ✓ Complete and validated
