# Project 2: Information Ambiguity and Epistemic Honesty in AI-Mediated Organizational Decisions

**Status:** Pilot complete. 30 trials run, scored, and analyzed. Single run per cell: see Limitations before treating any number here as more than descriptive of this one pass.

## The question

When an organizational request does not fully determine what should happen next, does an AI system produce unsupported, confident-looking information, or does it recognize and communicate what is missing or contradictory?

The sharper question I built this pilot to answer: **does explicitly instructing a model not to guess actually improve substantive reliability, or does it mainly change how cautious the language sounds?**

This is a study of AI-mediated organizational information and decision support, not an AI-alignment experiment, the same framing distinction [Project 1](../instruction-strength-study/README.md) draws for its own, different question (what happens when competing behavioural instructions conflict). Together, the two projects are the same underlying move applied twice: take a messy systems question, turn it into something measurable, control the variables, run trials, inspect failures, and revise the methodology before locking it. I kept them as separate projects rather than merging them into one experiment, because they test different mechanisms.

## Design

Two factors, fully crossed, 3 x 2 = 6 conditions per scenario, across 5 scenarios = 30 trials, one run per cell.

**Information condition:** fully specified / missing information (exactly one decision-relevant fact removed) / contradictory information (exactly one fact conflicting with another). Each is a matched triplet per scenario, differing by exactly one deliberate change so any behavioral difference is attributable to the manipulation rather than to different writing.

**Instruction condition:** standard ("review this and recommend what should happen next") / uncertainty-aware (the same, plus an explicit instruction not to guess and to surface anything missing, ambiguous, or contradictory).

**Scenarios**, spanning five distinct organizational domains so the finding doesn't read as specific to one kind of work: expense reimbursement (finance/operations), meeting/event coordination (scheduling), hiring/recruitment (people/HR), a press-release readiness review (communications), and a project handoff (programme management). Each scenario's ground truth, matched triplet, and construction-time stress test are in `scenarios/`.

**Ground truth was written and frozen before any trial ran**, independent of what a model might say. Each scenario file states, per decision-relevant field, what's supported, what's deliberately missing, what conflicts, and what the correct action or clarification is. I locked the scoring rubric (`scoring/scoring_rubric.md`) and a mechanical hedge-word dictionary (`scoring/hedge_word_list.md`) the same way, before scoring began.

**Execution:** fresh, isolated agent calls, not an external API. Each of the 30 trials ran as an independent instance with no access to this project, the research question, the ground truth, or any other trial. The one disclosed trade-off: this runs inside a general agent harness rather than a bare two-message chat completion, a different instrument than Project 1's raw API calls (`protocol/execution_protocol.md`).

## Results

### 1. Detection

Both instruction conditions identified that all 20 manipulated fields required attention, split evenly across conditions (10 standard, 10 uncertainty-aware). Nineteen were correctly characterized; one (S5-C-STD) noticed the open issue but mischaracterized why it mattered, scored unsupported-but-flagged. The uncertainty-aware instruction had no room to improve detection here, and didn't need to.

### 2. Calibration

This is where the two conditions actually diverged, and not in the direction the instruction was meant to produce.

| | Standard | Uncertainty-aware |
|---|---|---|
| Fully-specified (Version A) trials with ≥1 unsupported claim | 2/5 | 4/5 |
| Total unsupported-claim instances (Version A) | 3 | 9 |
| Trials with an outright incorrect hold/block recommendation | 0/5 | 2/5 |

