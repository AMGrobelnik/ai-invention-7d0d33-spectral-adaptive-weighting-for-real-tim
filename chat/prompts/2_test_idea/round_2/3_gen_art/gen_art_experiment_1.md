# gen_art_experiment_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_art`
> Run: `run_oxbmYex8-G2P` — Spectral Adaptive Weighting for Real-Time Ensemble Forecasting
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_experiment_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-07-30 12:52:14 UTC

```
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: An artifact executor (Step 3.3: GEN_ART in the invention loop)

Executing a plan to produce a concrete artifact.
GEN_PAPER_TEXT will use your artifact in the next paper draft.

Rigorous artifact with clear results → strong paper. Sloppy artifact → misdirected research.
</your_role>
</ai_inventor_context>

<research_methodology>
Design experiments like a researcher, not a programmer running a script.

- Every method needs a meaningful baseline — the current standard approach, not a strawman.
- Control your variables. When comparing methods, hold everything else constant.
- Results need variance, not just point estimates. A single run proves nothing.
- Implement the proposed method and baseline side-by-side in the same pipeline to eliminate implementation-level confounds.
</research_methodology>

<task>
Implement the research methodology as a production-ready experimental system.
Adapt your implementation approach based on the hypothesis and domain requirements.
</task>

<critical_requirements>
- Fully implement the methodology described in hypothesis
- Use appropriate frameworks based on research domain
- Load and process data from the specified data_filepath
- Complete working systems
- Handle all edge cases, errors, and exceptions properly
- Always implement baseline comparison method
</critical_requirements>

<common_mistakes_to_avoid>
- Holding multiple large objects in memory at once — process one at a time: load → compute → del + gc.collect() → next
- Loading more data than needed — select only required tables/columns/rows
- Accumulating results in loops without freeing intermediates — aggregate incrementally
- Spawning too many parallel processes — stay within the hardware limits
- Running computation without timeouts or without first testing on a small sample
</common_mistakes_to_avoid>

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

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_oxbmYex8-G2P/3_invention_loop/iter_2/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_oxbmYex8-G2P/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_oxbmYex8-G2P/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_oxbmYex8-G2P/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_oxbmYex8-G2P/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_experiment_1_idx1
type: experiment
title: Spectral-Adaptive Ensemble Validation
summary: >-
  Implement and validate spectral-predictability-driven online weighting for ARIMA+LSTM ensemble on M4/finance/energy datasets.
  Test core hypothesis: spectral predictability Ω correlates with optimal linear-vs-nonlinear blend weights. Execute with
  ablations (window size, weighting form, monotone vs. non-monotone) and statistical rigor (95% CIs, paired t-tests).
runpod_compute_profile: gpu
implementation_pseudocode: "1. DATA LOADING & VALIDATION\n   - Load dataset from dependency (full_data_out.json, 440 examples)\n\
  \   - Parse each example: extract series (input), train/test split (metadata_train_end_idx)\n   - Validate: no NaN, series\
  \ length ≥250, test set ≥10 points\n   - Track: series_id, domain, frequency, spectral_power_ratio (Ω proxy)\n\n2. SPECTRAL\
  \ PREDICTABILITY COMPUTATION\n   - Implement Ω computation on rolling windows: Ω = sum(top-k power) / sum(all power)\n \
  \  - Use numpy.fft.rfft for power spectrum (O(N log N))\n   - Test window sizes: {32, 64, 128, 256} (hyperparameter sweep)\n\
  \   - For each window position: compute Ω, store time series of Ω\n   - Verify: Ω ∈ [0,1], high Ω ⟹ concentrated spectrum\
  \ (periodic), low Ω ⟹ diffuse (chaotic)\n\n3. BASELINE FORECASTERS (ARIMA & LSTM)\n   \n   3a. ARIMA (linear baseline)\n\
  \       - Use statsmodels auto_arima for automatic order selection\n       - Grid search: p,d,q ∈ [0,2]³ with AIC criterion\n\
  \       - Fit on train data (up to metadata_train_end_idx)\n       - Forecast horizon = len(test_values)\n       - Output:\
  \ point forecasts (1D array)\n   \n   3b. LSTM (nonlinear baseline)\n       - PyTorch implementation: 2 stacked layers,\
  \ 64 units each, dropout 0.2\n       - Input: lookback window L=128 time steps, output: 1-step ahead (recursive forecast)\n\
  \       - Fit on train data with 10% validation split for early stopping\n       - Optimizer: Adam, learning_rate=0.001,\
  \ batch_size=16, epochs=100 (or early stop)\n       - Forecast recursively for full test horizon (append predictions, use\
  \ as next input)\n       - Output: point forecasts (1D array)\n\n4. HYPERPARAMETER TUNING FOR WEIGHTING FUNCTION α(Ω)\n\
  \   \n   4a. Validation set split\n       - Split training data: 70% fit (ARIMA/LSTM), 30% validation (tune α)\n       -\
  \ Compute Ω on validation window (same T_w as test)\n   \n   4b. Weighting function candidates\n       - Logistic: α(Ω)\
  \ = 1 / (1 + exp(-a(Ω - b)))\n           Grid: a ∈ [0.1, 1, 5, 10, 50], b ∈ [0.1, 0.3, 0.5, 0.7, 0.9]\n       - Linear:\
  \ α(Ω) = max(0, min(1, c·Ω + d))\n           Grid: c ∈ [-1, 0, 1, 5], d ∈ [-1, 0, 1]\n       - Power-law: α(Ω) = Ω^p for\
  \ p ∈ [0.5, 1, 2, 3]\n       - Non-monotone (neural): 2-layer NN, 32 units, input Ω, output α ∈ [0,1]\n   \n   4c. Optimization\n\
  \       - For each function candidate: blend forecasts as: ŷ = α(Ω)·ŷ_arima + (1-α(Ω))·ŷ_lstm\n       - Compute MSE on validation\
  \ set\n       - Keep best-performing α parameters (minimum validation MSE)\n\n5. TEST-TIME EVALUATION\n   \n   5a. Ensemble\
  \ forecasting\n       - Compute rolling Ω on test window (same T_w used in training)\n       - Apply learned α(Ω) to blend:\
  \ ŷ_blend = α(Ω)·ŷ_arima + (1-α(Ω))·ŷ_lstm\n       - Compute test MSE, RMSE, MAE\n   \n   5b. Baseline comparisons (on same\
  \ test set)\n       - Fixed 0.5/0.5 ensemble: ŷ = 0.5·ŷ_arima + 0.5·ŷ_lstm\n       - Static per-series optimal (convex):\
  \ α* = argmin_α MSE on validation, fixed for test\n       - Error-based dynamic weighting (reactive): α_t = 1 / (1 + |e_arima,t|\
  \ / |e_lstm,t|) using recent validation errors\n       - ARIMA-only\n       - LSTM-only\n   \n   5c. Summary metrics per\
  \ series\n       - MSE, RMSE, MAE for each method (spectral-adaptive, 5 baselines)\n       - Spectral statistics: Ω_train_mean,\
  \ Ω_train_std, Ω_test_mean, Ω_test_std, Ω_regime_shift = |Ω_test_mean - Ω_train_mean|\n       - Relative improvement: Δ_vs_fixed\
  \ = (MSE_fixed - MSE_spectral) / MSE_fixed (positive = spectral wins)\n\n6. AGGREGATED ANALYSIS & STATISTICAL TESTING\n\
  \   \n   6a. Per-domain and overall statistics\n       - For each method: collect all per-series MSE values\n       - Compute:\
  \ mean MSE, std MSE, median MSE, 95% CI via bootstrap (1000 resamples)\n   \n   6b. Paired t-tests\n       - Paired t-test\
  \ (spectral-adaptive vs. fixed 0.5/0.5) on MSE deltas\n       - Bonferroni correction: α = 0.05 / number of tests\n    \
  \   - Report: t-statistic, p-value, effect size (Cohen's d)\n   \n   6c. Regime-shift sensitivity\n       - Stratify series\
  \ by Ω_regime_shift quartiles\n       - Compare spectral-adaptive vs. fixed ensemble separately in each quartile\n     \
  \  - Hypothesis: largest wins in high-shift quartiles (>0.2 Ω change)\n\n7. ABLATION STUDIES (integrated into single run)\n\
  \   \n   7a. Window size ablation\n       - Repeat steps 2-6 for each T_w ∈ {32, 64, 128, 256}\n       - Track: MSE mean/std\
  \ for spectral-adaptive across window sizes\n       - Report: which T_w minimizes MSE?\n   \n   7b. Weighting form comparison\n\
  \       - For each form (logistic, linear, power-law, NN):\n         - Tune on same validation set\n         - Evaluate\
  \ on test set\n         - Report: MSE, comparison table\n   \n   7c. Monotone vs. non-monotone\n       - Implement 2-layer\
  \ NN without monotonicity constraint\n       - Compare test MSE: logistic (constrained monotone) vs. NN (unconstrained)\n\
  \       - Test: does removing monotonicity constraint hurt or help?\n\n8. OUTPUT GENERATION\n   \n   8a. method_out.json\
  \ structure:\n       {\n         \"experiment_summary\": {\n           \"total_series\": N,\n           \"series_with_regime_shift\"\
  : count_gt_0.2,\n           \"compute_time_seconds\": total_time\n         },\n         \"methods\": {\n           \"spectral_adaptive\"\
  : {\"mse\": [...], \"mean\": X, \"std\": Y, \"ci_95\": [L, U]},\n           \"fixed_0.5_0.5\": {...},\n           ...\n\
  \         },\n         \"statistical_tests\": {\n           \"spectral_vs_fixed\": {\"t_stat\": X, \"p_value\": Y, \"cohens_d\"\
  : Z}\n         },\n         \"ablations\": {\n           \"window_size\": {\"32\": X, \"64\": Y, ...},\n           \"weighting_form\"\
  : {\"logistic\": X, \"linear\": Y, ...},\n           \"monotone_vs_nn\": {\"logistic_mse\": X, \"nn_mse\": Y}\n        \
  \ },\n         \"per_series_detailed\": [\n           {\"series_id\": S, \"domain\": D, \"omega_train\": X, \"omega_test\"\
  : Y, \"mse_spectral\": Z, ...},\n           ...\n         ]\n       }\n   \n   8b. Figures (matplotlib + pickle):\n    \
  \   - Fig 1: Rolling Ω time series (train vs. test) for 5 representative series\n       - Fig 2: Learned weighting functions\
  \ α(Ω) for each weighting form\n       - Fig 3: Window size vs. MSE/variance trade-off (line plot + error bars)\n      \
  \ - Fig 4: Weighting form comparison (bar chart: logistic vs. linear vs. power-law vs. NN)\n       - Fig 5: MSE distribution\
  \ by method (box plots, 6 methods side-by-side)\n       - Fig 6: Regime-shift sensitivity (scatter: Ω_shift vs. MSE improvement,\
  \ per series)\n\n9. ERROR HANDLING & FALLBACKS\n   - If auto_arima fails for a series (no convergence): use ExponentialSmoothing\
  \ fallback\n   - If LSTM training diverges: reinitialize, reduce learning_rate to 0.0001\n   - If Ω computation yields NaN\
  \ (e.g., all-zero window): clip Ω to [0.01, 0.99]\n   - If test set too small (<5 points): skip series, log warning\n\n\
  10. COMPUTATIONAL TRACKING\n    - Time spectral computation, ARIMA fit, LSTM fit, ensemble blend per series\n    - Verify\
  \ overhead <5% vs. static ensemble (reported in method_out.json)\n    - Use multiprocessing for independent series (map\
  \ over CPU cores, avoid GPU bottleneck)"
fallback_plan: |-
  FALLBACK 1: Reduced Dataset Scope
    If full 440 series takes >5 hours: sample 100 representative series (stratified by domain, Ω quartile), report as 'validation on representative subset'.

  FALLBACK 2: Simplified ARIMA Fit
    If auto_arima grid search is too slow: use fixed (p=1, d=1, q=1) ARIMA for all series instead. Accept reduced baseline quality; focus on ensemble weighting logic.

  FALLBACK 3: Smaller LSTM
    If LSTM training is slow (>30s per series): reduce to 1 layer × 32 units, epochs=50, batch_size=32. Trade accuracy for speed.

  FALLBACK 4: Single Window Size
    If ablation of 4 window sizes is too slow: use T_w=128 only (most commonly recommended in literature), skip ablation. Report as limitation.

  FALLBACK 5: Simplified Weighting Functions
    If hyperparameter tuning grid is too large: use only logistic α(Ω) with fixed grid a∈[0.1, 1, 10], b∈[0.3, 0.5, 0.7] (27 configs instead of 50). Defer linear/power-law/NN to future work.

  FALLBACK 6: Skip Statistical Testing
    If insufficient time: compute mean/std MSE only, skip Bonferroni-corrected t-tests. Report raw improvement percentages with caveat: 'statistical significance not tested'.

  FALLBACK 7: Minimal Figures
    If plotting is slow: produce 2 key figures (rolling Ω example, MSE distribution by method), defer regime-shift scatter and weighting function curves.

  FALLBACK 8: CPU-Only Execution
    If GPU unavailable or causing driver issues: disable PyTorch GPU, use CPU-based LSTM training (torch.device('cpu')). Will be slower but ensures reproducibility.
testing_plan: |-
  PHASE 1: RAPID SMOKE TEST (15 minutes)
    1. Load 1 representative example from each domain (energy, finance, transportation, weather)
    2. For each series:
       - Compute Ω on 50% of data (quick FFT test)
       - Fit ARIMA with fixed (1,1,1) order (skip auto_arima grid)
       - Train LSTM for 5 epochs only (tiny network)
       - Apply fixed 0.5/0.5 ensemble on remaining 50%
       - Check: output arrays have correct shape, MSE is numeric
    3. Confirm: no crashes, no NaN, output can serialize to JSON
    4. Goal: verify pipeline logic before full run
    5. Success signal: 4 series × 2 methods (ARIMA, LSTM) produce forecasts with MSE ∈ (0, 10^6]

  PHASE 2: MINI DATASET TEST (30 minutes)
    1. Load first 20 series from dataset (stratified: 5 per domain)
    2. Full pipeline: hyperparameter tuning on validation, test evaluation
    3. Compute spectral-adaptive and 3 baselines (fixed 0.5/0.5, error-based, ARIMA-only)
    4. Generate method_out.json and 2 figures (rolling Ω, MSE distribution)
    5. Check:
       - Spectral-adaptive MSE ≤ ARIMA-only and LSTM-only MSE (at least one series)
       - Window size ablation produces variation (not all identical)
       - No serialization errors
    6. Success signal: method_out.json validates against schema, contains >0 series results

  PHASE 3: REGIME-SHIFT STRATIFICATION TEST (10 minutes)
    1. In mini dataset: identify 2 series with high Ω_regime_shift (>0.2) and 2 with low (<0.05)
    2. Verify: MSE improvement (spectral vs. fixed) is larger in high-shift group
    3. Success signal: high-shift Δ_MSE ≥ low-shift Δ_MSE for ≥1 series

  PHASE 4: FULL DATASET EXECUTION (60-90 minutes)
    1. Once mini tests pass, execute on all 440 series
    2. Monitor: print progress every 50 series (elapsed time, ETA)
    3. Checkpoint: save partial method_out.json every 100 series (resumable)
    4. Track: count of skipped series (failures), reasons
    5. Success criteria:
       - Spectral-adaptive achieves ≥3% lower test MSE vs. fixed on ≥60% of series (relaxed from 70%)
       - Paired t-test p-value <0.05 (Bonferroni-corrected)
       - Regime-shift quartile analysis shows expected trend

  FAILURE MODES TO MONITOR
    - auto_arima: no valid model found → fallback to ExponentialSmoothing (counts as 'series_failure')
    - LSTM: NaN loss (exploding gradient) → restart with lower lr (max 2 restarts)
    - Ω computation: constant series (all values identical) → clip to Ω=0.5, log warning
    - Test set: too short (<5 points) → skip series entirely
    - Overall time: if mini test takes >45 min, abort, reduce to 50 series for full run

  CHECKPOINTS FOR PIVOTING
    - After Phase 1: if crashes, debug logging to identify which step fails (FFT? ARIMA? LSTM?)
    - After Phase 2: if spectral-adaptive doesn't beat ≥1 baseline, investigate:
      * Is Ω truly capturing predictability? (Compare to actual errors)
      * Is weighting function α converging? (Plot α vs. Ω scatter)
      * Are ARIMA and LSTM complementary? (Check their errors on same series)
    - After Phase 3: if regime-shift does NOT show expected trend, consider:
      * Ω is computed on test set → recompute on held-out validation
      * Monotonicity assumption is wrong → enable NN weighting
    - If overall >50% series skipped: switch to 50-series subset, accept 'limited validation scope' label
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
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
out_dependency_files:
  file_list:
  - data.py
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json
  data_file_paths:
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json

Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</dependencies>

<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **HARD LIMIT**: Maximum $10 USD total spend on LLM API calls (OpenRouter). Track cumulative cost after every call and STOP IMMEDIATELY if approaching this limit. Never exceed this budget under any circumstances.
</software_constraints>

<skills>
Skills are self-contained capabilities with instructions, context, and tools.

- aii-web-tools: Web search (Serper), page/PDF fetch as markdown, regex grep over page/PDF text
- aii-semscholar-bib: Batch-fetch BibTeX from Semantic Scholar
- aii-openrouter-llms: Search and call 300+ LLMs via OpenRouter
- aii-hf-datasets: Search, preview, download HuggingFace datasets
- aii-owid-datasets: Search and load Our World in Data tables
- aii-lean: Compile/verify Lean 4 code, Mathlib search, tactic suggestions
- aii-image-gen: Generate/edit images via Gemini 3 Pro Image (Nano Banana Pro)
- aii-json: Validate JSON against schemas, generate mini/preview variants
- aii-paper-writing: Academic paper structure, bibliography, citations
- aii-paper-to-latex: Assemble LaTeX papers and compile to PDF
- aii-parallel-computing: GPU acceleration, CPU parallelism, async I/O
- aii-python: Python coding standards for experiment scripts
- aii-use-hardware: Detect CPU/RAM/GPU, memory-safe processing
- aii-long-running-tasks: Gradual scaling pattern for long-running tasks
- aii-colab: Google Colab runtime constraints for notebooks
- aii-file-size-limit: Check and split oversized output files
</skills>
</available_resources>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for framework choices, implementation patterns, agent orchestration.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-python, aii-long-running-tasks, aii-json, aii-file-size-limit, aii-use-hardware, aii-parallel-computing.
TODO 2. Read preview files from dependencies to understand data structure. Use ALL datasets provided — do not skip or select a subset. Read domain handbook if applicable (see <available_domain_handbooks>). Test basic functionality with 'uv run'.
TODO 3. Fully implement our method AND baseline (comparison) as described in artifact plan in './method.py'. Use exp_gen_sol_out.json schema in aii-json skill for output format validation. Include everything specified in the artifact plan, but you may also implement additional relevant methods or analysis beyond what's listed. Be very attentive to meticulously and exhaustively fix any errors in your code.
</todos>
```

