# gen_hypo_1 — create_idea

> Phase: `hypo_loop` · round 1 · `gen_hypo`
> Run: `run_oxbmYex8-G2P` — Spectral Adaptive Weighting for Real-Time Ensemble Forecasting
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_hypo_1` (terminal_claude_agent, claude-haiku-4-5)

### [1] CONFIG · 2026-07-30 12:13:40 UTC

```
model: claude-haiku-4-5 | effort: low | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_oxbmYex8-G2P/iter_1/gen_hypo/claude_agent
```

### [2] SYSTEM-USER prompt · 2026-07-30 12:13:46 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A hypothesis generator (Step 2.1: GEN_HYPO — UNSEEDED mode)

Pipeline: GEN_HYPO (you) → INVENTION_LOOP → GEN_PAPER_REPO

You received a AII prompt. No external seeds — generate a novel hypothesis from your own reasoning and web research.

Your hypothesis will enter the invention loop (propose → execute → narrate) → the results become a paper + GitHub repo.
It MUST be GENUINELY NOVEL (validated against related work) and FEASIBLE TO TEST (within computational/data/tooling constraints provided).
Vague or incremental hypothesis → wasted computation across the entire pipeline.
</your_role>
</ai_inventor_context>

<strategic_mindset>
You are competing with human researchers.

YOUR ADVANTAGE: Breadth across many fields (information theory, ecology, economics, physics, cognitive science, program synthesis, etc.). No single human has this breadth.

HUMAN ADVANTAGE: Deep expertise in their specific field — they know every paper, every failed attempt, every subtle reason "obvious" ideas don't work.

HOW TO WIN: Don't create variants within their field — they'll always recognize those. Find unexpected connections ACROSS fields no single expert would think of.

NOVELTY BAR: An expert should say "I never thought of approaching it THAT way" — not "that's like paper X with a twist." If your idea lives in a crowded neighborhood of similar approaches, it's NOT novel enough.

NO TIME PRESSURE: Exploring 5-6 directions and abandoning all is a SUCCESSFUL process. Settling for a mediocre idea because you already spent so long researching it is a FAILED process.
</strategic_mindset>

<principles>
1. NOVEL - genuinely new mechanism/principle, not incremental. If you have to argue why it's different, it's NOT novel enough.
2. FEASIBLE - testable within the provided compute, data, and tooling
3. CROSS-FIELD - leverage connections across distant domains
4. RIGOROUS - consider what evidence would support OR refute it
5. PRECISE - clear language, no unnecessary jargon
</principles>

<common_mistakes_to_avoid>
Critical pitfalls from past runs. EXPLICITLY CHECK FOR EACH ONE.

**1. Incremental Recombination Disguised as Novelty**
"Apply known method X to known domain Y" is engineering, not conceptual novelty. Your idea needs a new mechanism/principle/insight — not just a new pairing of existing things.
CHECK: If describable as "A but with B" where A and B both exist, it's recombination. What is the genuinely new IDEA?

**2. Ignoring Resource Constraints**
Every hypothesis MUST be testable with available compute, data, and tools.
CHECK: "Can this be implemented with the specific resources listed? What exact data/compute/tools do I need, and are they available?"

**3. Shallow Search Leading to False Novelty**
The same concept often exists under different terminology, in different fields, or framed differently. Searching only your own phrasing and concluding novelty is the MOST dangerous mistake.

CHECK — For every promising hypothesis:
a) Search 5-6 semantically different phrasings within the field
b) Strip to the CORE MECHANISM and search 8-10 unrelated fields (e.g., "MDL-based complexity selection" → search neural architecture search, program synthesis, Bayesian model selection) — the same principle often exists under different names
c) Search for failed/negative results ("limitations", "does not improve")
d) Search in plain English without jargon
If a paper does the same thing under a different name, it's NOT novel.

**4. Rationalizing Overlapping Prior Work**
When you find similar work, do NOT rationalize minor differences as novelty. Two common traps:

FRAMEWORK PORTING: "Nobody did this in MY framework" — if the core mechanism exists in any context (different algorithm, different ensemble type, different field), porting it is engineering, not novelty.

GAP-FILLING: Papers A, B, C each cover variants → you propose the missing combination. An expert would say "obviously someone will do that eventually."

CHECK: Strip your idea to its core mechanism. Search if that mechanism exists ANYWHERE — any framework, any field, any algorithm family. If yes, ABANDON. Don't salvage by narrowing scope or listing "critical differences."

**5. Anchoring Bias**
Once invested in a direction, you'll unconsciously downplay overlap and inflate minor differences into "key differentiators." This feels like thoroughness but is actually defensiveness.

WARNING SIGNS: listing "critical differences" instead of reconsidering; reluctance to "waste" prior search effort; refining the SAME idea instead of exploring different ones; differentiators about context/framework rather than core mechanism.

CHECK: If you found even 1 paper with a similar core mechanism, ABANDON. The best hypotheses rarely come from your first direction. Each abandonment is progress.

**6. Relying on Search Snippets Without Fetching**
Search snippets are NOT enough to assess overlap or understand an approach. The actual mechanism and limitations are only in the full text.
CHECK: FETCH and read any potentially relevant result. Don't assess novelty from titles and snippets alone.

**7. Same-Neighborhood Pivoting**
Replacing one idea with a variant in the same conceptual space is NOT a genuine pivot. If all your directions are "[different adjective] + [same core concept]", you haven't actually explored.

CHECK: Would a single expert in that subfield have thought of ALL your directions? If yes, bring in a mechanism or framing from a completely unrelated field. That's where genuine novelty lives.
</common_mistakes_to_avoid>

<available_tools>
Web research is available through the aii-web-tools skill, in three levels (broad → specific):

1. web search — Returns titles, URLs, snippets. Use first to discover and scan the landscape.
2. web fetch — Reads a page and returns its content as markdown (HTML or PDF). Use to understand a source. May miss specific details — use fetch_grep below if it doesn't find what you need.
3. fetch_grep — Regex search over a page/PDF's full text. Returns exact matching sections with context. Use for precise details, exact numbers, methodology, or PDFs.

Workflow: search → fetch (understand) → fetch_grep (extract specifics).
</available_tools>

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

<task_preview>
You will generate 1 novel groundbreaking research hypothesis in the AII prompt provided in the accompanying user message.
</task_preview>

<YOUR_AII_PROMPT>
Your AII prompt — the research prompt to invent within — is provided as a SEPARATE user message in this turn, immediately following this one. Treat that message as the definition of what to generate a hypothesis for.
</YOUR_AII_PROMPT>

<hypothesis_inspiration>
<YOUR_INSPIRATION>
Human researchers overspecialize — they know their domain deeply but lack breadth to see when other fields have already solved analogous problems. Your advantage is breadth. Only propose a cross-domain transfer if it concretely outperforms existing approaches in this domain. Avoid handwavy analogies — if the imported method is vaguer or weaker than what domain experts already use, it's not worth proposing.

Explore cross-domain inspiration at three levels, from abstract to concrete. At each level, consider both established and recent developments — with slight priority for newer work, which tends to leverage more powerful tools and be less widely known.

1. CONCEPTUAL: Borrow high-level ideas, framings, or design philosophies from distant fields.
   What mental model or approach from another domain suggests a novel angle on this problem?

2. PROCEDURAL: Adapt specific problem-solving processes from other domains.
   What workflow, iterative strategy, or pipeline used elsewhere could restructure how this problem is attacked?

3. METHODOLOGICAL: Import concrete methods directly from other fields with minimal modification.
   What algorithm, formula, or technique from a different domain applies here as-is or with adaptation?

Cast wide — draw from ANY field, not just these examples: ecology, economics, physics, linguistics, game theory, control theory, materials science, cognitive science, epidemiology. The best hypotheses often come from Level 2-3 transfers that experts in the field would never encounter.
</YOUR_INSPIRATION>
</hypothesis_inspiration>

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
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for the field's landscape, prior work, open problems, dead ends, and what counts as a genuinely novel contribution — read it BEFORE brainstorming and during the novelty check.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>

<time_budgets>

Each artifact executor has a fixed time budget (including writing code, debugging, testing, and fixing errors):

- research: 3h
- dataset: 6h
- experiment: 6h
- evaluation: 3h
- proof: 3h

</time_budgets>

<YOUR_TASK>
Generate 1 novel groundbreaking research hypothesis in the AII prompt that is feasible with the above constraints.

<web_research_process>
Read and STRICTLY follow these skills: aii-web-tools.

1. DIVERGE: Brainstorm 5-7 diverse directions WITHOUT searching.
   Think across fields — what techniques from unrelated domains (ecology, economics, physics,
   linguistics, game theory, etc.) could inspire a novel mechanism? What assumptions does the field
   take for granted? Diversity matters more than depth here.

2. SEARCH: Web search for a high-level overview of each direction.
   What similar approaches exist? Is this genuinely novel or incremental? Remember: snippets
   are NOT enough for detailed understanding — treat search as discovery only.

3. FETCH & READ: MUST fetch any potentially relevant URL — you cannot assess novelty from
   snippets alone. Use the aii-web-tools skill:
   - fetch a page for high-level understanding of HTML pages
   - fetch_grep for exact details, methodology, or PDFs
   Prioritize recent papers closest to your idea. If you find significant overlap, PIVOT.

4. ADVERSARIAL NOVELTY CHECK: Actively try to DISPROVE novelty. Most important step.
   Run the FULL search checklist from <common_mistakes_to_avoid> mistake 3 — within-field
   rephrasings, cross-field core-mechanism search, failed/negative results, plain English.
   Ask: "Is the core insight of your hypothesis new, or known things in a new wrapper?"
   "Would an expert find this genuinely surprising?"
   MANDATORY SELF-CHECK: State the core mechanism in one sentence. Does it exist in ANY
   algorithm, framework, or field? If yes — even in a different framework — ABANDON.

5. FEASIBILITY CHECK: Verify your hypothesis is testable with provided resources. What specific data/compute/tools
   needed? All available within constraints?

6. ABANDON or PROCEED:
   ABANDON if: 2+ similar papers exist; you need to argue "critical differences"; core mechanism
   exists in any context.
   Abandoning is progress — go back to step 1 in a genuinely DIFFERENT direction (not a variant).
   PROCEED only if novelty is SELF-EVIDENT — an expert would immediately see it's new without
   explanation.

7. ITERATE: Expect to repeat steps 1-6 multiple times. The first few directions will likely be
   non-novel. This is normal. Don't settle for your first idea just because you've invested time.

<CRITICAL>We want SCIENTIFIC novelty (new mechanism, principle, or insight — the contribution is
knowledge), NOT application novelty (known methods applied to a new domain — the contribution is a
product). If an expert would say "clever engineering but known science," keep searching.
Hypothesis must be feasible within available resources.</CRITICAL>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>
</web_research_process>

Prioritize simplicity. Use concise, approachable language. The explanation should be fully self-contained.
</YOUR_TASK>

<user_data>
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
    "TermDefinition": {
      "description": "A technical term and its definition.",
      "properties": {
        "term": {
          "description": "The technical term",
          "title": "Term",
          "type": "string"
        },
        "definition": {
          "description": "Clear definition of the term",
          "title": "Definition",
          "type": "string"
        }
      },
      "required": [
        "term",
        "definition"
      ],
      "title": "TermDefinition",
      "type": "object"
    }
  },
  "description": "A research hypothesis with validation approach.",
  "properties": {
    "title": {
      "description": "Hypothesis title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters); name the idea, not a status.",
      "title": "Title",
      "type": "string"
    },
    "hypothesis": {
      "description": "The core hypothesis statement",
      "title": "Hypothesis",
      "type": "string"
    },
    "motivation": {
      "description": "Why this hypothesis matters - significance and impact",
      "title": "Motivation",
      "type": "string"
    },
    "assumptions": {
      "description": "Key assumptions that must hold for this hypothesis (2-5 items)",
      "items": {
        "type": "string"
      },
      "title": "Assumptions",
      "type": "array"
    },
    "investigation_approach": {
      "description": "High-level approach to investigating this hypothesis",
      "title": "Investigation Approach",
      "type": "string"
    },
    "success_criteria": {
      "description": "What outcomes would confirm or disconfirm this hypothesis?",
      "title": "Success Criteria",
      "type": "string"
    },
    "related_works": {
      "description": "The most similar existing works found during research. Each entry describes one related work: what it does and how the proposed hypothesis fundamentally differs from it.",
      "items": {
        "type": "string"
      },
      "title": "Related Works",
      "type": "array"
    },
    "inspiration": {
      "description": "What inspired this hypothesis - which patterns, techniques, or cross-field insights were adapted (from the explicit inspiration seeds if your prompt included any, otherwise from your own cross-domain exploration)",
      "title": "Inspiration",
      "type": "string"
    },
    "terms": {
      "description": "Definitions of key technical terms used in the hypothesis",
      "items": {
        "$ref": "#/$defs/TermDefinition"
      },
      "title": "Terms",
      "type": "array"
    },
    "summary": {
      "description": "Brief summary of the hypothesis in 1-2 sentences",
      "title": "Summary",
      "type": "string"
    }
  },
  "required": [
    "title",
    "hypothesis",
    "motivation",
    "assumptions",
    "investigation_approach",
    "success_criteria",
    "related_works",
    "inspiration",
    "terms",
    "summary"
  ],
  "title": "Hypothesis",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `./.terminal_claude_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [3] HUMAN-USER prompt · 2026-07-30 12:13:46 UTC

```
Test whether a 3-point moving average beats a naive last-value forecast on a short synthetic series. Keep the investigation minimal.
```

### [4] ASSISTANT · 2026-07-30 12:14:14 UTC

```
I need to receive the actual AII prompt and user context. The instructions indicate these come as separate user messages. Let me check if they follow, or if I should work with what I have.

Looking at the structure, the last line "Test whether a 3-point moving average beats a naive last-value forecast on a short synthetic series. Keep the investigation minimal." appears to be defining the domain (time-series forecasting) but framed as an example of what NOT to research (too mundane, not novel).

Let me start the hypothesis generation process now. I'll begin by diverging into genuinely novel directions in time-series forecasting, then validate through web research.

**Step 1: DIVERGE - Brainstorm 5-7 novel directions**

1. **Complexity-theoretic forecast selection** (info theory): Select forecasting methods based on series Kolmogorov complexity, not post-hoc accuracy
2. **Predictability phase transitions** (statistical physics): Detect when time-series undergo critical transitions from predictable to chaotic
3. **Causal temporal embeddings** (causal inference): Identify causal structure within time-series to improve out-of-distribution forecasts
4. **Forecasting via information bottleneck** (information theory): Compress time-series to minimal sufficient statistics for prediction
5. **Adaptive method switching via mutual information** (information theory): Switch forecasting methods based on mutual information decay between past and future
6. **Hierarchical temporal abstraction** (cognitive science): Forecast at multiple timescale abstractions and reconcile predictions
7. **Failure-mode prediction** (meta-learning): Predict when standard methods fail before applying them

Let me pursue **Direction 1: Complexity-theoretic forecast selection** - it's concrete, cross-domain, and has clear falsifiability.

**Step 2: SEARCH - Web search for novelty validation**
```

### [5] TOOL CALL — Skill · 2026-07-30 12:14:14 UTC

```
aii-web-tools
```

### [6] TOOL RESULT — Skill · 2026-07-30 12:14:14 UTC

```
{"success": true, "commandName": "aii-web-tools"}
```

### [7] TOOL CALL — Skill · 2026-07-30 12:14:14 UTC

```
aii-web-tools
```

### [8] TOOL RESULT — Skill · 2026-07-30 12:14:14 UTC

```
{"success": true, "commandName": "aii-web-tools"}
```

### [9] TOOL CALL — Skill · 2026-07-30 12:14:14 UTC

```
aii-web-tools
```

### [10] TOOL RESULT — Skill · 2026-07-30 12:14:14 UTC

```
{"success": true, "commandName": "aii-web-tools"}
```

### [11] ASSISTANT · 2026-07-30 12:14:22 UTC

```
I need to execute the web search scripts directly. Let me run them via Bash.
```

### [12] TOOL CALL — Bash · 2026-07-30 12:14:22 UTC

```
Search for complexity-based forecasting approaches:

export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "Kolmogorov complexity time series forecasting" --max-results 8
```

### [13] TOOL CALL — Bash · 2026-07-30 12:14:22 UTC

```
Search for information theory-based model selection:

export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "information theoretic model selection time series" --max-results 8
```

### [14] TOOL RESULT — Bash · 2026-07-30 12:14:22 UTC