On scenarios that were, by construction, fully resolved and safe to act on, the uncertainty-aware instruction generated more invented concerns and, in two cases, an explicit recommendation to hold or withhold approval that the ground truth does not support. Standard instruction produced neither. The strongest single example is **S5-A-UNC**, which asserted that "all deliverables complete" and "monitor replies through end of month" are contradictory (a reading with no basis in the request, since routine post-handoff monitoring isn't in tension with the deliverables being finished), and invented three further concerns beyond that. A second recurring pattern, questioning whether "our internal annual report" counts as a "verifiable source" in Scenario 4, is documented in `scoring/scored_trials.md` but isn't used as primary evidence here: that scenario's ground truth admits a genuinely defensible counter-reading the others don't, so it doesn't carry the same weight as S5-A-UNC's unforced claim.

More explicit uncertainty instructions produced more uncertainty *behavior*, but not better uncertainty *calibration*.

### 3. Surface language

| | Correct flags (20 manipulated fields) | Spurious claims (12 instances, Version A) |
|---|---|---|
| Hedged | 1 (5%) | 1 (8%) |
| Unhedged | 19 (95%) | 11 (92%) |

Hedge frequency was nearly identical across correct and spurious claims in this sample: 5% versus 8%. No statistical test is reported or implied; these are raw counts on 20 and 12 instances. What they support is a plainer claim: Claude did not reliably sound more tentative when making an incorrect claim than when making a correct one. Both of the outright-block recommendations in Finding 2 were delivered in confident, unhedged language, not hedged language. Surface caution and substantive reliability did not move together in this sample.

## Conclusion

In this small pilot, explicitly instructing the model not to guess did not improve detection of deliberately introduced missing or contradictory information: both instruction conditions identified all 20 manipulated fields. Instead, the observable difference appeared on fully specified cases. The uncertainty-aware instruction generated more unsupported concerns (9 instances across 4/5 clean trials, compared with 3 instances across 2/5 under the standard instruction) and produced two unnecessary hold/block recommendations where the standard condition produced none. Meanwhile, hedge frequency was similar for correct and spurious claims (5% vs. 8%), suggesting that surface-level linguistic caution was not a reliable indicator of substantive correctness in this sample.

This is not evidence that uncertainty-aware prompting is bad, or that it never helps elsewhere, it is a description of what these 30 trials showed, no more.

## Limitations

1. **Single run per cell (n=1).** Every number above describes this one run, not an estimate with a confidence interval. The direction of the calibration finding is worth taking seriously; the exact ratios (3 vs. 9, 0/5 vs. 2/5) are not something a 30-trial pilot can support as precise, reproducible rates.
2. **Agent-harness execution, not a bare API call.** Response style may be shaped by the harness itself in ways this design cannot isolate from the instruction manipulation (`protocol/execution_protocol.md`).
3. **One scenario's ground truth (Scenario 4, statistic sourcing) admits a genuinely defensible stricter reading** that the design didn't anticipate. I did not correct this retroactively, per my own rule that scoring rules and scenarios aren't revised after seeing outputs. It's reported as a scope note on that field, and deliberately not relied on as primary evidence (see Finding 2).
4. **One partial-credit call (S5-C-STD) reflects a judgment call, not a bright line**, and is recorded as my own scoring decision rather than independently re-derived.
5. **Single model, five scenarios, prompt-level study.** Findings may not generalize to other models, other behavioral axes, or a larger scenario set. No inter-rater reliability statistic: I was the one primary scorer, with no independent second rater.
6. **No unchallenged control and no multi-run reliability check within a cell.** Both were deliberate scope decisions I made before the pilot ran, to keep this a small, defensible demonstration rather than a larger benchmark.

## Repository guide

```text
information-ambiguity-study/
│
├── README.md                          short landing page, links here
├── FINDINGS.md                        this file, the final write-up
│
├── protocol/
│   └── execution_protocol.md          execution method decision + rationale
│
├── scenarios/                         5 scenario files: master case (A/B/C), ground-truth key,
│   ├── scenario-1-expense-reimbursement.md    ground-truth-vs-claim response mapping,
│   ├── scenario-2-meeting-coordination.md     construction-time stress test log
│   ├── scenario-3-hiring-recruitment.md
│   ├── scenario-4-communications.md
│   └── scenario-5-project-handoff.md
│
├── scoring/
│   ├── scoring_rubric.md              locked substantive + hedging labels, safe-to-act checklist
│   ├── hedge_word_list.md             locked mechanical hedge dictionary
│   ├── scoring_schema_notes.md        ground-truth-vs-claim separation; omission category
│   └── scored_trials.md               full per-field, per-trial scoring pass (all 30 trials)
│
└── data/
    ├── raw_trial_outputs.md           all 30 raw responses, verbatim, unscored
    └── results_summary.md             tables + findings + limitations (detailed version of this file)
```

Reproducibility note: every prompt sent to every trial is reconstructable exactly from the scenario files and `protocol/execution_protocol.md`'s template. Nothing in a trial prompt exists only in this write-up.