### [2] HUMAN-USER prompt · 2026-07-30 12:52:14 UTC

```
Test whether a 3-point moving average beats a naive last-value forecast on a short synthetic series. Keep the investigation minimal.
```

### [3] SKILL-INPUT — aii-python · 2026-07-30 12:52:44 UTC

The agent loaded the **aii-python** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-python
description: Python coding standards for experiment and evaluation scripts. Covers environment setup, logging, error handling, and code structure.
---

## Environment Setup

- Python 3.12+
- **NEVER use `pip` or `.venv/bin/pip`** — they are not installed. Use `uv` for ALL package operations:
  ```bash
  uv venv .venv --python=3.12
  source .venv/bin/activate  # or: .venv/bin/python script.py
  uv pip install pandas loguru  # NOT: pip install
  ```
- Create `.toml` file with dependencies, create uv `.venv` and activate it
- NO inline dependencies (no `# /// script` headers)

## Logging

Use `loguru` for all logging. Add a file sink alongside stdout.

```python
from loguru import logger
import sys

logger.remove()  # Remove default handler
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")
```

Rules:
- Log every major step (data loading, processing start/end, results)
- If applicable, log every LLM API call input and output
- Truncate long outputs in logs (add truncation logic for potentially large strings)
- Use `logger.error()` in except blocks (traceback auto-captured)