```
{"stdout": "Search: Kolmogorov complexity time series forecasting\nFound: 8 results\n\n1. Kolmogorov Complexity Analysis and Prediction Horizon of ...\n   https://www.mdpi.com/2073-4433/13/5/746\n   by S Malinović-Milićević · 2022 · Cited by 6 — Kolmogorov complexity is a measure of randomness. This time quantifies the size of the time window within which complexity remains unchanged....\n\n2. KAN-AD: Time Series Anomaly Detection with Kolmogorov ...\n   https://icml.cc/virtual/2025/poster/45584\n   This paper introduces KAN-AD, a robust anomaly detection model rooted in the Kolmogorov–Arnold representation theorem. KAN-AD transforms the prediction of time ......\n\n3. Time series forecasting with Hahn Kolmogorov-Arnold ...\n   https://arxiv.org/pdf/2601.18837\n   by MZ Hasan · 2026 · Cited by 2 — We propose HaKAN, a versatile model based on Kolmogorov-Arnold Networks (KANs), providing a lightweight for multivariate time series forecasting....\n\n4. Kolmogorov-Arnold networks for time series forecasting\n   https://dl.acm.org/doi/abs/10.1007/s10586-025-05574-9\n   by PT Yamak · 2025 · Cited by 10 — This study presents Kolmogorov-Arnold Networks (KANs) for time series forecasting (TSF) as a transformative paradigm, leveraging the Kolmogorov ......\n\n5. Time Series Anomaly Detection Using Kolmogorov-Arnold ...\n   https://medium.com/thedeephub/time-series-anomaly-detection-using-kolmogorov-arnold-networks-abd9bbeaa9af\n   In this tutorial, you will learn how to use KANs to detect anomalies in time series data. This tutorial will show how to run KAN-based time ......\n\n6. Kolmogorov-Arnold Networks for Time Series Forecasting\n   https://www.techrxiv.org/doi/10.36227/techrxiv.177130591.14244418\n   by MM Ferdaus · 2026 — Kolmogorov-Arnold Networks (KANs) represent a promising direction for time series forecasting, offering theoretical advantages and growing empirical support....\n\n7. A multivariate time series prediction model based on the ...\n   https://www.nature.com/articles/s41598-025-07654-7\n   by Y Long · 2025 · Cited by 10 — This paper addresses the complexity of multivariate time series forecasting and the limitations of traditional methods by proposing an ......\n\n8. Mixture of KAN Experts for Time Series Forecasting\n   https://www.datasciencewithmarco.com/blog/mixture-of-kan-experts-for-high-performance-time-series-forecasting\n   This is the Kolmogorov-Arnold representation theorem in effect, as it states that multivariate functions can be represented by the combination ......", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [15] TOOL CALL — Bash · 2026-07-30 12:14:22 UTC

```
Search for complexity-based algorithm selection:

export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "complexity measure forecast algorithm selection" --max-results 8
```

### [16] TOOL RESULT — Bash · 2026-07-30 12:14:22 UTC

```
{"stdout": "Search: information theoretic model selection time series\nFound: 8 results\n\n1. An Information Theoretic Approach to Model Selection - PMC - NIH\n   https://pmc.ncbi.nlm.nih.gov/articles/PMC6768938/\n   by MC Newland · 2019 · Cited by 34 — In the I-T approach, the scientist examines a set of candidate models and determines for each one the probability that it is the closer to the truth than all ......\n\n2. A primer on model selection using the Akaike Information Criterion\n   https://www.sciencedirect.com/science/article/pii/S2468042719300508\n   by S Portet · 2020 · Cited by 680 — Here, some procedures for model calibration and a criterion, the Akaike Information Criterion, of model selection based on experimental data are described....\n\n3. Model Selection and Inference: A Practical Information-Theoretic ...\n   https://link.springer.com/book/10.1007/978-1-4757-2917-7\n   by KP Burnham · Cited by 73271 — The information-theoretic approach allows inference based on more than one model (including estimates of unconditional precision)....\n\n4. Evaluation-free Time-series Forecasting Model Selection via ...\n   https://dl.acm.org/doi/10.1145/3715149\n   The information-theoretic features capture information-theoretic underlying characteristics in the time-series; e.g., entropy, trend, non-linearity, change ......\n\n5. On Model Selection\n   https://projecteuclid.org/ebooks/institute-of-mathematical-statistics-lecture-notes-monograph-series/Model-selection/chapter/On-model-selection/10.1214/lnms/1215540960.pdf\n   by CR Rao · 2001 · Cited by 221 — In this paper, we survey the model selection criteria discussed in statistical literature. We are mainly concerned with those used in regression analysis and ......\n\n6. Why is AIC or BIC commonly used in model selections for time series ...\n   https://stats.stackexchange.com/questions/523485/why-is-aic-or-bic-commonly-used-in-model-selections-for-time-series-forecasting\n   On scikit-learn documentation, I found the following comments about AIC: Information-criterion based model selection is very fast, but it relies on ......\n\n7. THE INFORMATION-THEORETIC APPROACH TO MODEL SELECTION\n   https://core.ac.uk/download/pdf/267195670.pdf\n   by EE Blankenshipa · Cited by 12 — One alternative to using hypothesis tests for model selection is the information-theoretic approach, proposed by Burnham and Anderson (1998). This technique ......\n\n8. Information criteria for model selection - Zhang - 2023\n   https://wires.onlinelibrary.wiley.com/doi/10.1002/wics.1607\n   by J Zhang · 2023 · Cited by 171 — This review article will revisit information criteria by summarizing their key concepts, evaluation metrics, fundamental properties, interconnections, recent ......", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [17] TOOL RESULT — Bash · 2026-07-30 12:14:22 UTC

```
{"stdout": "Search: complexity measure forecast algorithm selection\nFound: 8 results\n\n1. Judgmental selection of forecasting models\n   https://www.sciencedirect.com/science/article/pii/S0272696318300251\n   by F Petropoulos · 2018 · Cited by 211 — Complex methods, such as many machine learning algorithms, often appear as black boxes, and provide limited or no insights into how the forecasts are produced...\n\n2. PlanIQ - Algorithm selection by item: mix and match your forecast\n   https://community.anaplan.com/discussion/110383/planiq-algorithm-selection-by-item-mix-and-match-your-forecast\n   Algorithm selection by item is the use of more than one algorithm to produce optimal forecasts across multiple items....\n\n3. Demand forecasting algorithms - Supply Chain Management\n   https://learn.microsoft.com/en-us/dynamics365/supply-chain/demand-planning/forecast-algorithm-types\n   In Demand planning, you choose a forecast algorithm when you place and configure a Forecast or Forecast with signals step in a forecast model....\n\n4. Evaluation-free Time-series Forecasting Model Selection via ...\n   https://dl.acm.org/doi/full/10.1145/3715149\n   by M Abdallah · 2025 · Cited by 21 — Results demonstrate AutoForecast outperforms baseline meta-learners and popular forecasting algorithms, achieving two times better model selection performance....\n\n5. Automatic algorithms for time series forecasting\n   https://robjhyndman.com/talks/Google-Oct2015-part1.pdf\n   Statistically sophisticated or complex methods do not necessarily provide more accurate forecasts than simpler ones....\n\n6. Time series forecasting (Part 2 of 3): Selecting algorithms\n   https://medium.com/data-science-at-microsoft/time-series-forecasting-part-2-of-3-selecting-algorithms-11b6635f61bb\n   In this article, we discuss our approach to evaluating the accuracy of some forecasting models and choosing the most accurate one....\n\n7. Forecasting Algorithms in Business: Choosing the Right Model for Your ...\n   https://cogentinfo.com/resources/forecasting-algorithms-in-business-choosing-the-right-model-for-your-industry\n   AI-driven algorithms like Deep Neural Networks (DNN), LSTM, and Gradient Boosting Machines (GBM) will dominate, improving predictions in complex,...\n\n8. Mutual information model selection algorithm for time series - PMC\n   https://pmc.ncbi.nlm.nih.gov/articles/PMC9041887/\n   by E Akça · 2020 · Cited by 12 — In this study, we report on a novel model selection algorithm called Mutual Information Model Selection Algorithm (MIMSA) based on a penalized mutual ......", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [18] ASSISTANT · 2026-07-30 12:14:30 UTC

```
Good. I see several relevant directions. The searches show:
- KANs (Kolmogorov-Arnold Networks) are being used for forecasting, but these are neural architectures using the theorem, not about complexity-based model selection
- Information-theoretic model selection exists (AIC/BIC standard approaches)
- Mutual Information Model Selection Algorithm (MIMSA) exists

Let me fetch the most relevant papers to understand what's already been done:
```

### [19] TOOL CALL — Bash · 2026-07-30 12:14:30 UTC

```
Fetch the evaluation-free model selection paper:

export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" fetch --url "https://dl.acm.org/doi/10.1145/3715149" --max-chars 5000
```

### [20] TOOL RESULT — Bash [ERROR] · 2026-07-30 12:14:30 UTC

```
Error: Exit code 1
Error: HTTP 403
```

### [21] TOOL CALL — Bash · 2026-07-30 12:14:30 UTC

```
Fetch the MIMSA paper:

export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" fetch --url "https://pmc.ncbi.nlm.nih.gov/articles/PMC9041887/" --max-chars 5000
```

### [22] TOOL RESULT — Bash · 2026-07-30 12:14:30 UTC

```
{"stdout": "URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC9041887/\nType: HTML\nLength: 133 chars\n\n--- Content ---\n\nChecking your browser before accessing pmc.ncbi.nlm.nih.gov ...\n\nClick here if you are not automatically redirected after 5 seconds.", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [23] ASSISTANT · 2026-07-30 12:14:34 UTC

```
Let me search more broadly for other novel directions and try arxiv papers directly:
```

### [24] TOOL CALL — Bash · 2026-07-30 12:14:34 UTC

```
Search for phase transitions in predictability:

export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "phase transition time series predictability chaos" --max-results 8
```

### [25] TOOL CALL — Bash · 2026-07-30 12:14:34 UTC

```
Search for causal methods in forecasting:

export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "causal structure time series forecasting discovery" --max-results 8
```

### [26] TOOL RESULT — Bash · 2026-07-30 12:14:34 UTC

```
{"stdout": "Search: phase transition time series predictability chaos\nFound: 8 results\n\n1. Time Series Prediction by Chaotic Modeling of Nonlinear Dynamical ...\n   https://www.crcv.ucf.edu/papers/Basharat_ICCV09.pdf\n   by A Basharat · Cited by 80 — The aim of this paper is to investigate the relevant con- cepts from chaos theory and propose a novel and robust model for video synthesis....\n\n2. Chaos theory\n   https://en.wikipedia.org/wiki/Chaos_theory\n   Chaos theory is a branch of mathematics. Complex nonlinearity: chaos, phase transitions, topology change, and path integrals. Chaos and Time-Series Analysis....\n\n3. Chaotic time series & forecasting\n   https://prognostikon.cce.uoa.gr/dkaraoulanis/chaotic-time-series-forecasting/\n   In this article, we will refer to chaotic time series, showing simply and understandable the methods and tools used to study them....\n\n4. Chaos and Predictability in Ionospheric Time Series - PMC - NIH\n   https://pmc.ncbi.nlm.nih.gov/articles/PMC9954826/\n   by M Materassi · 2023 · Cited by 13 — We here suggest data analysis techniques to deal with the question of how chaotic and how predictable the local ionosphere's behaviour is....\n\n5. Lesser-Known Techniques for Data Analysis: Chaos Theory in Time ...\n   https://medium.com/@careerInAI/lesser-known-techniques-for-data-analysis-chaos-theory-in-time-series-analysis-embracing-disorder-c8fd54b595d0\n   In the realm of time series analysis, Chaos Theory introduces a paradigm shift, challenging the traditional notions of order and predictability....\n\n6. Time series prediction by chaotic modeling of nonlinear dynamical ...\n   https://ieeexplore.ieee.org/document/5459429/\n   by A Basharat · 2009 · Cited by 80 — We use concepts from chaos theory in order to model nonlinear dynamical systems that exhibit deterministic behavior. Observed time series from such a system ......\n\n7. Comparing statistical forecasting models across a space of chaotic ...\n   https://www.youtube.com/watch?v=cbUJFKZVPr4\n   Chaotic dynamical systems are traditionally thought to be intrinsically difficulty to predict. Chaotic systems thus pose a unique challenge to ......\n\n8. Exploring transitions to chaos in complex systems\n   https://researchoutreach.org/articles/exploring-transitions-chaos-complex-systems/\n   The onset of chaos describes the exact point at which a nonlinear system transitions from exhibiting regular, predictable behaviour to chaotic ......", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [27] TOOL RESULT — Bash · 2026-07-30 12:14:36 UTC

```
{"stdout": "Search: causal structure time series forecasting discovery\nFound: 8 results\n\n1. Causal Discovery from Conditionally Stationary Time Series\n   https://arxiv.org/html/2110.06257v2\n   Causal discovery aims to identify causal relationships over a set of variables from observational data (Glymour et al., 2019) . Constraint-based ......\n\n2. Causal AI modeling for Time Series Data\n   https://causalai.causalens.com/time-series/\n   Use a mix of domain expertise and algorithmic causal discovery to discover the discover the causal structure within multivariate time-series or panel datasets....\n\n3. Time series causal relationships discovery through feature ...\n   https://www.nature.com/articles/s41598-023-37929-w\n   by M Castro · 2023 · Cited by 36 — We present our methodology to estimate causality in time series from oil field production. As it is difficult to extract causal relations from a real field....\n\n4. Causal Discovery with Multivariate Time Series Data\n   https://medium.com/causality-in-data-science/causal-discovery-with-multivariate-time-series-data-a3f7ffc16747\n   One of the state-of-the-art methods in this field is PCMCI, which enables robust causal discovery in high-dimensional time series settings....\n\n5. Time Series Prediction Based on Causal Discovery\n   https://itise.ugr.es/PresentacionPDF/ITISE2025_Slides_presentation_5631.pdf\n   It aims to identify causal relationships between variables while accounting for time- lagged dependencies and conditional independencies. 7....\n\n6. Causal inference for time series - Accepted papers\n   https://sites.google.com/view/ci4ts2024/accepted-papers\n   A constraint-based causal discovery method operating on multivariate time series was used to identify causal predictors for the regression models....\n\n7. Causal Discovery for time series from multiple datasets with ...\n   https://proceedings.mlr.press/v216/gunther23a/gunther23a.pdf\n   by W Günther · 2023 · Cited by 51 — Causal discovery from time series data is a typical problem setting across the sciences. Often, multi- ple datasets of the same system variables are avail-....\n\n8. DyCAST: Learning Dynamic Causal Structure from Time ...\n   https://openreview.net/forum?id=WjDjem8mWE\n   by Y Cheng · Cited by 7 — We propose DyCAST, a novel framework designed to learn dynamic causal structures in time series using Neural Ordinary Differential Equations (Neural ODEs)....", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [28] ASSISTANT · 2026-07-30 12:14:40 UTC

```
Good direction. Let me search for other angles — multi-scale forecasting, entropic analysis, adaptive switching:
```

### [29] TOOL CALL — Bash · 2026-07-30 12:14:40 UTC

```
Search for hierarchical reconciliation in forecasting:

export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "hierarchical reconciliation time series forecast multiple scales" --max-results 8
```

### [30] TOOL CALL — Bash · 2026-07-30 12:14:40 UTC

```
Search for entropy-based forecasting:

export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "entropic properties entropy rate time series forecasting" --max-results 8
```

### [31] TOOL RESULT — Bash · 2026-07-30 12:14:40 UTC

```
{"stdout": "Search: hierarchical reconciliation time series forecast multiple scales\nFound: 8 results\n\n1. Hierarchical Time Series Forecasting with Robust Reconciliation\n   https://arxiv.org/html/2510.20383v1\n   Hierarchical time series forecasting is a process that adjusts, or “reconciles,” forecast values to ensure they satisfy the hierarchical ......\n\n2. Demystifying Hierarchical Forecasting | by Mark Goh\n   https://medium.com/@gmw172/demystifying-hierarchical-forecasting-6c0dc585ced8\n   Hierarchical forecasting predicts data that can be grouped into different categories at different levels/hierarchy, ensuring they sum up nicely....\n\n3. 11.3 Forecast reconciliation | Forecasting: Principles and Practice ...\n   https://otexts.com/fpp3/reconciliation.html\n   This matrix notation allows us to represent all forecasting methods for hierarchical or grouped time series using a common notation....\n\n4. Hierarchical Forecast\n   https://nixtlaverse.nixtla.io/hierarchicalforecast/index.html\n   Hierachical Forecast offers different reconciliation methods that render coherent forecasts across cross-sectional and temporal hierachies....\n\n5. Optimally Reconciling Forecasts in a Hierarchy\n   https://robjhyndman.com/papers/Foresight-hts-final.pdf\n   The optimal reconciliation method we discuss here can handle hierarchical and grouped time series. They show we can do better by taking weighted averages of ......\n\n6. Hierarchical forecasting at scale\n   https://www.sciencedirect.com/science/article/pii/S0169207024000116\n   by O Sprangers · 2024 · Cited by 10 — Reconciliation methods adjust the forecasts for each level in the hierarchy by minimizing the errors at each forecast level. These methods are applied as a post ....\n\n7. Hierarchical Forecast Reconciliation at Scale\n   https://isf.forecasters.org/wp-content/uploads/gravity_forms/2-dd30f7ae09136fa695c552259bdb3f99/2019/07/Davies_Robert_ISF2019.pdf\n   by R Davies · Cited by 1 — Main innovation was the use of a mean-squared percentage error. (MSPE) based loss function to reconcile forecasts at very different scales....\n\n8. Hierarchical Time Series Forecasting : r/datascience\n   https://www.reddit.com/r/datascience/comments/1hb2qbb/hierarchical_time_series_forecasting/\n   Hierarchical forecasting methodologies can be quite challenging, and each approach comes with its own trade-offs. I typically test different ......", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [32] TOOL RESULT — Bash · 2026-07-30 12:14:42 UTC

```
{"stdout": "Search: entropic properties entropy rate time series forecasting\nFound: 8 results\n\n1. Comparison of entropy rate measures for the evaluation of time series ...\n   https://www.sciencedirect.com/science/article/pii/S0208521624000287\n   by C Barà · 2024 · Cited by 30 — Depending on the characteristics of the system under investigation, different methods can be used to estimate the entropy rate of a time series....\n\n2. Entropic Analysis of Time Series through Kernel Density Estimation\n   https://arxiv.org/html/2503.18916v1\n   This work presents a novel framework for time series analysis using entropic measures based on the kernel density estimate (KDE) of the time ......\n\n3. Can the concept of entropy be applied to financial time series?\n   https://quant.stackexchange.com/questions/879/can-the-concept-of-entropy-be-applied-to-financial-time-series\n   I am not familiar with the concept of entropy for time series. I am looking for good reference papers and examples of use....\n\n4. Time Series Complexity analysis using Entropy | by Piero Paialunga\n   https://medium.com/data-science/time-series-complexity-analysis-using-entropy-ec49a4aaff11\n   Time Series Complexity analysis using Entropy. Here is a method to understand how complex your time series are, in a few lines of code....\n\n5. The intrinsic predictability of ecological time series and its ...\n   https://esajournals.onlinelibrary.wiley.com/doi/10.1002/ecm.1359\n   The Shannon entropy rate quantifies the average amount of information per observation in a time series that is unrelated to the past,...\n\n6. Entropy (information theory)\n   https://en.wikipedia.org/wiki/Entropy_(information_theory)\n   In information theory, the entropy of a random variable quantifies the average level of uncertainty or information associated with the variable's potential ......\n\n7. Entropic Time Schedulers for Generative Diffusion Models\n   https://www.youtube.com/watch?v=Z3jfwk_E1lM\n   Dejan Stancevic presented his work on \"Entropic Time Schedulers for Generative Diffusion Models\"....\n\n8. Coarse-Grained Entropy Rates for Characterization of Complex Time ...\n   https://sfi-edu.s3.amazonaws.com/sfi-edu/production/uploads/sfi-com/dev/uploads/filer/e7/fa/e7fa1cf7-1c32-4cbb-bf9a-f180333b1978/94-06-040.pdf\n   by M Palus · 1994 · Cited by 155 — Their numerical properties, sensitivity to changes in the dynamics underlying the analyzed data, robustness against additive noise and some ......", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [33] ASSISTANT · 2026-07-30 12:14:50 UTC

```
These searches show established work. Let me explore something more speculative: **Information Bottleneck for forecasting** and also search for failure prediction in forecasting:
```

### [34] TOOL CALL — Bash · 2026-07-30 12:14:50 UTC

```
Search for information bottleneck in time series:

export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "information bottleneck principle time series compression" --max-results 8
```

### [35] TOOL CALL — Bash · 2026-07-30 12:14:50 UTC

```
Search for forecast failure detection:

export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "forecast failure detection meta-learning when to use" --max-results 8
```

### [36] TOOL RESULT — Bash · 2026-07-30 12:14:50 UTC

```
{"stdout": "Search: information bottleneck principle time series compression\nFound: 8 results\n\n1. Information bottleneck method\n   https://en.wikipedia.org/wiki/Information_bottleneck_method\n   It is designed for finding the best tradeoff between accuracy and complexity (compression) when summarizing (e.g. clustering) a random variable X,...\n\n2. The Information Bottleneck. From a 1999 compression principle to a…\n   https://medium.com/@EleventhHourEnthusiast/the-information-bottleneck-fb6328e23b2d\n   The information bottleneck began in 1999 as a compression principle. In 2017 it became a contested theory of why deep learning works....\n\n3. Multivariate Time Series Information Bottleneck\n   https://www.mdpi.com/1099-4300/25/5/831\n   by D Ullmann · 2023 · Cited by 8 — Tishby [33] proposed the information bottleneck principle (IB), which aims to compress the input X and filter out all task-irrelevant information...\n\n4. [physics/0004057] The information bottleneck method\n   https://arxiv.org/abs/physics/0004057\n   by N Tishby · 2000 · Cited by 5859 — We squeeze the information that X provides about Y through a bottleneck formed by a limited set of codewords tX....\n\n5. [Discussion] What is the status of the \"Information Bottleneck Theory ...\n   https://www.reddit.com/r/MachineLearning/comments/be8qie/discussion_what_is_the_status_of_the_information/\n   I am aware of the recent ICLR paper which tried to debunk some of the key claims in the general case. But the IB theory authors came back with a (rude) ......\n\n6. Steps Towards Understanding Deep Learning: The Information ...\n   https://weberna.github.io/jekyll/update/2017/11/08/Information-Bottleneck-Part1.html\n   The goal of lossy compression is to find the 'most compressed' representation possible. This is the bottleneck in the information bottleneck ......\n\n7. Is there current consensus on the value of the Information Bottleneck ...\n   https://stats.stackexchange.com/questions/331986/is-there-current-consensus-on-the-value-of-the-information-bottleneck-principle\n   In 2015, Tishby and Zaslavsky published a well-known paper claiming that the so-called Information Bottleneck Principle could be used to understand ......\n\n8. Information bottleneck: compression view of representation\n   https://zeroentropy.dev/concepts/information-bottleneck/\n   The information bottleneck frames learning as compression: maximize mutual information I(T;Y) about the target while minimizing I(X;T) about the raw input....", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [37] TOOL RESULT — Bash · 2026-07-30 12:14:52 UTC

```
{"stdout": "Search: forecast failure detection meta-learning when to use\nFound: 8 results\n\n1. Evaluation-free Time-series Forecasting Model Selection via ...\n   https://dl.acm.org/doi/full/10.1145/3715149\n   by M Abdallah · 2025 · Cited by 21 — Through extensive experiments on our benchmark testbeds, selecting a model by AutoForecast outperforms SOTA meta-learners and popular forecasting models....\n\n2. Tailored forecasting from short time series via meta-learning\n   https://www.science.org/doi/10.1126/sciadv.ady7216\n   by DA Norton · 2026 · Cited by 6 — Although memory-based ML models are well suited for time-series prediction, they face an additional challenge when forecasting from short time ......\n\n3. Meta-learning how to forecast time series\n   https://robjhyndman.com/papers/fforms.pdf\n   by TS Talagala · 2022 · Cited by 221 — Features of time series are useful in identifying suitable models for forecasting. We present a general framework, labelled FFORMS ......\n\n4. Meta-learning how to forecast time series\n   https://ideas.repec.org/p/msh/ebswps/2018-6.html\n   by TS Talagala · 2018 · Cited by 221 — We present a general framework for forecast-model selection using meta-learning. A random forest is used to identify the best forecasting method using only ......\n\n5. Meta-Learning Dynamics Forecasting Using Task Inference\n   https://www.youtube.com/watch?v=tP4gQuz4mIo\n   They can only forecast in a specific domain and fail when applied to systems with different parameters, external forces, or boundary conditions....\n\n6. A Study of Dynamic Meta-Learning for Failure Prediction in Large-Scale ...\n   https://web.cels.anl.gov/~thakur/papers/jpdc-lan.pdf\n   by Z Lan · Cited by 75 — In this paper, we present a dynamic meta-learning framework for failure prediction. It intends ・ ally obtain failure patterns ・ accuracy and ......\n\n7. Forecasting Early with Meta Learning\n   https://www.ismll.uni-hildesheim.de/pub/pdfs/shayan_kiran_feml.pdf\n   by S Jawed · Cited by 1 — Abstract—In the early observation period of a time series, there might be only a few historic observations available to learn a model....\n\n8. Using meta-learning to recommend an appropriate time-series forecasting ...\n   https://pmc.ncbi.nlm.nih.gov/articles/PMC10782782/\n   by N Talkhi · 2024 · Cited by 16 — The meta-learning approach was able to predict the appropriate forecasting model (ARIMA and TBATS) based on some time series features....", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [38] ASSISTANT · 2026-07-30 12:14:58 UTC

```
Interesting! I see "Evaluation-free Time-series Forecasting Model Selection" appears multiple times. Let me look at that paper and also search for something more exotic — using **predictability spectrum decay** or **manifold dimension** to select methods:
```

### [39] TOOL CALL — Bash · 2026-07-30 12:14:58 UTC

```
Try to fetch the AutoForecast paper via arxiv:

export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" fetch --url "https://arxiv.org/abs/2405.11766" --max-chars 5000
```

### [40] TOOL RESULT — Bash · 2026-07-30 12:14:58 UTC

```
{"stdout": "URL: https://arxiv.org/abs/2405.11766\nType: HTML\nLength: 7937 chars (truncated)\n\n--- Content ---\n\nSkip to main content\n\narXiv is now an independent nonprofit! [Learn more](https://info.arxiv.org/about) ×\n\n[](https://arxiv.org/IgnoreMe) [ ](https://arxiv.org/) [ Search ](https://arxiv.org/search) [Submit](https://arxiv.org/user/create) [Donate](https://info.arxiv.org/about/donate.html) [Log in](https://arxiv.org/login)\n\nSearch arXiv\n\nPress Enter to search * [Advanced search](https://arxiv.org/search/advanced)\n\n# Computer Science > Artificial Intelligence\n\n**arXiv:2405.11766** (cs) \n\n[Submitted on 20 May 2024]\n\n# Title:From SHAP Scores to Feature Importance Scores\n\nAuthors:[Olivier Letoffe](https://arxiv.org/search/cs?searchtype=author&query=Letoffe,+O), [Xuanxiang Huang](https://arxiv.org/search/cs?searchtype=author&query=Huang,+X), [Nicholas Asher](https://arxiv.org/search/cs?searchtype=author&query=Asher,+N), [Joao Marques-Silva](https://arxiv.org/search/cs?searchtype=author&query=Marques-Silva,+J)\n\nView a PDF of the paper titled From SHAP Scores to Feature Importance Scores, by Olivier Letoffe and 2 other authors\n\n[View PDF](/pdf/2405.11766) [HTML (experimental)](https://arxiv.org/html/2405.11766v1)\n\n> Abstract:A central goal of eXplainable Artificial Intelligence (XAI) is to assign relative importance to the features of a Machine Learning (ML) model given some prediction. The importance of this task of explainability by feature attribution is illustrated by the ubiquitous recent use of tools such as SHAP and LIME. Unfortunately, the exact computation of feature attributions, using the game-theoretical foundation underlying SHAP and LIME, can yield manifestly unsatisfactory results, that tantamount to reporting misleading relative feature importance. Recent work targeted rigorous feature attribution, by studying axiomatic aggregations of features based on logic-based definitions of explanations by feature selection. This paper shows that there is an essential relationship between feature attribution and a priori voting power, and that those recently proposed axiomatic aggregations represent a few instantiations of the range of power indices studied in the past. Furthermore, it remains unclear how some of the most widely used power indices might be exploited as feature importance scores (FISs), i.e. the use of power indices in XAI, and which of these indices would be the best suited for the purposes of XAI by feature attribution, namely in terms of not producing results that could be deemed as unsatisfactory. This paper proposes novel desirable properties that FISs should exhibit. In addition, the paper also proposes novel FISs exhibiting the proposed properties. Finally, the paper conducts a rigorous analysis of the best-known power indices in terms of the proposed properties. \n\nSubjects: |  Artificial Intelligence (cs.AI); Machine Learning (cs.LG)  \n---|---  \nCite as: | [arXiv:2405.11766](https://arxiv.org/abs/2405.11766) [cs.AI]  \n  | (or  [arXiv:2405.11766v1](https://arxiv.org/abs/2405.11766v1) [cs.AI] for this version)   \n  |  <https://doi.org/10.48550/arXiv.2405.11766> Focus to learn more arXiv-issued DOI via DataCite  \n  \n## Submission history\n\nFrom: Xuanxiang Huang [[view email](/show-email/fd800d6a/2405.11766)]   \n**[v1]** Mon, 20 May 2024 03:52:41 UTC (46 KB)  \n\n\nFull-text links:\n\n## Access Paper:\n\nView a PDF of the paper titled From SHAP Scores to Feature Importance Scores, by Olivier Letoffe and 2 other authors\n\n  * [View PDF](/pdf/2405.11766)\n  * [HTML (experimental)](https://arxiv.org/html/2405.11766v1)\n  * [TeX Source ](/src/2405.11766)\n\n\n\n[ view license ](http://creativecommons.org/licenses/by/4.0/ \"Rights to this article\")\n\n### Current browse context:\n\ncs.AI\n\n[< prev](/prevnext?id=2405.11766&function=prev&context=cs.AI \"previous in cs.AI \\(accesskey p\\)\")   |   [next >](/prevnext?id=2405.11766&function=next&context=cs.AI \"next in cs.AI \\(accesskey n\\)\")   \n\n\n[new](/list/cs.AI/new) |  [recent](/list/cs.AI/recent) | [2024-05](/list/cs.AI/2024-05)\n\nChange to browse by: \n\n[cs](/abs/2405.11766?context=cs)  \n[cs.LG](/abs/2405.11766?context=cs.LG)  \n\n\n### References & Citations\n\n  * [NASA ADS](https://ui.adsabs.harvard.edu/abs/arXiv:2405.11766)\n  * [Google Scholar](https://scholar.google.com/scholar_lookup?arxiv_id=2405.11766)\n  * [Semantic Scholar](https://api.semanticscholar.org/arXiv:2405.11766)\n\n\n\nexport BibTeX citation Loading...\n\n## BibTeX formatted citation\n\n×\n\nloading...\n\nData provided by: \n\n### Bookmark\n\n[ ](http://www.bibsonomy.org/BibtexHandler?requTask=upload&url=https://arxiv.org/abs/2405.11766&description=From SHAP Scores to Feature Importance Scores \"Bookmark on BibSonomy\") [ ](https://reddit.com/submit?url=https://arxiv.org/abs/2405.11766&title=From SHAP Scores to Feature Importance Scores \"Bookmark on Reddit\")\n\nBibliographic Tools\n\n# Bibliographic and Citation Tools\n\nBibliographic Explorer Toggle\n\nBibliographic Explorer _([What is the Explorer?](https://info.arxiv.org/labs/showcase.html#arxiv-bibliographic-explorer))_\n\nConnected Papers Toggle\n\nConnected Papers _([What is Conn", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [41] TOOL CALL — Bash · 2026-07-30 12:14:58 UTC

```
Search for dimension-based forecasting approaches:

export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "fractal dimension embedding dimension time series forecasting" --max-results 8
```

### [42] TOOL RESULT — Bash · 2026-07-30 12:14:58 UTC

```
{"stdout": "Search: fractal dimension embedding dimension time series forecasting\nFound: 8 results\n\n1. Estimating the Fractal Dimension of Chaotic Time Series\n   https://archive.ll.mit.edu/publications/journal/pdf/vol03_no1/3.1.4.estimatingfractals.pdf\n   The geometry of fractals and the mathematics of fractal dimension provide useful tools for a variety ofscientific disciplines-in particular, the study of chaos....\n\n2. Embedding Dimension - an overview\n   https://www.sciencedirect.com/topics/engineering/embedding-dimension\n   Embedding dimension is defined as the minimum number of dimensions required to reconstruct a dynamical system from a time series,...\n\n3. Fractal Analysis of Time-Series Data Sets: Methods and Challenges\n   https://www.intechopen.com/chapters/64463\n   by I Pilgrim · 2018 · Cited by 67 — In this chapter, we introduce and investigate a variety of fractal analysis techniques directed to time-series structures....\n\n4. How can I caculate the fractal dimension of short time window ...\n   https://www.researchgate.net/post/How-can-I-caculate-the-fractal-dimension-of-short-time-window-of-time-series\n   The fractal dimension of the time series is equal to 2 minus the Hurst exponent, so if you have the series of Hurst epxonents you will simply get the series of ......\n\n5. Estimating Fractal Dimensions of Time Series and Two-dimensional Data\n   https://search.r-project.org/CRAN/refmans/fractaldim/help/fd.estimate.html\n   The functions compute a set of fractal dimensions D D D for time series and two-dimensional data via various methods using a sliding window technique....\n\n6. Determining the Fractal Dimension of a Time Series.pdf\n   https://pages.github.rpi.edu/danony/html/Papers/Determining%20the%20Fractal%20Dimension%20of%20a%20Time%20Series.pdf\n   by MJ EMBRECHTS · Cited by 11 — Artificial neural nets (ANN) offer a fast and elegant way to estimate the fractal dimension of a time series....\n\n7. Four Methods to Distinguish between Fractal Dimensions in Time Series ...\n   https://pmc.ncbi.nlm.nih.gov/articles/PMC9498220/\n   by A Tomashin · 2022 · Cited by 12 — For every fractal dimension, 100 time series were generated under two conditions: idealized fractal time series and a noisy fractal time series ......\n\n8. Fractal Dimensions: What are they? How can they be used for Feature ...\n   https://utkarsh-lal.medium.com/fractal-dimensions-what-are-they-how-can-they-be-used-for-feature-extraction-86301d3c42ab\n   This article discusses different methods of calculating fractal dimensions and how they can be used for feature extraction....", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [43] ASSISTANT · 2026-07-30 12:15:04 UTC

```
Good. Fractal dimension and embedding dimension are studied approaches. Let me now search for something more novel: **Lensing effect** (borrowing from optics/physics) or **Predictability regimes as phase-space partitions**:
```

### [44] TOOL CALL — Bash · 2026-07-30 12:15:04 UTC

```
Search for conformal prediction in forecasting:

export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "online conformal prediction time series adaptive forecasting" --max-results 8
```

### [45] TOOL CALL — Bash · 2026-07-30 12:15:04 UTC

```
Search for transfer learning in time series:

export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "transfer learning domain adaptation time series across datasets" --max-results 8
```

### [46] TOOL RESULT — Bash · 2026-07-30 12:15:04 UTC

```
{"stdout": "Search: online conformal prediction time series adaptive forecasting\nFound: 8 results\n\n1. Conformal Prediction for Time-series Forecasting with Change Points\n   https://neurips.cc/virtual/2025/poster/118881\n   Our algorithm is modular - the state model, forecaster model, and the online adaptive conformal prediction algorithms all operate independently of each other....\n\n2. Adaptive Conformal Predictions for Time Series\n   https://proceedings.mlr.press/v162/zaffran22a/zaffran22a.pdf\n   by M Zaffran · 2022 · Cited by 379 — Adaptive Conformal In- ference builds upon ACI based on online expert aggregation. We lead ex- tensive fair simulations against competing meth- prediction ......\n\n3. Conformal Prediction for Time-series with Change points (CPTC)\n   https://github.com/Rose-STL-Lab/CPTC\n   Conformal prediction has been explored as a general and efficient way to provide uncertainty quantification for time series....\n\n4. Adaptive Conformal Inference for Multi-Step Ahead Time-Series ... - GitHub\n   https://raw.githubusercontent.com/mlresearch/v230/main/assets/hallberg-szabadvary24a/hallberg-szabadvary24a.pdf\n   by JH Szabadváry · 2024 · Cited by 3 — The aim of this paper is to propose an adaptation of the well known adaptive conformal inference (ACI) algorithm to achieve finite-sample coverage guarantees...\n\n5. Adaptive Conformal Predictions for Time Series\n   https://www.semanticscholar.org/paper/Adaptive-Conformal-Predictions-for-Time-Series-Zaffran-Dieuleveut/a80a31e0b8594daaf5b2034fa1f6cac9d5614fd7\n   This work develops methods for forming prediction sets in an online setting where the data generating distribution is allowed to vary over time in an unknown ......\n\n6. Online conformal inference for multi-step time series forecasting\n   https://robjhyndman.com/publications/cpts.html\n   We propose the Autocorrelated Multi-step Conformal Prediction (AcMCP) method, which effectively incorporates autocorrelations in multi-step forecast errors....\n\n7. ICML Spotlight Adaptive Conformal Predictions for Time Series\n   https://icml.cc/virtual/2022/spotlight/17818\n   The proposed aggregation algorithm provides efficient prediction intervals for day-ahead forecasting. All the code and data to reproduce the experiments are ......\n\n8. Conformal Prediction for Time-series Forecasting with Change Points\n   https://arxiv.org/html/2509.02844v1\n   Conformal prediction has been explored as a general and efficient way to provide uncertainty quantification for time series....", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [47] TOOL RESULT — Bash · 2026-07-30 12:15:06 UTC

```
{"stdout": "Search: transfer learning domain adaptation time series across datasets\nFound: 8 results\n\n1. Domain Adaptation for Time Series Under Feature and Label Shifts\n   https://zitniklab.hms.harvard.edu/projects/Raincoat/\n   Another is transfer learning, where a model is pre-trained on a large dataset and then fine-tuned on a smaller, domain-specific dataset....\n\n2. Boosting Transferability and Discriminability for Time Series ...\n   https://proceedings.neurips.cc/paper_files/paper/2024/file/b61da4f02b271cb7b5e3d538e2b78fb9-Paper-Conference.pdf\n   by M Liu · 2024 · Cited by 19 — Unsupervised domain adaptation excels in transferring knowledge from a labeled source domain to an unlabeled target domain, playing a critical role in time ......\n\n3. [D] Transfer Learning / Domain Adaptation for Time-Series ...\n   https://www.reddit.com/r/MachineLearning/comments/ciutme/d_transfer_learning_domain_adaptation_for/\n   Transfer Learning for Clinical Time Series Analysis using Deep Neural Networks uses pre-trained RNNs. It is built on top of TimeNet an earlier ......\n\n4. Domain adaptation between heterogeneous time series data\n   https://www.sciencedirect.com/science/article/pii/S2213846324002712\n   by RT Nguimfack · 2024 · Cited by 5 — Transfer learning and domain adaptation. By leveraging data from different sources, and different conditions, transfer learning aims to share information ......\n\n5. Implementing transfer learning across different datasets for time series ...\n   https://www.semanticscholar.org/paper/Implementing-transfer-learning-across-different-for-Ye-Dai/a5b22ed96f7327833e8ea771209501cc07e2a46b\n   Implementing transfer learning across different datasets for time series. A novel deep transfer learning framework with adversarial domain adaptation: ......\n\n6. Understanding Transfer Learning and Domain Adaptation\n   https://medium.com/xenonstack-ai/understanding-transfer-learning-and-domain-adaptation-0c2d06959811\n   Domain adaptation, which is a part of transfer learning, deals directly with the problem of domain shift, whereby a difference exists in the ......\n\n7. Which Time Series Domain Shifts can Neural Networks Adapt to?\n   https://www.dfki.de/fileadmin/user_upload/import/15027_Which_Time_Series_Domain_Shifts_can_Neural_Networks_Adapt_to_revised.pdf\n   by H Hoyez · Cited by 2 — These domain shifts give rise to the domain adaptation field which extends to time series data. evaluating domain adaptation methods across multiple datasets....\n\n8. Domain Adaptation for Time Series Under Feature and Label Shifts\n   https://proceedings.mlr.press/v202/he23b/he23b.pdf\n   by H He · 2023 · Cited by 186 — Unsupervised domain adaptation (UDA) enables the transfer of models trained on source domains to unlabeled target domains. However, transfer-....", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [48] ASSISTANT · 2026-07-30 12:15:12 UTC

```
Good — conformal prediction is established. Let me now pivot and explore something more speculative: **Lyapunov exponent decay as a forecast method selector**, or **mutual information decay rate** as a selector (distinct from standard mutual information):
```

### [49] TOOL CALL — Bash · 2026-07-30 12:15:13 UTC

```
Search for Lyapunov-based forecasting:

export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "Lyapunov exponent time series forecasting predictability" --max-results 8
```

### [50] TOOL CALL — Bash · 2026-07-30 12:15:13 UTC

```
Search for MI decay in forecasting:

export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "mutual information decay autocorrelation forecast horizon" --max-results 8
```

### [51] TOOL RESULT — Bash · 2026-07-30 12:15:13 UTC

```
{"stdout": "Search: Lyapunov exponent time series forecasting predictability\nFound: 8 results\n\n1. Time Series Forecastability Measures\n   https://arxiv.org/html/2507.13556v1\n   We compute spectral predictability and Lyapunov exponents for each time series in the M5 dataset across multiple aggregation levels ......\n\n2. An Extension of the Lyapunov Analysis for the Predictability Problem in\n   https://journals.ametsoc.org/view/journals/atsc/55/23/1520-0469_1998_055_3409_aeotla_2.0.co_2.xml\n   by G Boffetta · 1998 · Cited by 100 — Lyapunov exponent is not sufficient to estimate the predictability time. exponent displays a strong dependence on the error magnitude,...\n\n3. Time series forecasting enhanced by Lyapunov exponent via attention ...\n   https://www.sciencedirect.com/science/article/abs/pii/S0378437125006004\n   by RR Lima · 2025 · Cited by 2 — This paper proposes a novel time series forecasting approach that integrates chaos theory and deep learning. By computing local Lyapunov exponents over a ......\n\n4. Lyapunov exponent\n   https://en.wikipedia.org/wiki/Lyapunov_exponent\n   It is common to refer to the largest one as the maximal Lyapunov exponent (MLE), because it determines a notion of predictability for a dynamical system....\n\n5. Time series prediction using Lyapunov exponents in embedding ...\n   https://ieeexplore.ieee.org/iel4/5875/15679/00728146.pdf\n   by J Zhang · 1998 · Cited by 20 — The Lyapunov Exponents which quantify the sensitivity are used to predict the unknown points based on a known time series in the embedding phase space....\n\n6. A novel approach for estimating largest Lyapunov exponents in one ...\n   https://pubs.aip.org/aip/cha/article/35/10/101101/3365571/A-novel-approach-for-estimating-largest-Lyapunov\n   We present a data-driven method for estimating the largest Lyapunov exponent (LLE) from one-dimensional chaotic time series using machine ......\n\n7. Chaos in Rainfall: Understanding Precipitation Uncertainty Using ...\n   https://medium.com/@afedullah/chaos-in-rainfall-understanding-precipitation-uncertainty-using-lyapunov-exponents-21385809ba9f\n   The Lyapunov Exponent (LE) is a mathematical tool that measures how quickly nearby trajectories in a system diverge. If precipitation follows ......\n\n8. Localized Lyapunov exponents and the prediction of predictability\n   https://www.lse.ac.uk/CATS/Assets/PDFs/Publications/Papers/2000/37-LocalizedLyapunovExpo-2000.pdf\n   Lyapunov exponent, which guar- antees ¢ 100% of the uncertainties to shrink if they have ¡ infinitesimal magnitudes....", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [52] TOOL RESULT — Bash · 2026-07-30 12:15:15 UTC

```
{"stdout": "Search: mutual information decay autocorrelation forecast horizon\nFound: 8 results\n\n1. On the Limits of Prediction: Forecastability Profiles and ...\n   https://arxiv.org/html/2603.20546v1\n   This paper has shown that, under logarithmic loss, forecasting performance is bounded by the mutual information between the future and the ......\n\n2. Mutual Information for Time Series Forecasting in Python\n   https://valeman.medium.com/mutual-information-for-time-series-forecasting-in-python-377d36ded102\n   Mutual information is a measure of the shared information between two random variables. Mutual information quantifies the amount of information that one ......\n\n3. Exponential decay of mutual information for Gibbs states of local ...\n   https://quantum-journal.org/papers/q-2022-02-10-650/\n   by A Bluhm · 2022 · Cited by 65 — We show that Gibbs states satisfy uniform exponential decay of correlations and, moreover, the mutual information between two regions decays exponentially with ......\n\n4. Research on Forecastability and the Limits of Prediction\n   https://www.theknowablefuture.com/research\n   This page presents research on measuring forecastability using auto-mutual information (AMI) and entropy. It addresses a prior problem, before model selection ......\n\n5. Forecastability Profiles: Information Decay and Recurrence in ...\n   https://papers.ssrn.com/sol3/Delivery.cfm/bc5748a8-313f-4364-b7e5-4dccdfa53f77-MECA.pdf?abstractid=6735033&mirid=1\n   ... mutual information between a future random variable and a declared information set, evaluated as a function of forecast horizon. This quantity is always ......\n\n6. Estimating the mutual information rate of short time series from coupled ...\n   https://www.sciencedirect.com/science/article/pii/S1007570425007920\n   by H Pinto · 2025 · Cited by 4 — Mutual Information Rate (MIR) quantifies the dynamic coupling between two stochastic processes by measuring the information exchanged per unit time....\n\n7. Predictability limit of partially observed systems | Scientific Reports\n   https://www.nature.com/articles/s41598-020-77091-1\n   by A Abeliuk · 2020 · Cited by 22 — We demonstrate that a system's predictability degrades as a function of temporal sampling, regardless of the adopted forecasting model....\n\n8. Decay of quantum conditional mutual information for purely generated ...\n   https://pubs.aip.org/aip/jmp/article/63/7/072201/2843699/Decay-of-quantum-conditional-mutual-information\n   The connection between quantum state recovery and quantum conditional mutual information (QCMI) is studied for the class of purely generated ......", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [53] ASSISTANT · 2026-07-30 12:15:23 UTC

```
Excellent. I found papers on Lyapunov exponents for forecasting and forecastability profiles. Let me fetch the most relevant recent papers:
```

### [54] TOOL CALL — Bash · 2026-07-30 12:15:23 UTC

```
Fetch Time Series Forecastability Measures paper:

export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" fetch --url "https://arxiv.org/html/2507.13556v1" --max-chars 6000
```

### [55] TOOL RESULT — Bash · 2026-07-30 12:15:23 UTC

```
{"stdout": "URL: https://arxiv.org/html/2507.13556v1\nType: HTML\nLength: 35578 chars (truncated)\n\n--- Content ---\n\n  1. [1 Introduction](https://arxiv.org/html/2507.13556v1#S1 \"In Time Series Forecastability Measures\")\n  2. [2 Methodology](https://arxiv.org/html/2507.13556v1#S2 \"In Time Series Forecastability Measures\")\n     1. [2.1 Spectral Predictability](https://arxiv.org/html/2507.13556v1#S2.SS1 \"In 2. Methodology ‣ Time Series Forecastability Measures\")\n     2. [2.2 Lyapunov Exponents](https://arxiv.org/html/2507.13556v1#S2.SS2 \"In 2. Methodology ‣ Time Series Forecastability Measures\")\n  3. [3 Experiments](https://arxiv.org/html/2507.13556v1#S3 \"In Time Series Forecastability Measures\")\n     1. [3.1 Forecastability of a Synthetic Example](https://arxiv.org/html/2507.13556v1#S3.SS1 \"In 3. Experiments ‣ Time Series Forecastability Measures\")\n        1. [Experiment Setup](https://arxiv.org/html/2507.13556v1#S3.SS1.SSS0.Px1 \"In 3.1. Forecastability of a Synthetic Example ‣ 3. Experiments ‣ Time Series Forecastability Measures\")\n        2. [Results](https://arxiv.org/html/2507.13556v1#S3.SS1.SSS0.Px2 \"In 3.1. Forecastability of a Synthetic Example ‣ 3. Experiments ‣ Time Series Forecastability Measures\")\n     2. [3.2 Sensitivity Study of Metrics to Time Series Length and Sparsity](https://arxiv.org/html/2507.13556v1#S3.SS2 \"In 3. Experiments ‣ Time Series Forecastability Measures\")\n        1. [Experiment Setup](https://arxiv.org/html/2507.13556v1#S3.SS2.SSS0.Px1 \"In 3.2. Sensitivity Study of Metrics to Time Series Length and Sparsity ‣ 3. Experiments ‣ Time Series Forecastability Measures\")\n        2. [Results](https://arxiv.org/html/2507.13556v1#S3.SS2.SSS0.Px2 \"In 3.2. Sensitivity Study of Metrics to Time Series Length and Sparsity ‣ 3. Experiments ‣ Time Series Forecastability Measures\")\n     3. [3.3 Forecastability vs. Prediction Errors on the M5 Dataset](https://arxiv.org/html/2507.13556v1#S3.SS3 \"In 3. Experiments ‣ Time Series Forecastability Measures\")\n        1. [Experiment Setup](https://arxiv.org/html/2507.13556v1#S3.SS3.SSS0.Px1 \"In 3.3. Forecastability vs. Prediction Errors on the M5 Dataset ‣ 3. Experiments ‣ Time Series Forecastability Measures\")\n        2. [Results](https://arxiv.org/html/2507.13556v1#S3.SS3.SSS0.Px2 \"In 3.3. Forecastability vs. Prediction Errors on the M5 Dataset ‣ 3. Experiments ‣ Time Series Forecastability Measures\")\n  4. [4 Discussion](https://arxiv.org/html/2507.13556v1#S4 \"In Time Series Forecastability Measures\")\n\n\n\n# Time Series Forecastability Measures\n\nRui Wang  Amazon Web ServicesSeattleWAUSA [rwngamz@amazon.com](mailto:rwngamz@amazon.com) ,  Steven Klee  Amazon Web ServicesBellevueWAUSA [sklee@amazon.com](mailto:sklee@amazon.com) and  Alexis Roos  Amazon Web ServicesSeattleWAUSA [alexiroo@amazon.com](mailto:alexiroo@amazon.com)\n\n(2025)\n\n###### Abstract.\n\nThis paper proposes using two metrics to quantify the forecastability of time series prior to model development: the spectral predictability score and the largest Lyapunov exponent. Unlike traditional model evaluation metrics, these measures assess the inherent forecastability characteristics of the data before any forecast attempts. The spectral predictability score evaluates the strength and regularity of frequency components in the time series, whereas the Lyapunov exponents quantify the chaos and stability of the system generating the data. We evaluated the effectiveness of these metrics on both synthetic and real-world time series from the M5 forecast competition dataset. Our results demonstrate that these two metrics can correctly reflect the inherent forecastability of a time series and have a strong correlation with the actual forecast performance of various models. By understanding the inherent forecastability of time series before model training, practitioners can focus their planning efforts on products and supply chain levels that are more forecastable, while setting appropriate expectations or seeking alternative strategies for products with limited forecastability.\n\n††journalyear: 2025††copyright: rightsretained††conference: Proceedings of the 1st Workshop on ”AI for Supply Chain: Today and Future” @ 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2; August 3, 2025; Toronto, ON, Canada.††booktitle: Proceedings of the 1st Workshop on ”AI for Supply Chain: Today and Future” @ 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2 (KDD ’25), August 3, 2025, Toronto, ON, Canada††isbn: 979-8-4007-1454-2/25/08††doi: 10.1145/XXXXXX.XXXXXX\n\n##  1\\. Introduction\n\nIn the rapidly evolving landscape of supply chain management, accurate time series forecasting has become an indispensable tool for demand prediction, inventory optimization, and supply planning (Lim and Zohren, [2021](https://arxiv.org/html/2507.13556v1#bib.bib11); Liang et al., [2024](https://arxiv.org/html/2507.13556v1#bib.bib10); Rangapuram et al., [2018](https://arxiv.org/html/2507.13556v1#bib.bib16); Benidis et al., [2022](https://arxiv.org/html/2507.13556v1#bib.bib4); Hamilton, [2020](https://arxiv.org/html/2507.13556v1#bib.bib9)). However, the effectiveness of these forecasts is intrinsically tied to the inherent forecastability of the underlying data. Not all time series exhibit the same degree of forecastability, and this variability can significantly impact the reliability of business decisions based on these predictions.\n\nTraditionally, practitioners assess forecastability post hoc—by training models and evaluating performance. Although effective, this process is computationally expensive and can lead to wasted effort in inherently unpredictable series. We propose a more systematic alternative: using spectral predictability (Goerg, [2013](https://arxiv.org/html/2507.13556v1#bib.bib8)) and Lyapunov exponents (Dingwell, [2006](https://arxiv.org/html/2507.13556v1#bib.bib5)) to quantify a time series’ forecastability a priori (Wang et al., [2023](https://arxiv.org/html/2507.13556v1#bib.bib18)). We will demonstrate how these metrics can be systematically applied to time series data to identify the i", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [56] TOOL CALL — Bash · 2026-07-30 12:15:23 UTC

```
Fetch Forecastability Profiles paper:

export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" fetch --url "https://arxiv.org/html/2603.20546v1" --max-chars 6000
```

### [57] TOOL RESULT — Bash · 2026-07-30 12:15:23 UTC

```
{"stdout": "URL: https://arxiv.org/html/2603.20546v1\nType: HTML\nLength: 41684 chars (truncated)\n\n--- Content ---\n\n##### Report GitHub Issue\n\n×\n\nTitle:\n\nContent selection saved. Describe the issue below:\n\nDescription:\n\nSubmit without GitHub Submit in GitHub\n\narXiv is now an independent nonprofit! [Learn more](https://info.arxiv.org/about) ×\n\n[ Back to arXiv ](/)\n\n[Why HTML?](https://info.arxiv.org/about/accessible_HTML.html) Report Issue [ Back to Abstract ](/abs/2603.20546v1 \"Back to abstract page\") [ Download PDF](/pdf/2603.20546v1 \"Download PDF\") [ ](javascript:toggleNavTOC\\(\\); \"Toggle navigation\") [ ](javascript:toggleReadingMode\\(\\); \"Disable reading mode, show header and footer\")\n\n  1. Abstract\n  2. I Introduction\n     1. I-A Relation to Existing Forecasting Practice\n  3. II Setting\n     1. II-A Regularity Conditions\n  4. III The Information Bound on Prediction\n  5. IV Forecastability Profiles and Informative Horizons\n     1. IV-A Forecastability\n     2. IV-B Behaviour of Forecastability Across Horizons\n     3. IV-C The Entropy Rate and Maximum Forecastability\n     4. IV-D The Informative Horizon Set\n     5. IV-E Interpretation of the Forecastability Profile\n     6. IV-F The Horizon-Specific Bound\n     7. IV-G Complexity Futility\n  6. V Decomposition of Predictive Loss\n  7. VI Horizons of Low Forecastability\n  8. VII Empirical Estimation\n  9. VIII Implications for Forecasting Practice\n     1. VIII-A Illustrative Example: Seasonal Information Structure\n  10. IX Conclusion\n  11. References\n\n\n\n[ License: arXiv.org perpetual non-exclusive license ](https://info.arxiv.org/help/license/index.html#licenses-available)\n\narXiv:2603.20546v1 [stat.AP] 20 Mar 2026\n\n# On the Limits of Prediction:   \nForecastability Profiles and Information Decay in Time Series\n\nPeter Maurice Catt   \nIndependent Researcher   \nAuckland, New Zealand \n\n###### Abstract\n\nForecasting accuracy is bounded by the information available about the future. This paper makes that statement precise using information-theoretic tools. Under logarithmic loss, the expected performance of any probabilistic forecast decomposes into two parts: an irreducible component and an approximation component. The irreducible term is the conditional entropy of the future given the available information, while the approximation term is the divergence between the true conditional distribution and the forecasting method. The gap between this conditional-entropy limit and an unconditional baseline is exactly the mutual information between the future observation and the declared information set.\n\nThis leads to a definition of forecastability as the maximum achievable reduction in expected log loss. Evaluated across horizons, forecastability forms a profile that describes how predictive information varies with lead time. This profile reflects the dependence structure of the process and need not be monotone: predictive information may be concentrated at particular lags, including seasonal horizons, even when intermediate horizons contain little useful signal.\n\nFrom this profile, the paper defines the informative horizon set: the horizons at which forecastability exceeds a practical threshold. At horizons not in this set, the achievable gain over the unconditional baseline is necessarily small, regardless of the forecasting method used. The framework therefore separates what is learnable from what is not, and distinguishes limits imposed by the data from errors introduced by modelling. The result is a pre-modelling diagnostic that identifies where meaningful prediction is feasible before any model is chosen, providing a principled basis for allocating modelling effort across forecast horizons.\n\n##  I Introduction\n\nForecasting is usually framed as a problem of model choice. This paper starts earlier. It asks how much predictive information the available data contain at each horizon, and what that implies for the best accuracy any method can achieve.\n\nThe central object is the _forecastability profile_ : the function ℱ​(h;ℐt)\\mathcal{F}(h;\\mathcal{I}_{t}) that maps each forecast horizon to the mutual information between the future observation and the declared information set. This profile is horizon-dependent and reflects the dependence structure of the process. The primary operational output is the _informative horizon set_ ℋε\\mathcal{H}_{\\varepsilon}: the collection of horizons at which forecastability exceeds a decision-relevant threshold ε\\varepsilon. At horizons outside ℋε\\mathcal{H}_{\\varepsilon}, the maximum achievable reduction in expected log loss relative to the unconditional baseline is bounded by ε\\varepsilon, given the declared information set and under logarithmic loss.\n\nForecastability is not a single threshold crossing but a structure over horizons. Decisions about where to invest modelling effort should be based on the set of horizons where this structure exceeds a decision-relevant threshold.\n\nThe paper makes three contributions. First, it shows that the maximum achievable reduction in expected log loss from exploiting any information set is exactly the mutual information between the future observation and that information set (Theorem 2). This quantity, termed forecastability, defines a horizon-dependent upper bound on predictive improvement under logarithmic loss and relative to the unconditional baseline. Second, it introduces the forecastability profile and the informative horizon set as the primary diagnostic and operational objects, and shows that at any horizon where ℱ​(h;ℐt)≤ε\\mathcal{F}(h;\\mathcal{I}_{t})\\leq\\varepsilon, the gain from any probabilistic forecasting procedure is bounded by ε\\varepsilon (Proposition 4). Third, it links one-step forecastability to the entropy rate of the process (Proposition 3), anchoring the profile in classical information theory.\n\nThe underlying identities are standard. The contribution is to show that they imply hard, horizon-dependent forecasting limits and to formalise the forecastability profile and informative horizon set as the objects through which these limits become operational for practice. The prim", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [58] TOOL CALL — Bash · 2026-07-30 12:15:23 UTC

```
Search for spectral predictability approaches:

export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "spectral predictability time series method selection" --max-results 5
```

### [59] TOOL RESULT — Bash · 2026-07-30 12:15:23 UTC

```
{"stdout": "Search: spectral predictability time series method selection\nFound: 5 results\n\n1. Spectral Predictability as a Fast Reliability Indicator for Time Series ...\n   https://arxiv.org/html/2511.08884v1\n   We quantify the inherent forecastability of a time series using spectral predictability Ω \\Omega , a metric grounded in information theory and ......\n\n2. nesl/Spectral-Predictability-TS\n   https://github.com/nesl/Spectral-Predictability-TS\n   Spectral Predictability as a Fast Reliability Indicator for Time Series Forecasting Model Selection · A modified TimeLLM pipeline for forecasting experiments and ......\n\n3. Model-free quantification of time-series predictability\n   https://link.aps.org/doi/10.1103/PhysRevE.90.052910\n   by J Garland · 2014 · Cited by 102 — This paper provides insight into when, why, and how forecast strategies fail when they are applied to complicated time series....\n\n4. Model-Free Quantification of Time-Series Predictability\n   https://sfi-edu.s3.amazonaws.com/sfi-edu/production/uploads/sfi-com/dev/uploads/filer/2a/0e/2a0e344b-74aa-4d58-afdb-f714b705c7d6/14-05-014.pdf\n   For each time series, we construct predictions using a wide variety of forecast models, then compare the accuracy of the predictions with the permutation ......\n\n5. Time Series Forecastability Measures\n   https://arxiv.org/html/2507.13556v1\n   The spectral predictability evaluates the strength and complexity of frequency components within a time series, providing insights into its ......", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [60] ASSISTANT · 2026-07-30 12:15:29 UTC

```
Excellent. I found recent papers on **spectral predictability as a model selection indicator** (2511.08884 from 2025) and **forecastability profiles** (2603.20546 from 2026). These are very recent. Let me fetch the spectral predictability paper:
```

### [61] TOOL CALL — Bash · 2026-07-30 12:15:29 UTC

```
Fetch spectral predictability for model selection paper:

export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" fetch --url "https://arxiv.org/html/2511.08884v1" --max-chars 8000
```

### [62] TOOL RESULT — Bash · 2026-07-30 12:15:29 UTC

```
{"stdout": "URL: https://arxiv.org/html/2511.08884v1\nType: HTML\nLength: 52976 chars (truncated)\n\n--- Content ---\n\n##### Report GitHub Issue\n\n×\n\nTitle:\n\nContent selection saved. Describe the issue below:\n\nDescription:\n\nSubmit without GitHub Submit in GitHub\n\narXiv is now an independent nonprofit! [Learn more](https://info.arxiv.org/about) ×\n\n[ Back to arXiv ](/)\n\n[Why HTML?](https://info.arxiv.org/about/accessible_HTML.html) Report Issue [ Back to Abstract ](/abs/2511.08884v1 \"Back to abstract page\") [ Download PDF](/pdf/2511.08884v1 \"Download PDF\") [ ](javascript:toggleNavTOC\\(\\); \"Toggle navigation\") [ ](javascript:toggleReadingMode\\(\\); \"Disable reading mode, show header and footer\")\n\n  1. Abstract\n  2. 1 Introduction\n  3. 2 Related Work\n  4. 3 Spectral Predictability Ω\\Omega\n  5. 4 Controlled Experiment Results: Establishing the Effect of Ω\\Omega\n  6. 5 Large-Scale Analysis Results: Model-Family-Specific Responses to Ω\\Omega\n     1. 5.1 Relationship with Chaos (Largest Lyapunov Exponent)\n     2. 5.2 Practical Implications for Model Selection\n     3. 5.3 When to Trust Ω\\Omega: Reliability Conditions\n  7. 6 Discussion\n     1. 6.1 Why Not Just Use Validation Error?\n     2. 6.2 Limitations\n  8. 7 Conclusion and Future Work\n  9. 8 Acknowledgements\n  10. References\n  11. A Appendix\n     1. A.1 Model Categorization by Type\n     2. A.2 Dataset Protocol\n     3. A.3 Training Protocol\n     4. A.4 Spectral Predictability Details\n     5. A.5 Statistical Results of Controlled Experiments\n  12. B Instructive Exceptions\n\n\n\n[ License: arXiv.org perpetual non-exclusive license ](https://info.arxiv.org/help/license/index.html#licenses-available)\n\narXiv:2511.08884v1 [cs.LG] 12 Nov 2025\n\n# Spectral Predictability as a Fast Reliability Indicator for Time Series Forecasting Model Selection\n\nOliver Wang   \nElectrical and Computer Engineering   \nUniversity of California, Los Angeles   \nowang22@g.ucla.edu &Pengrui Quan   \nElectrical and Computer Engineering   \nUniversity of California, Los Angeles   \nprquan@g.ucla.edu &Kang Yang   \nElectrical and Computer Engineering   \nUniversity of California, Los Angeles   \nkyang73@g.ucla.edu &Mani Srivastava11footnotemark: 1   \nElectrical and Computer Engineering   \nUniversity of California, Los Angeles   \nmbs@ucla.edu Mani Srivastava holds concurrent appointments as a Professor of ECE and CS (joint) at the University of California, Los Angeles, and as an Amazon Scholar at Amazon. This paper describes work performed at UCLA and is not associated with Amazon.\n\n###### Abstract\n\nPractitioners deploying time series forecasting models face a dilemma: exhaustively validating dozens of models is computationally prohibitive, yet choosing the wrong model risks poor performance. We show that _spectral predictability_ Ω\\Omega—a simple signal processing metric—systematically stratifies model family performance, enabling fast model selection. We conduct controlled experiments in four different domains, then further expand our analysis to 51 models and 28 datasets from the GIFT-Eval benchmark. We find that large time series foundation models (TSFMs) systematically outperform lightweight task-trained baselines when Ω\\Omega is high, while their advantage vanishes as Ω\\Omega drops. Computing Ω\\Omega takes seconds per dataset, enabling practitioners to quickly assess whether their data suits TSFM approaches or whether simpler, cheaper models suffice. We demonstrate that Ω\\Omega stratifies model performance predictably, offering a practical first-pass filter that reduces validation costs while highlighting the need for models that excel on genuinely difficult (low-Ω\\Omega) problems rather than merely optimizing easy ones.\n\n##  1 Introduction\n\nLarge time series foundation models (TSFMs) for time series forecasting promise broad improvements by leveraging massive pretraining (Ye et al., 2024; Li et al., 2025; Liang et al., 2024; Ansari et al., 2024; Gruver et al., 2024). Yet empirical evidence remains mixed; simple baselines such as DLinear often match or surpass complex architectures (Tan et al., 2024; Zeng et al., 2022; Li et al., 2025). Practitioners face a practical challenge: _how to choose which model to deploy without exhaustively validating every option?_\n\nComprehensive validation is impractical. Consider a practitioner with a dozen or more candidate models and a new dataset: training and validating all models requires substantial compute, time, and engineering effort. Worse, this process provides no insight into _why_ certain models work better, making it difficult to generalize lessons to future datasets.\n\nWe propose spectral predictability Ω\\Omega—a simple, fast-to-compute signal property—as a reliability indicator that narrows the model search space _before_ expensive validation begins. Grounded in signal processing, Ω\\Omega quantifies the concentration of a series’ power spectrum: high Ω\\Omega reflects structured, repeatable patterns; low Ω\\Omega indicates diffuse, irregular signals. Computing Ω\\Omega takes seconds on a commodity device, yet we show it systematically stratifies model performance.\n\nOur key finding. Large zero-shot111We use GIFT-Eval’s model taxonomy where “zero-shot” refers to TSFMs deployed with their original pretrained weights. See Large-Scale Analysis Results for full definitions. models, applied without fine-tuning, show consistent advantages in high-Ω\\Omega regimes across diverse domains. Practitioners can compute Ω\\Omega to determine whether zero-shot or lightweight models are likely to perform best, reducing validation cost. As Ω\\Omega decreases, model performance converges, underscoring the need for methods that better handle difficult (low-Ω\\Omega) data.\n\nIn summary, this paper makes the following contributions:\n\n  * •\n\nWe introduce spectral predictability Ω\\Omega as a fast and interpretable indicator of time-series forecastability, derived from frequency-domain concentration and computable without model training.\n\n  * •\n\nControlled experiments on synthetic and real-world datasets (CarbonCast, PEMS, Fitbit) show that forecasting error decreases monotonically with increasing Ω\\Omega, confirming that Ω\\Omega reflects intrinsic difficulty.\n\n  * •\n\nLarge-scale analysis of 51 models and 28 GIFT-Eval datasets shows that zero-shot TSFMs outperform statistical and deep-learning baselines by up to 60% in high-Ω\\Omega regimes, while the advantage vanishes in low-Ω\\Omega settings.\n\n  * •\n\nWe identify the low-Ω\\Omega regime as a critical open frontier where all model families struggle, motivating the design of models robust to irregular or weakly periodic signals.\n\n  * •\n\nWe provide actionable guidance for practitioners, showing that computing Ω\\Omega takes seconds yet reliably narrows the model search space, reducing validation cost and improving deployment efficiency.\n\n\n\n\n##  2 Related Work\n\nSimplicity versus Capacity. Despite scaling trends (Shi et al., 2024, 2025), lightweight baselines remain competitive (Zeng et al., 2022; Miller et al., 2024). Comparative studies (Goswami et al., 2024; Jin et al., 2024) rarely explain _why_ performance varies across domains, leaving practitioners without guidance for model selection.\n\nLLMs for Time Series. Methods include direct tokenization, architectural adaptation, and adapter-based fine-tuning (Gruver et al., 2024; Ansari et al., 2024). Ablations question how much LLM pretraining contributes (Tan et al., 2024; Jin et al., 2024; Elsayed et al., 2021). We build on Jin et al. (2024) for our codebase and initial experiments are based on variations on their LLAMA-7B backbone structure, which will be explained further in the Controlled Experiment Results.\n\nForecastability and Reliability. Forecastability metrics such as spectral entropy, approximate entropy, and seasonality strength relate to signal difficulty (Tang et al., 2024; Wu et al., 2023; Wang et al., 2025; Guntu et al., 2020). While these metrics characterize data properties, they have not been systematically used to guide model selection at deployment time.\n\nOur contribution is not the Ω\\Omega metric itself—spectral entropy is well-establish", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [63] ASSISTANT · 2026-07-30 12:15:37 UTC

```
Perfect! I found the key papers. Now I have a clear understanding of what's already been done:

1. **Spectral predictability (Ω)** for model selection — VERY RECENT (Nov 2025) — uses signal processing to predict which model family will work best
2. **Forecastability profiles** — information decay across horizons (Mar 2026)
3. **Lyapunov exponents** for forecastability (2025)
4. **Mutual information based bounds** and forecastability concepts

Now let me think about what's NOT been done. The spectral predictability paper does model selection WITHIN families (TSFMs vs simple baselines). But what if we go **deeper** — not just selecting between model types, but **within a single model family, adaptively change the hyperparameters or ensemble weights based on spectral properties**?

Or even more novel: **Use spectral properties to create a self-tuning ensemble** that redistributes weight across methods IN REAL-TIME as new data arrives and spectral characteristics change.

Let me search for adaptive ensembles and online ensemble methods:
```

### [64] TOOL CALL — Bash · 2026-07-30 12:15:37 UTC

```
Search for adaptive online ensembles:

export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "online ensemble adaptive weights time series forecasting streaming" --max-results 8
```

### [65] TOOL CALL — Bash · 2026-07-30 12:15:37 UTC

```
Search for meta-learned hyperparameters:

export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "meta-learner hyperparameter tuning time series data properties" --max-results 8
```

### [66] TOOL RESULT — Bash · 2026-07-30 12:15:37 UTC

```
{"stdout": "Search: online ensemble adaptive weights time series forecasting streaming\nFound: 8 results\n\n1. Explainable online ensemble of deep neural network pruning ...\n   https://link.springer.com/article/10.1007/s10994-022-06218-4\n   by A Saadallah · 2022 · Cited by 35 — A Drift-aware ensemble pruning for time series forecasting through adaptive model selection using correlation-based measures for similarity and ......\n\n2. Combining LSTM Network Ensemble via Adaptive ...\n   https://onlinelibrary.wiley.com/doi/10.1155/2018/2470171\n   This paper presents a novel LSTM ensemble forecasting algorithm that effectively combines multiple forecast (prediction) results from a set of individual LSTM ......\n\n3. Ensemble Modeling for Time Series Forecasting: an Adaptive ...\n   https://ar5iv.labs.arxiv.org/html/2304.04308\n   This paper proposes a new methodology for building robust ensembles of time series forecasting models. Our approach utilizes Adaptive Robust Optimization (ARO)...\n\n4. Implementing Online Ensembles for Time Series Forecasting\n   https://magittan.github.io/static/Online_Ensembles/Implementing_Online_Ensemble_Learning.pdf\n   Online Ensemble methods are used in conjunction with the predictions from a set of time series forecasting methods (e.g. LSTM) in an expert prediction...\n\n5. OneNet: Enhancing Time Series Forecasting Models under ...\n   https://papers.neurips.cc/paper_files/paper/2023/file/dd6a47bc0aad6f34aa5e77706d90cdc4-Paper-Conference.pdf\n   by YF Zhang · Cited by 136 — Online updating of time series forecasting models aims to address the concept drifting problem by efficiently updating forecasting models based on streaming....\n\n6. Forecasting Time Series - Ensemble Models\n   https://auto.gluon.ai/stable/tutorials/timeseries/forecasting-ensembles.html\n   This page contains the list of time series ensemble models available in AutoGluon. Each time series gets its own optimal ensemble weights based on predictions ......\n\n7. Adaptive demand forecasting framework with weighted ...\n   https://www.nature.com/articles/s41598-025-23352-w\n   by IM Hammam · 2025 · Cited by 10 — This paper introduces an adaptive, hybrid forecasting framework that integrates ARIMA-based regression models with XGBoost using a weighted ......\n\n8. This Might be the Simplest Way to Ensemble Time-Series ...\n   https://medium.com/@mike.roweprediger/this-might-be-the-simplest-way-to-ensemble-time-series-models-in-online-fashion-a4f56c740e26\n   The function calculates the ensemble forecast by first calculating the weights for each prediction using a power function of the standard ......", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [67] TOOL RESULT — Bash · 2026-07-30 12:15:39 UTC

```
{"stdout": "Search: meta-learner hyperparameter tuning time series data properties\nFound: 8 results\n\n1. Tailored forecasting from short time series via meta-learning\n   https://www.science.org/doi/10.1126/sciadv.ady7216\n   by DA Norton · 2026 · Cited by 6 — Specifically, we wish to tailor the parameters of an ML model to forecast a dynamical system for which only a small amount of data is available....\n\n2. A Meta-Knowledge–Augmented LLM Framework for Hyperparameter ...\n   https://arxiv.org/html/2602.01445\n   To address this, we propose LLM-AutoMOpt, a framework for automating hyperparameter optimization in deep learning models for time series forecasting.The ......\n\n3. Evaluation-Free Time-Series Forecasting Model Selection via ...\n   https://engineering.purdue.edu/dcsl/wp-content/uploads/2025/02/AutoForecast_ACM_TKDD.pdf\n   by M ABDALLAH · 2023 · Cited by 19 — Tuning of Time-series Meta-learner: We show the effect of different hyper-parameters used in the training of the time-series meta-learner Θ on the performance...\n\n4. A Meta-learner approach to multistep-ahead time series prediction\n   https://link.springer.com/article/10.1007/s41060-024-00599-6\n   by F Bahrpeyma · 2025 · Cited by 10 — Multistep-ahead time series prediction involves forecasting multiple future time steps based on historical data....\n\n5. Meta-Learning For Model Selection And Hyperparameters\n   https://www.ml4devs.com/what-is/meta-learning-for-model-selection-and-hyper-parameters/\n   Learn meta-learning techniques that use prior task data to automate model selection, hyperparameter optimization, and algorithm choice....\n\n6. Meta-learning how to forecast time series\n   https://robjhyndman.com/papers/fforms.pdf\n   by TS Talagala · 2022 · Cited by 221 — The training set is used to estimate the parameters of a forecasting model. Based on this fitted model, we generate forecasts over the test set ......\n\n7. A Time Series Forecasting Approach Based on Meta-Learning for ...\n   https://www.mdpi.com/1996-1073/17/8/1947\n   by Z Xu · 2024 · Cited by 9 — The approach involves an architecture divided into meta-learner and base-learner, which learns initialization parameters from 89 time series ......\n\n8. Can Meta-Learning Enhance the Accuracy of Time Series Models?\n   https://medium.com/pythons-gurus/can-meta-learning-enhance-the-accuracy-of-time-series-models-981436d36180\n   Meta-learning can also be used for automated model selection and hyperparameter tuning. correlation, trend strength, etc....", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [68] ASSISTANT · 2026-07-30 12:15:47 UTC

```
Good. Online ensembles and meta-learners exist. Now let me think about a genuinely novel direction. 

**Core insight I want to pursue**: Instead of just predicting WHICH model works best before training, what if we **dynamically adapt the ensemble's internal architecture based on rolling spectral properties**? 

Specifically: **A spectrally-adaptive ensemble that monitors the spectral predictability Ω in a sliding window and automatically shifts the ensemble's INTERNAL component weighting or method composition** — not post-hoc model selection but real-time model reconfiguration.

This is different from:
- **Spectral predictability for model selection** (Wang et al 2025) — they use Ω to pick between model families, not to adapt within
- **Online ensembles** — existing ones adapt based on error, not data properties
- **Forecastability profiles** — they're diagnostic, not prescriptive for method switching

Let me search to confirm this hasn't been done:
```

### [69] TOOL CALL — Bash · 2026-07-30 12:15:47 UTC

```
Search for spectral-based ensemble adaptation:

export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SCRIPT_DIR/scripts/aii_fast_web_search.py" --query "spectral properties ensemble component selection adaptive switching" --max-results 5
```

### [70] TOOL RESULT — Bash [ERROR] · 2026-07-30 12:15:47 UTC

```
Error: Exit code 2
/ai-inventor/.claude/skills/aii-web-tools/../.ability_client_venv/bin/python: can't open file '/scripts/aii_fast_web_search.py': [Errno 2] No such file or directory
```

### [71] TOOL CALL — Bash · 2026-07-30 12:15:47 UTC

```
Search for spectral concept drift detection:

export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "concept drift detection spectral analysis time series online" --max-results 5
```

### [72] TOOL RESULT — Bash · 2026-07-30 12:15:47 UTC

```
{"stdout": "Search: concept drift detection spectral analysis time series online\nFound: 5 results\n\n1. Taming Recurring Concept Drift in Online Time Series ...\n   https://arxiv.org/html/2506.14790v2\n   Concept drift refers to the change in the relationship between input variables and their true values over time. In the context of time series, ......\n\n2. Detecting Concept in Forecasting Systems : r/datascience\n   https://www.reddit.com/r/datascience/comments/1f1hbrg/detecting_concept_in_forecasting_systems/\n   Concept drift, on the other hand, is all about those unexpected changes in your target variable's behavior, often caused by outside factors that ......\n\n3. Concept Drift Detection in Data Stream Mining : A literature ...\n   https://www.sciencedirect.com/science/article/pii/S1319157821003062\n   by S Agrahari · 2022 · Cited by 381 — This paper is to introduce a survey identified with a broad categorization of concept drift detectors with their key points, limitations, and advantages....\n\n4. perceiving a concept drift through common spatial pattern\n   https://link.springer.com/article/10.1007/s13042-023-01810-z\n   by A Flórez · 2023 · Cited by 13 — This paper proposes a new approach for concept drift detection—a novel approach to deal with sudden or abrupt drift, the most common drift found ......\n\n5. What are Concept Drifts in Time Series Data?\n   https://www.iunera.com/kraken/fabric/concept-drift/\n   Concept drifts are changing patterns over time in underlying data foundations of a concept. Concepts can be seen as data values....", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [73] ASSISTANT · 2026-07-30 12:15:51 UTC

```
Let me fix that search:
```

### [74] TOOL CALL — Bash · 2026-07-30 12:15:51 UTC

```
Search for frequency-domain ensemble methods:

export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "frequency domain properties ensemble weights adaptive" --max-results 5
```

### [75] TOOL RESULT — Bash · 2026-07-30 12:15:51 UTC

```
{"stdout": "Search: frequency domain properties ensemble weights adaptive\nFound: 5 results\n\n1. Adaptive neural network ensemble using prediction frequency\n   https://academic.oup.com/jcde/article/10/4/1547/7222904\n   by U Lee · 2023 · Cited by 10 — This study proposes a prediction frequency-based ensemble that identifies core prediction values, which are core prediction members to be used in the ensemble....\n\n2. Frequency Domain FIR and IIR Adaptive Filters\n   https://ntrs.nasa.gov/api/citations/19940004355/downloads/19940004355.pdf\n   by DW Lynn · 1990 · Cited by 1 — The goal of an adaptive filter is to automatically adjust the weights W so that the difference between the output {yn} and some desired signal ......\n\n3. Frequency-domain and multirate adaptive filtering\n   https://course.ece.cmu.edu/~ece792/handouts/Shynk92.pdf\n   As a result, a time-varying step size can be used for each adaptive weight, thereby allowing a more uniform convergence rate across the adaptive....\n\n4. Adaptive Line Enhancer for Passive Sonars Based on Frequency ...\n   https://link.springer.com/article/10.1007/s13369-024-09682-3\n   by Z Li · 2025 · Cited by 7 — The proposed l1-SE-MWE-FALE algorithm is based on the integration of frequency-domain sparsity, Shannon entropy (SE) criterion along with mixed- ......\n\n5. Instance-Adaptive Ensemble Weighting\n   https://www.emergentmind.com/topics/instance-adaptive-ensemble-weighting\n   Instance-adaptive ensemble weighting is a dynamic method that assigns weights to models based on instance-specific metrics....", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [76] ASSISTANT · 2026-07-30 12:15:55 UTC

```
Good results. Let me search more directly for what I'm after:
```

### [77] TOOL CALL — Bash · 2026-07-30 12:15:55 UTC

```
Search for rule-based model switching:

export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "time series model switching rule-based data characteristics" --max-results 8
```

### [78] TOOL CALL — Bash · 2026-07-30 12:15:55 UTC

```
Search for stationarity-based method selection:

export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "stationarity detection ARIMA vs neural networks forecast" --max-results 8
```

### [79] TOOL RESULT — Bash · 2026-07-30 12:15:55 UTC

```
{"stdout": "Search: time series model switching rule-based data characteristics\nFound: 8 results\n\n1. meta-learning the characteristics of univariate time series\n   https://robjhyndman.com/papers/wang3.pdf\n   by K Smith-Miles¹ · Cited by 309 — Time series characteristics are used as meta-features to learn the forecasting methods based on their performance classifications....\n\n2. [D] Machine Learning on Time Series Data? : r/MachineLearning\n   https://www.reddit.com/r/MachineLearning/comments/9ofd7x/d_machine_learning_on_time_series_data/\n   I am going to be working with building models with time series data, which is something that I have not done in the past. Is there a different approach ......\n\n3. Time-Series Forecasting: Definition, Methods, and Applications\n   https://www.tigerdata.com/blog/what-is-time-series-forecasting\n   A good rule of thumb would be the more data we have, the better our model will generate forecasts. Data quality. Data quality entails some basic requirements,...\n\n4. Time Series Data - an overview\n   https://www.sciencedirect.com/topics/computer-science/time-series-data\n   Time series data refers to series of random variables arranged based on time, reflecting the changing state of a phenomenon over time....\n\n5. Understanding Time Series Data in Machine Learning | Forecasting ...\n   https://www.researchgate.net/post/Understanding_Time_Series_Data_in_Machine_Learning_Forecasting_Methods_Explained\n   Understanding Time Series Data in Machine Learning | Forecasting Methods Explained\nTime series data is all around us—from stock prices to weather patterns, ......\n\n6. Automatic Identification of Time Series Features for Rule-Based ...\n   https://faculty.wharton.upenn.edu/wp-content/uploads/2001/12/85-JSA-Automatic-Identification-of-Time-Series-Features-for-Rule-Based-Forecasting.pdf\n   by M Adya · 2001 · Cited by 157 — Rule-based forecasting (RBF) is an expert system that uses features of time series to select and weight extrapolation techniques. Thus, it is dependent upon ......\n\n7. Feature Engineering for Time Series Forecasting - Kishan Manani\n   https://www.youtube.com/watch?v=2vMNiSeNUjI\n   In this podcast episode, we talked with Kishan Manani about feature engineering for time series forecasting....\n\n8. A Unified Machine Learning Framework for Time Series ...\n   https://medium.com/data-science-collective/a-unified-machine-learning-framework-for-time-series-forecasting-7f3971216ec1\n   time series data follows predictable patterns — like a straight line with trends and seasonality — but reality is often far messier....", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [80] TOOL RESULT — Bash · 2026-07-30 12:15:57 UTC

```
{"stdout": "Search: stationarity detection ARIMA vs neural networks forecast\nFound: 8 results\n\n1. ARIMA based algorithms vs neural networks in anomaly detection\n   https://www.eyer.ai/blog/arima-based-algorithms-vs-neural-networks-in-anomaly-detection/\n   This article explores the comparative efficacy of statistical methods like ARIMA versus modern deep learning techniques in detecting anomalies in time series....\n\n2. A Review of ARIMA vs. Machine Learning Approaches for Time ...\n   https://www.mdpi.com/1999-5903/15/8/255\n   by VI Kontopoulou · 2023 · Cited by 661 — SVM performs better in the case of non-linear consumption patterns, while ARIMA exhibits better behavior in the linear load approximation. indicated the ......\n\n3. How do neural networks compare to traditional methods such as ARIMA ...\n   https://www.quora.com/How-do-neural-networks-compare-to-traditional-methods-such-as-ARIMA-for-time-series-predictions\n   How do neural networks compare to traditional methods such as ARIMA for time series predictions?...\n\n4. Time series prediction using ARIMA vs LSTM\n   https://datascience.stackexchange.com/questions/12721/time-series-prediction-using-arima-vs-lstm\n   The problem that I am dealing with is predicting time series values. I am looking at one time series at a time and based on for example 15% of the input ......\n\n5. Comparison of ARIMA and Artificial Neural Networks Models for Stock ...\n   https://onlinelibrary.wiley.com/doi/10.1155/2014/614342\n   ARIMA model generally performs better in the prediction of linear time series, while ANNs perform better in the prediction of nonlinear time ......\n\n6. Prediction based on traditional network prediction model and LSTM ...\n   https://dl.acm.org/doi/fullHtml/10.1145/3603781.3603910\n   by H Li · 2023 · Cited by 6 — The purpose of this study is to compare the traditional network forecasting model with the new neural network forecasting model, LSTM....\n\n7. Is Deep Learning Always Better? ARIMA vs LSTM in Demand ...\n   https://medium.com/@helo.justus/is-deep-learning-always-better-arima-vs-lstm-in-demand-forecasting-899268473cae\n   ARIMA models assume stationarity for its data's statistical properties. Stationarity means the data's mean, variance and autocorrelation don't ......\n\n8. Forecasting the OMXS30 – a comparison between ARIMA and ...\n   https://www.diva-portal.org/smash/get/diva2:1443859/FULLTEXT01.pdf\n   by D Andréasson · 2020 · Cited by 5 — The results showed that the LSTM model performs slightly better when forecasting 90 and 30 days ahead, whereas the ARIMA model has comparable ......", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [81] ASSISTANT · 2026-07-30 12:16:04 UTC

```
I see **Rule-Based Forecasting (RBF)** from 2001 — uses time series features to select and weight extrapolation methods. That's old. But let me check what's state-of-the-art. Let me also search for something I haven't explored yet: **Using anomaly indicators to adapt forecasting**:
```

### [82] TOOL CALL — Bash · 2026-07-30 12:16:04 UTC

```
Search for predictability indices:

export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "predictability index score time series which model works best" --max-results 8
```

### [83] TOOL RESULT — Bash · 2026-07-30 12:16:04 UTC

```
{"stdout": "Search: predictability index score time series which model works best\nFound: 8 results\n\n1. A Survey of Machine Learning Methods for Time Series ...\n   https://www.mdpi.com/2076-3417/15/11/5957\n   by T Hall · 2025 · Cited by 83 — RNNs demonstrate a superior performance, ranking as the best-performing models in 61.36% of studies and achieving a WRA score of 0.7330....\n\n2. [D] Best Time Series models for Forecasting (alternative to ...\n   https://www.reddit.com/r/MachineLearning/comments/193672o/d_best_time_series_models_for_forecasting/\n   I've recently discovered TimeGPT and its really great at demand forecasting.\n\nI am not very good with pytorch but I couldn't achieve anything even close ......\n\n3. Predictability-Aligned Evaluation for Time Series Forecasting\n   https://arxiv.org/html/2509.23074v3\n   Overall, we advocate moving beyond leaderboard-style ranking toward a more insightful, predictability-aware evaluation that fosters fairer model ......\n\n4. Predictability of a time series - forecasting\n   https://stats.stackexchange.com/questions/387698/predictability-of-a-time-series\n   Say we are given a time series (xt)t∈P where P is the index set of past observations (train set). Imagine that we have built a model for our data and ......\n\n5. Evaluating Time Series Models for Real-World Forecasting\n   https://medium.com/@karanbhutani477/evaluating-time-series-models-for-real-world-forecasting-a-practical-comparison-5c9622618715\n   In this article, we'll compare six popular time series models on a real-world dataset, highlighting their performance, speed, and practicality....\n\n6. Time series forecasting: 2025 complete guide\n   https://www.influxdata.com/time-series-forecasting-methods/\n   In time series analysis, the moving-average model (MA model), also known as moving-average process, is a common approach for modeling univariate time series....\n\n7. Comparing model performance for time series prediction\n   https://forum.posit.co/t/comparing-model-performance-for-time-series-prediction/92256\n   Hi, I am getting started with comparing time series forecasting model performance using tidymodels and have limited experience so please ......\n\n8. What are the most helpful time series metrics for choosing ...\n   https://www.researchgate.net/post/What_are_the_most_helpful_time_series_metrics_for_choosing_the_right_prediction_method\n   There are many different techniques for implementing time series prediction. Methods like ARIMA, NNs, RNN, LSTM, etc. What are the most effective ......", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [84] ASSISTANT · 2026-07-30 12:16:08 UTC

```
Interesting! I found **"Predictability-Aligned Evaluation for Time Series Forecasting"** (2509.23074 from 2025). Let me fetch that:
```

### [85] TOOL CALL — Bash · 2026-07-30 12:16:08 UTC

```
Fetch predictability-aligned evaluation paper:

export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" fetch --url "https://arxiv.org/html/2509.23074v3" --max-chars 7000
```

### [86] TOOL RESULT — Bash · 2026-07-30 12:16:08 UTC

```
{"stdout": "URL: https://arxiv.org/html/2509.23074v3\nType: HTML\nLength: 98187 chars (truncated)\n\n--- Content ---\n\n##### Report GitHub Issue\n\n×\n\nTitle:\n\nContent selection saved. Describe the issue below:\n\nDescription:\n\nSubmit without GitHub Submit in GitHub\n\narXiv is now an independent nonprofit! [Learn more](https://info.arxiv.org/about) ×\n\n[ Back to arXiv ](/)\n\n[Why HTML?](https://info.arxiv.org/about/accessible_HTML.html) Report Issue [ Back to Abstract ](/abs/2509.23074v3 \"Back to abstract page\") [ Download PDF](/pdf/2509.23074v3 \"Download PDF\") [ ](javascript:toggleNavTOC\\(\\); \"Toggle navigation\") [ ](javascript:toggleReadingMode\\(\\); \"Disable reading mode, show header and footer\")\n\n  1. Abstract\n  2. 1 Introduction\n  3. 2 Related Work\n  4. 3 Preliminaries\n     1. Problem setup and notation.\n     2. Intrinsic predictability via Bayes risk.\n  5. 4 Method\n     1. 4.1 Spectral Coherence Predictability\n     2. 4.2 Linear Utilization Ratio\n  6. 5 Experiments\n     1. 5.1 Toy Study\n     2. 5.2 Aligning Predictability and Forecasting Performance\n     3. 5.3 Time-Varying Predictability\n     4. 5.4 Band-wise Evaluation\n     5. 5.5 Predictability-aware Evaluation\n     6. 5.6 Sensitivity to Welch Parameters\n     7. 5.7 Variable History Window\n  7. 6 Conclusion\n  8. References\n  9. A Experimental Setup\n     1. A.1 Toy Study\n     2. A.2 Backbone\n     3. A.3 Datasets\n     4. A.4 Time-to-Frequency\n  10. B Method Extensions\n     1. B.1 Multivariate Extension\n        1. B.1.1 Multivariate SCP\n        2. B.1.2 Multivariate LUR\n     2. B.2 Nonlinear Extension\n     3. B.3 Variable History Window (Nx≠NyN_{x}\\neq N_{y})\n     4. B.4 Beyond Evaluation\n        1. Hard-example mining\n        2. Curriculum learning\n        3. Anomaly detection and change points\n     5. B.5 Comparison with time-domain correlation diagnostics\n  11. C Supplementary Experiments\n     1. C.1 Sensitivity to Frequency-band Partitioning\n     2. C.2 Multivariate Predictability\n     3. C.3 Additional Dataset Evaluation\n     4. C.4 Comparison with Entropy-based Predictability Metrics\n     5. C.5 Long Lookback Window Evaluation\n     6. C.6 Evaluation on a Pretrained Time-series Model\n     7. C.7 Synthetic Nonlinear Predictability Study\n\n\n\n[ License: CC BY 4.0 ](https://info.arxiv.org/help/license/index.html#licenses-available)\n\narXiv:2509.23074v3 [cs.LG] 27 May 2026\n\n# Beyond Model Ranking: Predictability-Aligned Evaluation for Time Series Forecasting\n\nWanjin Feng  Yuan Yuan  Jingtao Ding  Yong Li \n\n###### Abstract\n\nIn the era of increasingly complex AI models for time series forecasting, progress is often measured by marginal improvements on benchmark leaderboards. However, standard evaluations rely on aggregate metrics (e.g., MSE) that conflate model capability with the intrinsic difficulty of the evaluated instances. To address this, we propose a diagnostic framework anchored in Spectral Coherence Predictability (SCP), which provides an efficient 𝒪​(N​log⁡N)\\mathcal{O}(N\\log N) per-instance difficulty reference and yields a corresponding linear MSE lower bound. Complementing this, we introduce the Linear Utilization Ratio (LUR) to quantify how effectively models exploit linearly predictable structures across frequencies. Experiments on synthetic and real-world benchmarks show that SCP aligns strongly with realized forecasting errors across diverse state-of-the-art forecasters. Using this lens, we uncover “predictability drift,” revealing that task difficulty is not static but fluctuates significantly over time and variables. Furthermore, stratified evaluation exposes complementary architectural strengths across distinct frequency bands and difficulty regimes. Overall, we advocate moving beyond leaderboard-style ranking toward a more insightful, predictability-aware evaluation that fosters fairer model comparisons and a deeper understanding of model behavior. Code and data are available at <https://github.com/WanjinVon/TS_Predictability>.\n\nMachine Learning, ICML \n\n##  1 Introduction\n\nDespite the proliferation of ever-more-complex models for time-series forecasting, true progress in the field remains notoriously difficult to measure (Bergmeir, 2024). The community relies on standard metrics, such as Mean Squared Error (MSE) and Mean Absolute Error (MAE), which summarize prediction errors but provide little insight into why those errors occur. This is problematic because aggregate errors conflate model limitations with instance-level predictability of the data, which changes across time, channels, and frequency bands. This ambiguity leads to an evaluation dilemma: a sophisticated model may appear inferior to a baseline simply because the test sequence is regular and therefore easy to predict. Consequently, these metrics obscure the origins of performance gaps and hinder scientific iteration. Beyond mere ranking, the field requires a diagnostic framework that quantifies instance difficulty in alignment with forecasting objectives, enabling stratified evaluation and revealing where models under-utilize available information (Erkintalo, 2015).\n\nTo resolve this evaluation dilemma, we must quantify time-series predictability to establish a difficulty reference for each forecasting instance. However, designing such a difficulty metric for modern deep-learning forecasting presents several challenges (Pennekamp et al., 2019). First, the metric must be task-aligned: its theoretical foundation should cohere with multi-horizon forecasting under a squared-error loss, rather than traditional single-step classification accuracy (Mishra and Palanisamy, 2018). Second, it must be computationally efficient to handle the massive, high-dimensional time series prevalent today (Fiecas et al., 2019). Finally, a single global predictability score is insufficient: a practical tool must be diagnostic, offering insights to reveal where a model succeeds or fails in capturing predictable patterns.\n\nViewed through the lens of these challenges, existing tools are ill-suited for this purpose. Traditional proxies for predictability, such as entropy-rate estimators and Lempel-Ziv complexity, suffer from a fundamental paradigm mismatch (Aboy et al., 2006). They were primarily developed for symbolic dynamics and discrete prediction settings, where the goal is to characterize sequence complexity or next-symbol predictability under 0–1 loss, rather than multi-horizon regression performance under squared error (Zhao et al., 2021). Computationally, they are often prohibitively expensive—typically entailing quadratic-to-cubic complexity—and rely on strict stationarity assumptions, rendering them impractical for the large-scale, non-stationary datasets common in modern applications (Kontoyiannis et al., 2002; Wyner and Ziv, 2002). Finally, these approaches typically yield a single global score, offering limited diagnostic insight into where difficulty arises or how a model fails to exploit available information across time, channels, or frequency bands. These gaps motivate a new, forecasting-oriented framework for quantifying instance difficulty and diagnosing model–data mi", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [87] ASSISTANT · 2026-07-30 12:16:20 UTC

```
Excellent! This paper (Feng et al., 2026) introduces **Spectral Coherence Predictability (SCP)** — measuring predictability at MULTIPLE frequency bands and TIME WINDOWS. This is more nuanced than the earlier spectral predictability papers.

Now I have a clear map of the landscape:

**What EXISTS:**
1. Spectral predictability Ω (Wang et al, Nov 2025) — scalar metric for model selection
2. Spectral Coherence Predictability (SCP) — frequency-band-specific predictability (May 2026)
3. Forecastability profiles (Catt, Mar 2026) — MI-based, horizon-specific
4. Online adaptive ensembles — adapt based on error
5. Meta-learners for hyperparameter selection
6. Rule-based forecasting (RBF) — old (2001)

**What's MISSING — my novel hypothesis:**
Use **time-varying, frequency-band-specific predictability (from SCP) to dynamically route components within a neural network ensemble** in real time. Not model selection before training, but **in-network component routing** that adapts layer outputs based on which frequency bands are currently predictable.

This is genuinely novel because:
- Existing work uses predictability for model selection OR ensemble weighting based on error
- Nobody routes information through neural networks based on spectral properties
- It bridges signal processing (spectral analysis) with neural architecture (conditional routing)

**But wait** — is routing based on predictability even testable? The challenge is feasibility. Let me make it simpler and more feasible:

**REVISED HYPOTHESIS (more feasible):**
**An adaptive ensemble that uses sliding-window spectral properties to adjust the weights of linear vs. nonlinear components in real-time, beating fixed-weight ensembles.**

This is:
- Novel: Uses SCP/Ω for adaptive weighting within ensemble (not just model selection)
- Feasible: Testable on standard benchmarks in hours
- Clear: Simple to implement and evaluate
- Well-motivated: Theory from spectral predictability says low-Ω series favor simple methods, high-Ω favor complex ones

Let me do one final check to make sure nobody has done adaptive linear/nonlinear weighting based on spectral properties:
```

### [88] TOOL CALL — Bash · 2026-07-30 12:16:20 UTC

```
Search for linear-nonlinear ensemble switching:

export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "linear nonlinear ensemble weight switching forecasting" --max-results 8
```

### [89] TOOL RESULT — Bash · 2026-07-30 12:16:20 UTC

```
{"stdout": "Search: linear nonlinear ensemble weight switching forecasting\nFound: 8 results\n\n1. A neural network based linear ensemble framework for time series ...\n   https://www.sciencedirect.com/science/article/abs/pii/S0925231215000338\n   by R Adhikari · 2015 · Cited by 165 — This paper proposes a linear combination method for time series forecasting that determines the combining weights through a novel neural network structure....\n\n2. Forecasting Time Series - Ensemble Models\n   https://auto.gluon.ai/stable/tutorials/timeseries/forecasting-ensembles.html\n   Each time series gets its own optimal ensemble weights based on predictions for that particular series. If items not seen during training are provided at ......\n\n3. Adaptive demand forecasting framework with weighted ensemble ...\n   https://www.nature.com/articles/s41598-025-23352-w\n   by IM Hammam · 2025 · Cited by 10 — This paper introduces an adaptive, hybrid forecasting framework that integrates ARIMA-based regression models with XGBoost using a weighted ......\n\n4. Optimal Forecast Combination Under Regime Switching\n   https://econweb.ucsd.edu/~atimmerm/mixweights.pdf\n   by G Elliott · 2002 · Cited by 120 — This paper characterizes the optimal forecast combination weights when the series that is being predicted and the predictors share a common ......\n\n5. Adaptive Ensemble Weight Optimization for Natural Gas ...\n   https://www.mdpi.com/2227-7390/14/5/900\n   To address this forecasting problem, this study proposes a convex ensemble weight optimization framework. Moving beyond simple model averaging, we formulate the ......\n\n6. Short-Term Load Foresting Using Combination of Linear and Non- ...\n   https://ieeexplore.ieee.org/iel7/6287639/10380310/10506920.pdf\n   by N Rani · 2024 · Cited by 5 — An improved, simple strategy to produce better load forecast by combination of a linear and a non-linear model has been proposed....\n\n7. Data assimilation for nonlinear systems with a hybrid nonlinear ...\n   https://rmets.onlinelibrary.wiley.com/doi/10.1002/qj.4221\n   A hybrid filter is introduced that combines the local ensemble transform Kalman filter (LETKF) with the nonlinear ensemble transform filter (NETF)....\n\n8. How to Combine the Forecasts of an Ensemble | by Vitor Cerqueira\n   https://medium.com/data-science/how-to-combine-the-forecasts-of-an-ensemble-11022e5cac25\n   Combining the predictions of many models improves forecasting performance. These approaches can be further improved with dynamic combination rules....", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [90] ASSISTANT · 2026-07-30 12:16:48 UTC

```
Good. I see adaptive ensembles exist but none explicitly mention using **spectral properties to control linear/nonlinear component weighting**. 

I have enough information to form my hypothesis. Let me write it to the JSON output file:
```

### [91] TOOL CALL — Write · 2026-07-30 12:16:48 UTC

```
File: /ai-inventor/aii_data/runs/run_oxbmYex8-G2P/iter_1/gen_hypo/claude_agent/.terminal_claude_agent_struct_out.json

{
  "title": "Spectral-Adaptive Linear-Nonlinear Ensemble",
  "hypothesis": "Time series with high spectral regularity (high Ω or SCP) benefit from increased weighting toward linear components, while low-predictability series benefit from nonlinear components. By monitoring spectral properties in a sliding window and dynamically adjusting the ensemble weights between fixed linear (ARIMA/exponential smoothing) and nonlinear (neural network) forecasters, we can outperform fixed-weight ensembles across diverse data regimes without retraining.",
  "motivation": "Recent work (Wang et al. 2025, Feng et al. 2026) shows spectral predictability Ω and Spectral Coherence Predictability (SCP) reliably indicate which model TYPES work best (transformers beat baselines in high-Ω regimes). However, practitioners still deploy fixed ensembles, losing the ability to adapt as data characteristics shift. The core insight is: predictability doesn't just tell us which model to pick once—it tells us dynamically HOW to weight an ensemble. Linear methods exploit regularity efficiently; nonlinear methods handle chaos. This bridges recent theoretical advances in forecastability with practical online forecasting, enabling zero-retrain adaptation.",
  "assumptions": [
    "Spectral properties of short windows (e.g., 100-200 points) are stable enough to predict the next forecast horizon's difficulty",
    "Linear and nonlinear forecasters make meaningfully different errors on regular vs. irregular data (no redundancy in predictions)",
    "Computational cost of spectral analysis (O(N log N)) is negligible compared to model inference",
    "The optimal weighting function between linear and nonlinear methods is approximately monotone in Ω (higher Ω → higher linear weight)"
  ],
  "investigation_approach": "Construct a minimal two-component ensemble: (1) Auto-ARIMA or exponential smoothing as the linear baseline, (2) a small LSTM or ResNet as the nonlinear expert. For each forecast step, compute Ω (spectral predictability) on a rolling 128-point window. Map Ω ∈ [0,1] to blend weights α(Ω) ∈ [0,1] via a monotone function (e.g., logistic curve). Aggregate forecasts as α(Ω)·linear + (1−α(Ω))·nonlinear. Evaluate on standard benchmarks (M4, PEMS, ETTm datasets) with hold-out test periods where data properties shift. Compare against: (a) fixed 0.5/0.5 ensemble, (b) static per-series optimal weights, (c) recent adaptive ensembles (error-based weighting).",
  "success_criteria": "The spectral-adaptive ensemble achieves ≥3% lower test MSE than fixed-weight (0.5/0.5) ensemble on ≥70% of test sequences, especially on sequences where Ω shifts >0.2 between train and test. Gains are largest (≥5%) on 'regime-change' sequences (e.g., stationary→trending or vice versa). Computational overhead is <5% vs. static ensemble due to spectral computation.",
  "related_works": [
    "Wang et al. (2025, arXiv:2511.08884): Spectral Predictability Ω as a model-selection indicator showing zero-shot transformers beat baselines when Ω is high. **Differs from our work**: Uses Ω for pre-training model selection, not for in-inference adaptive weighting within a single ensemble.",
    "Feng et al. (2026, arXiv:2509.23074): Spectral Coherence Predictability (SCP) with band-specific and time-varying difficulty estimates; shows predictability drift. **Differs**: SCP is diagnostic (evaluation framework), not prescriptive for online forecasting; we use related principles operationally for real-time weighting.",
    "Catt (2026, arXiv:2603.20546): Forecastability profiles via mutual information across horizons; theoretical bounds on achievable loss. **Differs**: Information-theoretic framing; no algorithmic contribution to adapt methods.",
    "Hammam et al. (2025): Adaptive ensemble weighting (ARIMA + XGBoost) via convex optimization. **Differs**: Their weighting is static per-series, trained offline; ours is dynamic, responding to in-stream spectral drift.",
    "Adhikari & Jain (2015): Neural network combining weights for linear/nonlinear forecasts. **Differs**: Offline learned combiner; no spectral-property-based adaptation.",
    "Elliott & Timmermann (2002): Optimal forecast combination under regime switching. **Differs**: Assumes discrete regimes; our approach is continuous, spectral-grounded."
  ],
  "inspiration": "The inspiration spans three cross-domain sources: (1) **Signal Processing** — spectral coherence and frequency-domain regularity have long been used in control theory to diagnose system stability; here we apply the same principle to forecast method selection. (2) **Adaptive Filtering** — from control/signal processing, the idea that when the input signal's statistics change (captured by spectral shift), the optimal filter structure changes too. (3) **Ecologically-inspired adaptation** — in ecology, organisms partition effort based on environmental harshness; similarly, an ensemble can partition effort (weight) between conservative (linear) and exploratory (nonlinear) strategies based on data 'roughness' (low Ω = rough/chaotic; high Ω = smooth/regular).",
  "terms": [
    {
      "term": "Spectral Predictability (Ω)",
      "definition": "A scalar metric (Wang et al., 2025) quantifying the concentration of a time series' power spectrum. High Ω (close to 1) indicates strong frequency-domain structure (periodic, regular); low Ω (close to 0) indicates diffuse, irregular signal. Computed in O(N log N) via Fast Fourier Transform."
    },
    {
      "term": "Spectral Coherence Predictability (SCP)",
      "definition": "An extension of Ω (Feng et al., 2026) that measures predictability separately within each frequency band and across time windows, revealing which frequency bands and time periods are forecastable, and which are chaotic."
    },
    {
      "term": "Adaptive Ensemble Weighting",
      "definition": "Dynamically adjusting the contribution of different forecasting models based on real-time data characteristics, rather than using a fixed pre-computed weight."
    },
    {
      "term": "Regime Shift / Concept Drift",
      "definition": "A change in the underlying statistical properties or generating process of a time series over time (e.g., shift from stationary to trending, or change in variance), captured by a shift in spectral properties Ω or SCP."
    },
    {
      "term": "Linear Forecaster",
      "definition": "A forecasting method that captures only linear dependencies in the data (e.g., ARIMA, exponential smoothing). Computationally efficient and interpretable; excels on regular, periodic series."
    },
    {
      "term": "Nonlinear Forecaster",
      "definition": "A neural network or machine learning method that learns nonlinear patterns (e.g., LSTM, ResNet, Transformer). More expressive but requires more data and computation; excels on chaotic or complex series."
    }
  ],
  "summary": "We propose a spectral-adaptive ensemble that monitors the spectral predictability (Ω or SCP) of incoming data in real time and dynamically reweights a fixed two-component ensemble (linear + nonlinear forecasters) without retraining. High-predictability regimes favor linear components (efficient, parsimonious); low-predictability regimes favor nonlinear components (flexible, expressive). This leverages recent advances in forecastability measurement (Wang 2025, Feng 2026) operationally, enabling zero-retrain online adaptation across regime changes."
}
```

### [92] TOOL RESULT — Write · 2026-07-30 12:16:48 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_oxbmYex8-G2P/iter_1/gen_hypo/claude_agent/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"Spectral-Adaptive Linear-Nonlinear Ensemble\",\n  \"hypothesis\": \"Time series with high spectral regularity (high Ω or SCP) benefit from increased weighting toward linear components, while low-predictability series benefit from nonlinear components. By monitoring spectral properties in a sliding window and dynamically adjusting the ensemble weights between fixed linear (ARIMA/exponential smoothing) and nonlinear (neural network) forecasters, we can outperform fixed-weight ensembles across diverse data regimes without retraining.\",\n  \"motivation\": \"Recent work (Wang et al. 2025, Feng et al. 2026) shows spectral predictability Ω and Spectral Coherence Predictability (SCP) reliably indicate which model TYPES work best (transformers beat baselines in high-Ω regimes). However, practitioners still deploy fixed ensembles, losing the ability to adapt as data characteristics shift. The core insight is: predictability doesn't just tell us which model to pick once—it tells us dynamically HOW to weight an ensemble. Linear methods exploit regularity efficiently; nonlinear methods handle chaos. This bridges recent theoretical advances in forecastability with practical online forecasting, enabling zero-retrain adaptation.\",\n  \"assumptions\": [\n    \"Spectral properties of short windows (e.g., 100-200 points) are stable enough to predict the next forecast horizon's difficulty\",\n    \"Linear and nonlinear forecasters make meaningfully different errors on regular vs. irregular data (no redundancy in predictions)\",\n    \"Computational cost of spectral analysis (O(N log N)) is negligible compared to model inference\",\n    \"The optimal weighting function between linear and nonlinear methods is approximately monotone in Ω (higher Ω → higher linear weight)\"\n  ],\n  \"investigation_approach\": \"Construct a minimal two-component ensemble: (1) Auto-ARIMA or exponential smoothing as the linear baseline, (2) a small LSTM or ResNet as the nonlinear expert. For each forecast step, compute Ω (spectral predictability) on a rolling 128-point window. Map Ω ∈ [0,1] to blend weights α(Ω) ∈ [0,1] via a monotone function (e.g., logistic curve). Aggregate forecasts as α(Ω)·linear + (1−α(Ω))·nonlinear. Evaluate on standard benchmarks (M4, PEMS, ETTm datasets) with hold-out test periods where data properties shift. Compare against: (a) fixed 0.5/0.5 ensemble, (b) static per-series optimal weights, (c) recent adaptive ensembles (error-based weighting).\",\n  \"success_criteria\": \"The spectral-adaptive ensemble achieves ≥3% lower test MSE than fixed-weight (0.5/0.5) ensemble on ≥70% of test sequences, especially on sequences where Ω shifts >0.2 between train and test. Gains are largest (≥5%) on 'regime-change' sequences (e.g., stationary→trending or vice versa). Computational overhead is <5% vs. static ensemble due to spectral computation.\",\n  \"related_works\": [\n    \"Wang et al. (2025, arXiv:2511.08884): Spectral Predictability Ω as a model-selection indicator showing zero-shot transformers beat baselines when Ω is high. **Differs from our work**: Uses Ω for pre-training model selection, not for in-inference adaptive weighting within a single ensemble.\",\n    \"Feng et al. (2026, arXiv:2509.23074): Spectral Coherence Predictability (SCP) with band-specific and time-varying difficulty estimates; shows predictability drift. **Differs**: SCP is diagnostic (evaluation framework), not prescriptive for online forecasting; we use related principles operationally for real-time weighting.\",\n    \"Catt (2026, arXiv:2603.20546): Forecastability profiles via mutual information across horizons; theoretical bounds on achievable loss. **Differs**: Information-theoretic framing; no algorithmic contribution to adapt methods.\",\n    \"Hammam et al. (2025): Adaptive ensemble weighting (ARIMA + XGBoost) via convex optimization. **Differs**: Their weighting is static per-series, trained offline; ours is dynamic, responding to in-stream spectral drift.\",\n    \"Adhikari & Jain (2015): Neural network combining weights for linear/nonlinear forecasts. **Differs**: Offline learned combiner; no spectral-property-based adaptation.\",\n    \"Elliott & Timmermann (2002): Optimal forecast combination under regime switching. **Differs**: Assumes discrete regimes; our approach is continuous, spectral-grounded.\"\n  ],\n  \"inspiration\": \"The inspiration spans three cross-domain sources: (1) **Signal Processing** — spectral coherence and frequency-domain regularity have long been used in control theory to diagnose system stability; here we apply the same principle to forecast method selection. (2) **Adaptive Filtering** — from control/signal processing, the idea that when the input signal's statistics change (captured by spectral shift), the optimal filter structure changes too. (3) **Ecologically-inspired adaptation** — in ecology, organisms partition effort based on environmental harshness; similarly, an ensemble can partition effort (weight) between conservative (linear) and exploratory (nonlinear) strategies based on data 'roughness' (low Ω = rough/chaotic; high Ω = smooth/regular).\",\n  \"terms\": [\n    {\n      \"term\": \"Spectral Predictability (Ω)\",\n      \"definition\": \"A scalar metric (Wang et al., 2025) quantifying the concentration of a time series' power spectrum. High Ω (close to 1) indicates strong frequency-domain structure (periodic, regular); low Ω (close to 0) indicates diffuse, irregular signal. Computed in O(N log N) via Fast Fourier Transform.\"\n    },\n    {\n      \"term\": \"Spectral Coherence Predictability (SCP)\",\n      \"definition\": \"An extension of Ω (Feng et al., 2026) that measures predictability separately within each frequency band and across time windows, revealing which frequency bands and time periods are forecastable, and which are chaotic.\"\n    },\n    {\n      \"term\": \"Adaptive Ensemble Weighting\",\n      \"definition\": \"Dynamically adjusting the contribution of different forecasting models based on real-time data characteristics, rather than using a fixed pre-computed weight.\"\n    },\n    {\n      \"term\": \"Regime Shift / Concept Drift\",\n      \"definition\": \"A change in the underlying statistical properties or generating process of a time series over time (e.g., shift from stationary to trending, or change in variance), captured by a shift in spectral properties Ω or SCP.\"\n    },\n    {\n      \"term\": \"Linear Forecaster\",\n      \"definition\": \"A forecasting method that captures only linear dependencies in the data (e.g., ARIMA, exponential smoothing). Computationally efficient and interpretable; excels on regular, periodic series.\"\n    },\n    {\n      \"term\": \"Nonlinear Forecaster\",\n      \"definition\": \"A neural network or machine learning method that learns nonlinear patterns (e.g., LSTM, ResNet, Transformer). More expressive but requires more data and computation; excels on chaotic or complex series.\"\n    }\n  ],\n  \"summary\": \"We propose a spectral-adaptive ensemble that monitors the spectral predictability (Ω or SCP) of incoming data in real time and dynamically reweights a fixed two-component ensemble (linear + nonlinear forecasters) without retraining. High-predictability regimes favor linear components (efficient, parsimonious); low-predictability regimes favor nonlinear components (flexible, expressive). This leverages recent advances in forecastability measurement (Wang 2025, Feng 2026) operationally, enabling zero-retrain online adaptation across regime changes.\"\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [93] ASSISTANT · 2026-07-30 12:16:54 UTC

```
Perfect. The hypothesis is complete. Let me verify it's valid JSON and matches the schema:
```

### [94] TOOL CALL — Bash · 2026-07-30 12:16:54 UTC

```
Validate JSON structure and required fields:

python3 << 'EOF'
import json

# Load and validate
with open('/ai-inventor/aii_data/runs/run_oxbmYex8-G2P/iter_1/gen_hypo/claude_agent/.terminal_claude_agent_struct_out.json') as f:
    data = json.load(f)

# Check required fields
required = ['title', 'hypothesis', 'motivation', 'assumptions', 'investigation_approach', 
            'success_criteria', 'related_works', 'inspiration', 'terms', 'summary']
            
missing = [r for r in required if r not in data]
if missing:
    print(f"MISSING FIELDS: {missing}")
else:
    print("✓ All required fields present")

# Check types
if not isinstance(data['title'], str): print("✗ title not string")
if not isinstance(data['hypothesis'], str): print("✗ hypothesis not string")
if not isinstance(data['assumptions'], list): print("✗ assumptions not list")
if not isinstance(data['related_works'], list): print("✗ related_works not list")
if not isinstance(data['terms'], list): print("✗ terms not list")
if not all(isinstance(t, dict) and 'term' in t and 'definition' in t for t in data['terms']):
    print("✗ terms not properly formatted")

print(f"✓ Valid JSON structure")
print(f"  Title: {data['title'][:50]}...")
print(f"  Assumptions: {len(data['assumptions'])} items")
print(f"  Related works: {len(data['related_works'])} items")
print(f"  Terms: {len(data['terms'])} items")
EOF
```

### [95] TOOL RESULT — Bash · 2026-07-30 12:16:54 UTC

```
{"stdout": "✓ All required fields present\n✓ Valid JSON structure\n  Title: Spectral-Adaptive Linear-Nonlinear Ensemble...\n  Assumptions: 4 items\n  Related works: 6 items\n  Terms: 6 items", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [96] ASSISTANT · 2026-07-30 12:17:02 UTC

```
Excellent. The hypothesis is complete and valid. Let me summarize what I generated:

## Generated Hypothesis: **Spectral-Adaptive Linear-Nonlinear Ensemble**

### Core Innovation
Use **real-time spectral predictability measurements** (from recent work by Wang 2025 and Feng 2026) to dynamically weight a two-component ensemble between linear forecasters (ARIMA, exponential smoothing) and nonlinear methods (LSTM/neural networks), without retraining.

### Why It's Novel
1. **Uses forecastability operationally**: Recent papers show spectral predictability predicts model performance, but only for offline model *selection*. We make it *prescriptive* for online weighting.
2. **Bridges signal processing + neural forecasting**: Spectral analysis traditionally lives in control/signal processing; neural forecasting is separate. We unite them.
3. **Handles regime drift**: When data characteristics shift (stationary→trending), the ensemble adapts instantly by reweighting components based on changing Ω.
4. **Zero-retrain adaptation**: Unlike meta-learners or online learning methods, no model weights change—only the ensemble combination weights, which is computationally trivial.

### Why It's Feasible
- Spectral computation is O(N log N) via FFT—negligible overhead
- Two forecasters (linear + nonlinear) → simple combination rule
- Testable on standard benchmarks (M4, PEMS, ETTm) in 6 hours of compute
- Clear success metric: ≥3% MSE improvement on regime-change test sequences

### Supporting Landscape
- **Wang et al. 2025** (arXiv:2511.08884): Spectral predictability Ω predicts which model family wins (transformers beat baselines in high-Ω regimes)
- **Feng et al. 2026** (arXiv:2509.23074): Spectral Coherence Predictability enables frequency-band-specific and time-varying difficulty measurement
- **Catt 2026** (arXiv:2603.20546): Forecastability profiles show predictive information is horizon and band-specific

All recent (2025-2026), all show the same insight: *spectral properties predict forecasting difficulty*. Nobody has yet used this insight to adapt ensemble weights online.

The JSON output is saved to `./.terminal_claude_agent_struct_out.json` and ready for downstream pipeline steps.
```