## Error Handling

- Wrap major operations in try/except blocks
- Use `@logger.catch(reraise=True)` decorator on main functions — without `reraise=True`, the script exits 0 even on uncaught exceptions, hiding failures from downstream consumers
- Use explicit exception types, not bare `except:`
- Never silently swallow exceptions — always log them

```python
@logger.catch(reraise=True)
def main():
    try:
        data = load_data(path)
    except FileNotFoundError:
        logger.error("Data file not found")
        raise
    except json.JSONDecodeError:
        logger.error("Invalid JSON in data file")
        raise
```

## Code Structure

- Use `pathlib.Path` for file operations: `Path("data/input.json").read_text()` not `open(...).read()`
- Use type hints for function signatures
- Use keyword arguments for functions with more than 4 parameters
- No hardcoded paths — derive from script location or accept as arguments

## Script Pattern

Standard pattern for experiment/evaluation scripts:

```python
#!/usr/bin/env python3
"""Brief description of what this script does."""

from loguru import logger
from pathlib import Path
import json
import sys

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def main():
    # Load data
    data_path = Path("full_data_out.json")
    logger.info(f"Loading data from {data_path}")
    data = json.loads(data_path.read_text())
    logger.info(f"Loaded {len(data['examples'])} examples")

    # Process
    results = []
    for i, example in enumerate(data["examples"]):
        try:
            result = process(example)
            results.append(result)
        except Exception:
            logger.error(f"Failed on example {i}")
            continue

    # Save output
    output = {"examples": results}
    Path("method_out.json").write_text(json.dumps(output, indent=2))
    logger.info(f"Saved {len(results)} results")

if __name__ == "__main__":
    main()
```
````

### [4] SKILL-INPUT — aii-long-running-tasks · 2026-07-30 12:52:44 UTC

The agent loaded the **aii-long-running-tasks** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-long-running-tasks
description: Gradual scaling pattern for long-running autonomous tasks. Use when running experiments, evaluations, or any code that processes data at increasing scale with runtime checks.
---

## Core Principles

1. **Time budget first**: Read your time/runtime constraints before running anything. Set every Bash timeout to fit within the budget.
2. **Start small, scale up**: Run on minimal input first, fix errors, then increase scale.
3. **Extrapolate before scaling**: Use recorded runtimes to predict whether the next step fits in the budget. Don't guess — calculate.
4. **Background execution**: For anything that takes >1 min, run in background (`run_in_background=true`) and do useful work while waiting.
5. **Stop early if needed**: Quality results on less data beats a timeout or crash. It's always acceptable to stop at a smaller scale.

---

## Gradual Scaling Sequence

Run code at increasing data sizes, checking runtime at each step.

Substitute your actual file names:
- `{mini_file}` — mini JSON (3 examples) from dependency workspace
- `{full_file}` — full dataset from dependency workspace
- `{script}` — your processing script (e.g., `./method.py`, `./eval.py`)
- `{schema}` — JSON schema to validate output against

**STEP 1 — MINI DATA:** Run `{script}` on `{mini_file}`. Do NOT truncate logs. Fix all errors. Validate output against `{schema}`. Verify you are NOT using mock scripts, mock data, or mock APIs.

**STEP 2 — 10 EXAMPLES:** Modify `{script}` to load only the first 10 examples from `{full_file}`. Run and fix errors. Validate schema. Record the runtime.

**STEP 3 — 50 EXAMPLES:** Load first 50 examples from `{full_file}`. Run and fix errors. Record runtime. **EXTRAPOLATE**: Using runtimes from steps 2-3, estimate time per example. Calculate how many examples fit in your remaining time budget. If 50 already used most of the budget, stop here.

**STEP 4 — 100 EXAMPLES (if budget allows):** Load first 100 examples. Run and fix errors. Record runtime. Re-extrapolate with the new data point.

**STEP 5 — 200 EXAMPLES (if budget allows):** Load first 200 examples from `{full_file}`. Run and fix errors. Record runtime.

**STEP 6 — MAXIMIZE:** Using all recorded runtimes, extrapolate time-per-example (it may not be perfectly linear — account for overhead). Calculate the maximum number of examples that fits within your remaining time budget with a 10% safety margin. Load that many (or all if they fit). Run and validate.

## Final Testing Phase

After completing the scaling sequence, redo the entire sequence **one more time** up to your final example count:

mini → 10 → 50 → 100 → 200 → max

At each scale: look for issues, fix problems, validate output, ensure it completes within time limits.

---

## Background Execution

For any step that takes >1 min, run as a **background task**:

1. Launch with Bash `run_in_background=true`
2. While it runs, use the time productively:
   - Sanity-check previous outputs
   - Verify file integrity (correct field names, non-empty values)
   - Review code for edge cases at larger scale
   - Prepare the next step
3. Check back on the background task to get results
4. If it failed, fix errors and re-run

---

## Resource Limits

Set hard RAM and CPU time limits so code fails fast instead of crashing the system. Read limits from `<hardware>` and leave headroom for the OS (e.g., if 16GB total, cap at 14GB).

Python example using stdlib `resource` module:
```python
import resource
resource.setrlimit(resource.RLIMIT_AS, (14 * 1024**3, 14 * 1024**3))  # 14GB RAM
resource.setrlimit(resource.RLIMIT_CPU, (3600, 3600))  # 1 hour CPU time
```
Exceeding RAM raises `MemoryError`. Exceeding CPU time sends `SIGKILL`.

## Monitoring

At each step, record runtime AND check resource usage (`free -h` for RAM, `top -bn1 | head -5` for CPU). If memory usage is climbing toward the limit or CPU is pegged, stop and investigate before scaling further.
````

### [5] SKILL-INPUT — aii-json · 2026-07-30 12:52:44 UTC

The agent loaded the **aii-json** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-json
description: JSON validation and formatting toolkit. Validate JSON files against schemas for experiment pipelines, and generate full/mini/preview versions of JSON datasets. Use for validating pipeline outputs, checking schema compliance, or creating size-optimized JSON variants.
---

## Contents

- Validating JSON (schema validation against experiment schemas)
- Formatting JSON (generate full/mini/preview versions)

**IMPORTANT - Parallel execution:** GNU `parallel` subshells do NOT inherit `source activate`. Use `export` for variables and **single-quoted** command templates so parallel's subshells can resolve them:
```
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

---

## Validating JSON

Validate JSON files against predefined schemas for experiment-based hypothesis selection, data collection, solution generation, and evaluation.

### Quick Start

1. Read the schema spec you need to adhere to (e.g., `schemas/exp_eval_sol_out.json`)
2. Create your output file following that schema structure
3. Validate:

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_validate_schema.py --format exp_eval_sol_out --file /path/to/eval_out.json
```

### Script: aii_json_validate_schema.py

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_validate_schema.py --format exp_eval_sol_out --file /tmp/eval_out.json
```

**Parallel execution (multiple validations):**

IMPORTANT: When validating multiple files, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_json_validate_schema.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --format {1} --file {2}' ::: 'exp_sel_data_out' 'exp_gen_sol_out' 'exp_eval_sol_out' :::+ '/tmp/full_data_out.json' '/tmp/method_out.json' '/tmp/eval_out.json'
```

**Example output (success):**
```
Validating: aii_json_validate_schema.py
Format: exp_eval_sol_out

✓ Validation PASSED
```

**Example output (failure):**
```
Validating: aii_json_validate_schema.py
Format: exp_sel_data_out

✗ Validation FAILED

Errors:
  Path: datasets → 0 → examples → 0
  Error: 'output' is a required property
  Validator: required
```

**Parameters:**

`--format` (required)
- Format type to validate against
- Determines which schema to use

`--file` (required)
- Path to JSON file to validate
- Must be valid JSON
- **Always pass an absolute path.** Relative paths resolve from the
  ability server's CWD (typically ``/ai-inventor/aii_server``), not from
  your agent workspace, so ``data_out/x.json`` will silently look in the
  wrong directory and fail with "Could not load JSON file". The validate
  endpoint also accepts a ``workspace_dir`` arg if you need to keep a
  relative path — pass your workspace path there.

**Tips:**
- Fix errors in your JSON and rerun validation until it passes

### Schema Files

Schemas are stored in `.claude/skills/aii-json/schemas/`:

**Hypothesis Selection & Evaluation:**
- `sel_hypo_out.json` - Hypothesis Selection output (all hypotheses with selected flags)
- `feasibility_eval_all.json` - All hypotheses with feasibility scores
- `feasibility_eval_top.json` - Top 5 most feasible hypotheses
- `novelty_research_one.json` - Single hypothesis novelty research arguments with citations
- `novelty_eval_all.json` - All hypotheses with novelty scores
- `novelty_eval_top.json` - Single best selected hypothesis

**Experiment Pipeline:**
- `exp_sel_data_out.json` - Experiment Data Selection format
- `exp_gen_sol_out.json` - Experiment Solution Generation format
- `exp_eval_sol_out.json` - Experiment Solution Evaluation format

---

## Formatting JSON

Generate three size-optimized versions of a JSON file for efficient development and preview:
- **full**: Identical to original (all data)
- **mini**: First 3 items only (for quick testing)
- **preview**: Mini + all strings truncated to 200 chars (for quick inspection)

### Quick Start

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_format_mini_preview.py --input method_out.json
```

### Script: aii_json_format_mini_preview.py

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_format_mini_preview.py --input method_out.json
```

**Parallel execution (multiple files):**

IMPORTANT: When formatting multiple files, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_json_format_mini_preview.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --input {}' ::: 'full_data_out.json' 'method_out.json' 'eval_out.json'
```

**Example output:**
```
Generated 3 versions:
  Full (50 items): /path/to/full_method_out.json
  Mini (3 items): /path/to/mini_method_out.json
  Preview (3 items, truncated): /path/to/preview_method_out.json
```

**Parameters:**

`--input` (required)
- Path to input JSON file
- Must have a top-level array
- Example: `method_out.json`, `full_data_out.json`

`--output-dir` (optional)
- Output directory for generated files
- Default: same directory as input file
- Files are prefixed with `full_`, `mini_`, `preview_`

**Output Files:**

All three files use the same base name with different prefixes:
- `full_{basename}.json` - Complete dataset (identical to original)
- `mini_{basename}.json` - First 3 array items only
- `preview_{basename}.json` - First 3 items with strings truncated to 200 chars

**Tips:**
- Input JSON must have a top-level array structure
- String truncation is recursive (applies to nested objects and arrays)
- Use preview files for quick inspection without reading large datasets
- Use mini files for developing/testing code before running on full dataset

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [6] SKILL-INPUT — aii-file-size-limit · 2026-07-30 12:52:44 UTC

The agent loaded the **aii-file-size-limit** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

```
---
name: aii-file-size-limit
description: File size check procedure for splitting oversized output files. Use after generating JSON output files to check and split files exceeding the provided size limit.
---

## File Size Check

After generating output files, run `ls -lh` to check sizes. If ANY file exceeds the provided file size limit:

1. Create directory with same base name (e.g., `data_out/` for `full_data_out.json`)
2. Split into parts under the limit named: `full_data_out_1.json`, `full_data_out_2.json`, etc.
3. Place parts in directory (e.g., `data_out/full_data_out_1.json`, `data_out/full_data_out_2.json`)
4. Delete the original oversized file
5. Update the script to read from split files: `for f in sorted(glob.glob('data_out/full_data_out_*.json')): data.extend(json.load(open(f)))`
6. For each split part, generate its own mini/preview versions with the json skill's format script
```

### [7] SKILL-INPUT — aii-use-hardware · 2026-07-30 12:52:44 UTC

The agent loaded the **aii-use-hardware** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-use-hardware
description: Detect hardware and use it responsibly. Covers CPU/RAM/GPU detection, memory-safe data processing, and resource-aware computation.
---

**Step 1** — Run `bash scripts/get_hardware.sh` (relative to this skill's directory).

Read the `=== CGROUP ===` section carefully. If `Type: cgroup v1` or `cgroup v2`:
- You are in a **container with hard resource limits**. Exceeding them = OOM kill, no recovery.
- **Never** use `psutil.virtual_memory().total`, `free -h`, `/proc/meminfo`, `os.cpu_count()`, or `nproc` for resource limits — these report **host** values, not your container's allocation.
- **Always** read limits from the cgroup paths shown in the output, or use the Python helpers below.
- For **runtime memory monitoring**, read current usage from cgroup too:
  - v2: `/sys/fs/cgroup/memory.current`
  - v1: `/sys/fs/cgroup/memory/memory.usage_in_bytes`

**Step 2** — Use Step 1 results to pick package variants **before** installing.

Defaults often target the most powerful environment — PyPI's `torch` ships with CUDA libs even on CPU-only hosts. Wrong variant = wasted disk, slow setup, possible import-time failures.

If `=== GPU ===` shows `No GPU`, install torch's CPU build (skips ~4.5GB of CUDA libs):
```bash
uv pip install torch --extra-index-url https://download.pytorch.org/whl/cpu
```
Same idea for any library whose wheel selection depends on detected hardware (GPU/CPU-only builds, architecture-specific wheels).

After install, sanity-check imports right away (`python -c "import torch"`). Disk-pressure or interrupted installs leave half-built wheels (e.g. `libtorch_global_deps.so` missing) — catch these before the experiment runs.

**Step 3** — Set Python constants from the Step 1 results:
```python
import os, math, torch, psutil
from pathlib import Path

def _detect_cpus() -> int:
    """Detect actual CPU allocation (containers/pods/bare metal)."""
    try:  # cgroups v2 quota
        parts = Path("/sys/fs/cgroup/cpu.max").read_text().split()
        if parts[0] != "max":
            return math.ceil(int(parts[0]) / int(parts[1]))
    except (FileNotFoundError, ValueError): pass
    try:  # cgroups v1 quota
        q = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_quota_us").read_text())
        p = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_period_us").read_text())
        if q > 0:
            return math.ceil(q / p)
    except (FileNotFoundError, ValueError): pass
    try:  # CPU affinity (cpuset — used by RunPod, Docker --cpuset-cpus)
        return len(os.sched_getaffinity(0))
    except (AttributeError, OSError): pass
    return os.cpu_count() or 1

def _container_ram_gb() -> float | None:
    """Read RAM limit from cgroup (containers/pods)."""
    for p in ["/sys/fs/cgroup/memory.max", "/sys/fs/cgroup/memory/memory.limit_in_bytes"]:
        try:
            v = Path(p).read_text().strip()
            if v != "max" and int(v) < 1_000_000_000_000:
                return int(v) / 1e9
        except (FileNotFoundError, ValueError): pass
    return None

NUM_CPUS = _detect_cpus()
HAS_GPU = torch.cuda.is_available()
VRAM_GB = torch.cuda.get_device_properties(0).total_mem / 1e9 if HAS_GPU else 0
DEVICE = torch.device("cuda" if HAS_GPU else "cpu")
TOTAL_RAM_GB = _container_ram_gb() or psutil.virtual_memory().total / 1e9
AVAILABLE_RAM_GB = min(psutil.virtual_memory().available / 1e9, TOTAL_RAM_GB)
```

## Step 4 — Set Memory Limits

OOM kills the entire container. **Every script MUST set RAM and VRAM limits at startup.**

Decide the budget based on what the script actually needs. Estimate data size × 2-5x for in-memory overhead, then add ~50% breathing room for temporaries. You may use up to 90% of available RAM/VRAM, but **scale gradually** — start small (e.g. 30-50%), verify it works, then increase toward the limit. Never exceed 90% to keep a buffer for the OS, system processes, and the agent runtime itself. Going over crashes the container/machine with no recovery.

```python
import resource, psutil

_avail = psutil.virtual_memory().available
RAM_BUDGET = ???  # YOU decide: estimate what this script needs (in bytes)
assert RAM_BUDGET < _avail, f"Budget {RAM_BUDGET/1e9:.1f}GB > available {_avail/1e9:.1f}GB"
resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET * 3, RAM_BUDGET * 3))  # 3x: virtual > RSS; raises MemoryError on exceed

if HAS_GPU:
    _free, _total = torch.cuda.mem_get_info(0)
    VRAM_BUDGET = ???  # YOU decide: estimate GPU memory needs
    torch.cuda.set_per_process_memory_fraction(min(VRAM_BUDGET / _total, 0.95))  # raises OutOfMemoryError on exceed
```

## Memory-Safe Data Processing

- **One at a time**: load one large object → process → `del obj; gc.collect()` → next
- **Load only what you need**: select specific tables/columns/rows, not entire databases
- **Test small first**: run on a sample before scaling to full data to estimate memory/time
- **Free intermediates in loops**: don't accumulate large results — aggregate incrementally
- **Size before loading**: check file/dataset size before loading; if it's >30% of `RAM_BUDGET`, chunk it

## Common Mistakes (from real crashes)

- **Skipping this skill entirely** — loading data with no RAM detection, no limits, no budget. Container OOM-killed, all agents lost.
- **Using `psutil.virtual_memory().total` instead of `_container_ram_gb()`** — reports host RAM (e.g. 66 GB) when container limit is 28 GB. You MUST use the cgroup-aware functions above.
- **Loading all tables from a multi-table database at once** — one agent loaded 14 RelBench tables simultaneously, spiked past container limit.
- **Setting no memory limits** — without `resource.setrlimit` (RAM) and `set_per_process_memory_fraction` (VRAM), a runaway script OOM-kills the container instead of raising a catchable error.
- **Using `os.cpu_count()` directly** — returns host CPUs (e.g. 192) instead of container limit (e.g. 4) on RunPod/Docker. Always use `_detect_cpus()` above which checks cgroup quota → CPU affinity → `os.cpu_count()` in order.

## Hardware Use

- Keep these results in mind for ALL subsequent tasks — don't assume more than detected
- GPU if available and parallelizable, multiprocessing if multiple CPUs
- Push available resources to their full potential — don't leave hardware idle
````

### [8] SKILL-INPUT — aii-parallel-computing · 2026-07-30 12:52:44 UTC

The agent loaded the **aii-parallel-computing** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-parallel-computing
description: "CRITICAL PERFORMANCE SKILL. Maximize hardware utilization for compute-intensive tasks. Covers GPU acceleration, CPU parallelism, and async I/O. The difference between hours of failure and minutes of success. Use whenever writing ANY script that processes data, makes API calls, or does computation."
---

**ALWAYS parallelize. Sequential processing is unacceptable for any non-trivial workload.** A sequential script doing 1000 API calls takes hours and fails halfway. An async version finishes in minutes with proper error handling. ALWAYS ask: "Can this run in parallel?" — the answer is almost always yes.

Read aii-use-hardware skill first → get `NUM_CPUS`, `HAS_GPU`, `VRAM_GB`, `device`. Set `NUM_WORKERS` proportional to available CPU capacity — check `psutil.cpu_percent(interval=1)` and scale accordingly (e.g. 30% used → use ~70% of cores).

## Decision Tree (follow strictly)

- **I/O-bound** (API calls, downloads, web, file reads) → `asyncio` + `aiohttp` with `Semaphore(NUM_WORKERS * 4)`. NEVER do sequential HTTP requests in a loop.
- **CPU-bound, vectorizable** → GPU available: PyTorch on device / No GPU: NumPy vectorized ops. NEVER loop over array elements in Python.
- **CPU-bound, independent items** → `ProcessPoolExecutor(max_workers=NUM_WORKERS)`. NEVER process items one-by-one when they're independent.
- **Sequential** → only acceptable when items have data dependencies (each depends on the previous result).

## GPU Rules

- Use up to 90% of available VRAM — scale gradually (start small, increase after each successful run, keep 10% buffer)
- Move to device → compute → move back: `torch.tensor(data, device=device)` → `.cpu().numpy()`
- OOM fallback: catch `torch.cuda.OutOfMemoryError` → `empty_cache()` → halve batch size → retry on GPU. Keep reducing until it fits. Stay on GPU.
- Batch large data: chunk it, `del batch` between iterations to free VRAM

## Parallelism Rules

- **CPU-bound**: `ProcessPoolExecutor` + `as_completed`, pre-allocate result list indexed by submission order
- **I/O-bound**: `asyncio` + `aiohttp`, `Semaphore(NUM_WORKERS * 4)`, single shared `ClientSession`, `asyncio.gather(*tasks, return_exceptions=True)`
- Always add `tenacity` retries for transient failures, always set timeouts on HTTP requests
- **CRITICAL — `ProcessPoolExecutor` start method**: Default `fork` deadlocks with loguru (and any threading library). ALWAYS pass `mp_context=multiprocessing.get_context("spawn")` when constructing `ProcessPoolExecutor` in any script that uses loguru, threading, or async I/O. Example:
  ```python
  import multiprocessing as mp
  from concurrent.futures import ProcessPoolExecutor
  with ProcessPoolExecutor(max_workers=N, mp_context=mp.get_context("spawn")) as pool:
      ...
  ```
````

### [9] SYSTEM-USER prompt · 2026-07-30 13:18:46 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_oxbmYex8-G2P/3_invention_loop/iter_2/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_oxbmYex8-G2P/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_oxbmYex8-G2P/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_oxbmYex8-G2P/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_oxbmYex8-G2P/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_experiment_1_idx1
type: experiment
title: Spectral-Adaptive Ensemble Validation
summary: >-
  Implement and validate spectral-predictability-driven online weighting for ARIMA+LSTM ensemble on M4/finance/energy datasets.
  Test core hypothesis: spectral predictability Ω correlates with optimal linear-vs-nonlinear blend weights. Execute with
  ablations (window size, weighting form, monotone vs. non-monotone) and statistical rigor (95% CIs, paired t-tests).
runpod_compute_profile: gpu
implementation_pseudocode: "1. DATA LOADING & VALIDATION\n   - Load dataset from dependency (full_data_out.json, 440 examples)\n\
  \   - Parse each example: extract series (input), train/test split (metadata_train_end_idx)\n   - Validate: no NaN, series\
  \ length ≥250, test set ≥10 points\n   - Track: series_id, domain, frequency, spectral_power_ratio (Ω proxy)\n\n2. SPECTRAL\
  \ PREDICTABILITY COMPUTATION\n   - Implement Ω computation on rolling windows: Ω = sum(top-k power) / sum(all power)\n \
  \  - Use numpy.fft.rfft for power spectrum (O(N log N))\n   - Test window sizes: {32, 64, 128, 256} (hyperparameter sweep)\n\
  \   - For each window position: compute Ω, store time series of Ω\n   - Verify: Ω ∈ [0,1], high Ω ⟹ concentrated spectrum\
  \ (periodic), low Ω ⟹ diffuse (chaotic)\n\n3. BASELINE FORECASTERS (ARIMA & LSTM)\n   \n   3a. ARIMA (linear baseline)\n\
  \       - Use statsmodels auto_arima for automatic order selection\n       - Grid search: p,d,q ∈ [0,2]³ with AIC criterion\n\
  \       - Fit on train data (up to metadata_train_end_idx)\n       - Forecast horizon = len(test_values)\n       - Output:\
  \ point forecasts (1D array)\n   \n   3b. LSTM (nonlinear baseline)\n       - PyTorch implementation: 2 stacked layers,\
  \ 64 units each, dropout 0.2\n       - Input: lookback window L=128 time steps, output: 1-step ahead (recursive forecast)\n\
  \       - Fit on train data with 10% validation split for early stopping\n       - Optimizer: Adam, learning_rate=0.001,\
  \ batch_size=16, epochs=100 (or early stop)\n       - Forecast recursively for full test horizon (append predictions, use\
  \ as next input)\n       - Output: point forecasts (1D array)\n\n4. HYPERPARAMETER TUNING FOR WEIGHTING FUNCTION α(Ω)\n\
  \   \n   4a. Validation set split\n       - Split training data: 70% fit (ARIMA/LSTM), 30% validation (tune α)\n       -\
  \ Compute Ω on validation window (same T_w as test)\n   \n   4b. Weighting function candidates\n       - Logistic: α(Ω)\
  \ = 1 / (1 + exp(-a(Ω - b)))\n           Grid: a ∈ [0.1, 1, 5, 10, 50], b ∈ [0.1, 0.3, 0.5, 0.7, 0.9]\n       - Linear:\
  \ α(Ω) = max(0, min(1, c·Ω + d))\n           Grid: c ∈ [-1, 0, 1, 5], d ∈ [-1, 0, 1]\n       - Power-law: α(Ω) = Ω^p for\
  \ p ∈ [0.5, 1, 2, 3]\n       - Non-monotone (neural): 2-layer NN, 32 units, input Ω, output α ∈ [0,1]\n   \n   4c. Optimization\n\
  \       - For each function candidate: blend forecasts as: ŷ = α(Ω)·ŷ_arima + (1-α(Ω))·ŷ_lstm\n       - Compute MSE on validation\
  \ set\n       - Keep best-performing α parameters (minimum validation MSE)\n\n5. TEST-TIME EVALUATION\n   \n   5a. Ensemble\
  \ forecasting\n       - Compute rolling Ω on test window (same T_w used in training)\n       - Apply learned α(Ω) to blend:\
  \ ŷ_blend = α(Ω)·ŷ_arima + (1-α(Ω))·ŷ_lstm\n       - Compute test MSE, RMSE, MAE\n   \n   5b. Baseline comparisons (on same\
  \ test set)\n       - Fixed 0.5/0.5 ensemble: ŷ = 0.5·ŷ_arima + 0.5·ŷ_lstm\n       - Static per-series optimal (convex):\
  \ α* = argmin_α MSE on validation, fixed for test\n       - Error-based dynamic weighting (reactive): α_t = 1 / (1 + |e_arima,t|\
  \ / |e_lstm,t|) using recent validation errors\n       - ARIMA-only\n       - LSTM-only\n   \n   5c. Summary metrics per\
  \ series\n       - MSE, RMSE, MAE for each method (spectral-adaptive, 5 baselines)\n       - Spectral statistics: Ω_train_mean,\
  \ Ω_train_std, Ω_test_mean, Ω_test_std, Ω_regime_shift = |Ω_test_mean - Ω_train_mean|\n       - Relative improvement: Δ_vs_fixed\
  \ = (MSE_fixed - MSE_spectral) / MSE_fixed (positive = spectral wins)\n\n6. AGGREGATED ANALYSIS & STATISTICAL TESTING\n\
  \   \n   6a. Per-domain and overall statistics\n       - For each method: collect all per-series MSE values\n       - Compute:\
  \ mean MSE, std MSE, median MSE, 95% CI via bootstrap (1000 resamples)\n   \n   6b. Paired t-tests\n       - Paired t-test\
  \ (spectral-adaptive vs. fixed 0.5/0.5) on MSE deltas\n       - Bonferroni correction: α = 0.05 / number of tests\n    \
  \   - Report: t-statistic, p-value, effect size (Cohen's d)\n   \n   6c. Regime-shift sensitivity\n       - Stratify series\
  \ by Ω_regime_shift quartiles\n       - Compare spectral-adaptive vs. fixed ensemble separately in each quartile\n     \
  \  - Hypothesis: largest wins in high-shift quartiles (>0.2 Ω change)\n\n7. ABLATION STUDIES (integrated into single run)\n\
  \   \n   7a. Window size ablation\n       - Repeat steps 2-6 for each T_w ∈ {32, 64, 128, 256}\n       - Track: MSE mean/std\
  \ for spectral-adaptive across window sizes\n       - Report: which T_w minimizes MSE?\n   \n   7b. Weighting form comparison\n\
  \       - For each form (logistic, linear, power-law, NN):\n         - Tune on same validation set\n         - Evaluate\
  \ on test set\n         - Report: MSE, comparison table\n   \n   7c. Monotone vs. non-monotone\n       - Implement 2-layer\
  \ NN without monotonicity constraint\n       - Compare test MSE: logistic (constrained monotone) vs. NN (unconstrained)\n\
  \       - Test: does removing monotonicity constraint hurt or help?\n\n8. OUTPUT GENERATION\n   \n   8a. method_out.json\
  \ structure:\n       {\n         \"experiment_summary\": {\n           \"total_series\": N,\n           \"series_with_regime_shift\"\
  : count_gt_0.2,\n           \"compute_time_seconds\": total_time\n         },\n         \"methods\": {\n           \"spectral_adaptive\"\
  : {\"mse\": [...], \"mean\": X, \"std\": Y, \"ci_95\": [L, U]},\n           \"fixed_0.5_0.5\": {...},\n           ...\n\
  \         },\n         \"statistical_tests\": {\n           \"spectral_vs_fixed\": {\"t_stat\": X, \"p_value\": Y, \"cohens_d\"\
  : Z}\n         },\n         \"ablations\": {\n           \"window_size\": {\"32\": X, \"64\": Y, ...},\n           \"weighting_form\"\
  : {\"logistic\": X, \"linear\": Y, ...},\n           \"monotone_vs_nn\": {\"logistic_mse\": X, \"nn_mse\": Y}\n        \
  \ },\n         \"per_series_detailed\": [\n           {\"series_id\": S, \"domain\": D, \"omega_train\": X, \"omega_test\"\
  : Y, \"mse_spectral\": Z, ...},\n           ...\n         ]\n       }\n   \n   8b. Figures (matplotlib + pickle):\n    \
  \   - Fig 1: Rolling Ω time series (train vs. test) for 5 representative series\n       - Fig 2: Learned weighting functions\
  \ α(Ω) for each weighting form\n       - Fig 3: Window size vs. MSE/variance trade-off (line plot + error bars)\n      \
  \ - Fig 4: Weighting form comparison (bar chart: logistic vs. linear vs. power-law vs. NN)\n       - Fig 5: MSE distribution\
  \ by method (box plots, 6 methods side-by-side)\n       - Fig 6: Regime-shift sensitivity (scatter: Ω_shift vs. MSE improvement,\
  \ per series)\n\n9. ERROR HANDLING & FALLBACKS\n   - If auto_arima fails for a series (no convergence): use ExponentialSmoothing\
  \ fallback\n   - If LSTM training diverges: reinitialize, reduce learning_rate to 0.0001\n   - If Ω computation yields NaN\
  \ (e.g., all-zero window): clip Ω to [0.01, 0.99]\n   - If test set too small (<5 points): skip series, log warning\n\n\
  10. COMPUTATIONAL TRACKING\n    - Time spectral computation, ARIMA fit, LSTM fit, ensemble blend per series\n    - Verify\
  \ overhead <5% vs. static ensemble (reported in method_out.json)\n    - Use multiprocessing for independent series (map\
  \ over CPU cores, avoid GPU bottleneck)"
fallback_plan: |-
  FALLBACK 1: Reduced Dataset Scope
    If full 440 series takes >5 hours: sample 100 representative series (stratified by domain, Ω quartile), report as 'validation on representative subset'.

  FALLBACK 2: Simplified ARIMA Fit
    If auto_arima grid search is too slow: use fixed (p=1, d=1, q=1) ARIMA for all series instead. Accept reduced baseline quality; focus on ensemble weighting logic.

  FALLBACK 3: Smaller LSTM
    If LSTM training is slow (>30s per series): reduce to 1 layer × 32 units, epochs=50, batch_size=32. Trade accuracy for speed.

  FALLBACK 4: Single Window Size
    If ablation of 4 window sizes is too slow: use T_w=128 only (most commonly recommended in literature), skip ablation. Report as limitation.

  FALLBACK 5: Simplified Weighting Functions
    If hyperparameter tuning grid is too large: use only logistic α(Ω) with fixed grid a∈[0.1, 1, 10], b∈[0.3, 0.5, 0.7] (27 configs instead of 50). Defer linear/power-law/NN to future work.

  FALLBACK 6: Skip Statistical Testing
    If insufficient time: compute mean/std MSE only, skip Bonferroni-corrected t-tests. Report raw improvement percentages with caveat: 'statistical significance not tested'.

  FALLBACK 7: Minimal Figures
    If plotting is slow: produce 2 key figures (rolling Ω example, MSE distribution by method), defer regime-shift scatter and weighting function curves.

  FALLBACK 8: CPU-Only Execution
    If GPU unavailable or causing driver issues: disable PyTorch GPU, use CPU-based LSTM training (torch.device('cpu')). Will be slower but ensures reproducibility.
testing_plan: |-
  PHASE 1: RAPID SMOKE TEST (15 minutes)
    1. Load 1 representative example from each domain (energy, finance, transportation, weather)
    2. For each series:
       - Compute Ω on 50% of data (quick FFT test)
       - Fit ARIMA with fixed (1,1,1) order (skip auto_arima grid)
       - Train LSTM for 5 epochs only (tiny network)
       - Apply fixed 0.5/0.5 ensemble on remaining 50%
       - Check: output arrays have correct shape, MSE is numeric
    3. Confirm: no crashes, no NaN, output can serialize to JSON
    4. Goal: verify pipeline logic before full run
    5. Success signal: 4 series × 2 methods (ARIMA, LSTM) produce forecasts with MSE ∈ (0, 10^6]

  PHASE 2: MINI DATASET TEST (30 minutes)
    1. Load first 20 series from dataset (stratified: 5 per domain)
    2. Full pipeline: hyperparameter tuning on validation, test evaluation
    3. Compute spectral-adaptive and 3 baselines (fixed 0.5/0.5, error-based, ARIMA-only)
    4. Generate method_out.json and 2 figures (rolling Ω, MSE distribution)
    5. Check:
       - Spectral-adaptive MSE ≤ ARIMA-only and LSTM-only MSE (at least one series)
       - Window size ablation produces variation (not all identical)
       - No serialization errors
    6. Success signal: method_out.json validates against schema, contains >0 series results

  PHASE 3: REGIME-SHIFT STRATIFICATION TEST (10 minutes)
    1. In mini dataset: identify 2 series with high Ω_regime_shift (>0.2) and 2 with low (<0.05)
    2. Verify: MSE improvement (spectral vs. fixed) is larger in high-shift group
    3. Success signal: high-shift Δ_MSE ≥ low-shift Δ_MSE for ≥1 series

  PHASE 4: FULL DATASET EXECUTION (60-90 minutes)
    1. Once mini tests pass, execute on all 440 series
    2. Monitor: print progress every 50 series (elapsed time, ETA)
    3. Checkpoint: save partial method_out.json every 100 series (resumable)
    4. Track: count of skipped series (failures), reasons
    5. Success criteria:
       - Spectral-adaptive achieves ≥3% lower test MSE vs. fixed on ≥60% of series (relaxed from 70%)
       - Paired t-test p-value <0.05 (Bonferroni-corrected)
       - Regime-shift quartile analysis shows expected trend

  FAILURE MODES TO MONITOR
    - auto_arima: no valid model found → fallback to ExponentialSmoothing (counts as 'series_failure')
    - LSTM: NaN loss (exploding gradient) → restart with lower lr (max 2 restarts)
    - Ω computation: constant series (all values identical) → clip to Ω=0.5, log warning
    - Test set: too short (<5 points) → skip series entirely
    - Overall time: if mini test takes >45 min, abort, reduce to 50 series for full run

  CHECKPOINTS FOR PIVOTING
    - After Phase 1: if crashes, debug logging to identify which step fails (FFT? ARIMA? LSTM?)
    - After Phase 2: if spectral-adaptive doesn't beat ≥1 baseline, investigate:
      * Is Ω truly capturing predictability? (Compare to actual errors)
      * Is weighting function α converging? (Plot α vs. Ω scatter)
      * Are ARIMA and LSTM complementary? (Check their errors on same series)
    - After Phase 3: if regime-shift does NOT show expected trend, consider:
      * Ω is computed on test set → recompute on held-out validation
      * Monotonicity assumption is wrong → enable NN weighting
    - If overall >50% series skipped: switch to 50-series subset, accept 'limited validation scope' label
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
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
out_dependency_files:
  file_list:
  - data.py
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json
  data_file_paths:
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json

Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</dependencies>

<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **HARD LIMIT**: Maximum $10 USD total spend on LLM API calls (OpenRouter). Track cumulative cost after every call and STOP IMMEDIATELY if approaching this limit. Never exceed this budget under any circumstances.
</software_constraints>

<skills>
Skills are self-contained capabilities with instructions, context, and tools.

- aii-web-tools: Web search (Serper), page/PDF fetch as markdown, regex grep over page/PDF text
- aii-semscholar-bib: Batch-fetch BibTeX from Semantic Scholar
- aii-openrouter-llms: Search and call 300+ LLMs via OpenRouter
- aii-hf-datasets: Search, preview, download HuggingFace datasets
- aii-owid-datasets: Search and load Our World in Data tables
- aii-lean: Compile/verify Lean 4 code, Mathlib search, tactic suggestions
- aii-image-gen: Generate/edit images via Gemini 3 Pro Image (Nano Banana Pro)
- aii-json: Validate JSON against schemas, generate mini/preview variants
- aii-paper-writing: Academic paper structure, bibliography, citations
- aii-paper-to-latex: Assemble LaTeX papers and compile to PDF
- aii-parallel-computing: GPU acceleration, CPU parallelism, async I/O
- aii-python: Python coding standards for experiment scripts
- aii-use-hardware: Detect CPU/RAM/GPU, memory-safe processing
- aii-long-running-tasks: Gradual scaling pattern for long-running tasks
- aii-colab: Google Colab runtime constraints for notebooks
- aii-file-size-limit: Check and split oversized output files
</skills>
</available_resources>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for framework choices, implementation patterns, agent orchestration.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Use aii-json skill's format script with `--input method_out.json` to generate full, mini, and preview versions. If not in your workspace (see <workspace> above), copy them there. Run 'ls -lh' to verify these three files exist (DO NOT read them).
TODO 2. Apply aii-file-size-limit skill's file size check procedure (100MB limit) to method_out.json and full_method_out.json.
TODO 3. Ensure a `pyproject.toml` exists in your workspace with ALL dependencies pinned to the exact versions installed in your .venv (run `.venv/bin/pip freeze` to get them). This is required for reproducibility. The [project] section must include name, version, requires-python, and a dependencies list with pinned versions (e.g. `numpy==2.0.2`, not `numpy>=2.0`).
</todos>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ExperimentExpectedFiles": {
      "description": "All expected output files from experiment artifact.",
      "properties": {
        "script": {
          "description": "Path to method.py script. Example: 'method.py'",
          "title": "Script",
          "type": "string"
        },
        "full_output": {
          "description": "Full method output JSON file. Example: 'full_method_out.json'",
          "title": "Full Output",
          "type": "string"
        },
        "mini_output": {
          "description": "Mini method output JSON file. Example: 'mini_method_out.json'",
          "title": "Mini Output",
          "type": "string"
        },
        "preview_output": {
          "description": "Preview method output JSON file. Example: 'preview_method_out.json'",
          "title": "Preview Output",
          "type": "string"
        }
      },
      "required": [
        "script",
        "full_output",
        "mini_output",
        "preview_output"
      ],
      "title": "ExperimentExpectedFiles",
      "type": "object"
    }
  },
  "description": "Experiment artifact \u2014 structured output + file metadata.\n\nImplements research methodology with baseline comparison.\nProduces method.py and method_out.json files.",
  "properties": {
    "title": {
      "default": "",
      "description": "Artifact title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters); describe the content, not a status.",
      "maxLength": 90,
      "minLength": 12,
      "title": "Title",
      "type": "string"
    },
    "layman_summary": {
      "default": "",
      "description": "One-sentence plain-language summary of what this artifact does, accessible to non-experts. Used only in the per-artifact README, not in downstream prompts.",
      "maxLength": 250,
      "minLength": 80,
      "title": "Layman Summary",
      "type": "string"
    },
    "summary": {
      "default": "",
      "description": "Summary for downstream artifacts: what this artifact provides",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/ExperimentExpectedFiles",
      "description": "All output files you created. Must include method.py script plus full/mini/preview method output JSON files."
    },
    "upload_ignore_regexes": {
      "description": "Regex patterns for workspace paths that must NOT be published to the GitHub repo, matched against each file's path relative to this artifact's workspace root (POSIX form, e.g. 'cache/abc.json'). Applied ON TOP OF the deploy step's built-in exclusions. Use this for executor-specific caches, large transient intermediates, or content-addressed blob stores (e.g. a cache/ dir of thousands of hash-named files) that would bloat the repo. Examples: ['(^|/)cache/', '(^|/)\\\\.weight_cache/', '(^|/)checkpoints/']. Leave empty if every workspace file should be published.",
      "items": {
        "type": "string"
      },
      "title": "Upload Ignore Regexes",
      "type": "array"
    }
  },
  "required": [
    "out_expected_files"
  ],
  "title": "ExperimentArtifact",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `./.terminal_claude_agent_struct_out.json` exists and contains JSON matching the schema above.
````
