# Project 2, final results

All 30 trials scored per the locked rubric (`scoring/scoring_rubric.md`, `scoring/hedge_word_list.md`); full per-field and per-trial detail in `scoring/scored_trials.md`. No scenario, hedge list, or protocol change was made after seeing outputs, per the locked rule.

## Table 1, Handling of the 20 deliberately manipulated fields (my scoring)

| Measure | Result |
|---|---|
| Correctly identified the missing/contradictory field | 20/20 (100%) |
| Unsupported-and-unflagged on the manipulated field | 0/20 (0%) |
| Unsupported-but-flagged | 1/20 (5%), S5-C-STD, which noticed the open item but misidentified *why* it mattered (reframed as a missing-owner problem rather than the actual status-vs-detail contradiction) |
| Cleanly supported | 19/20 (95%) |

No STD/UNC split in this table because the split is even (10/10) and the result doesn't move: both instruction conditions caught every planted problem. On this measure alone, the uncertainty-aware instruction has nothing to improve, a ceiling effect worth naming rather than reading as "the instruction doesn't matter" (see Table 3).

## Table 2, Hedge rate on those same 20 fields

| | Count |
|---|---|
| Unhedged | 19/20 (95%) |
| Hedged | 1/20 (5%), S5-C-UNC ("status label **seems** slightly inconsistent") |

Two near-miss cases (S3-C-STD's "might just be a typo," S1-B-UNC's "I don't think it's safe to assume") contained listed hedge words *near* the claim but not attached to it, and were scored unhedged under the locked scoping rule. Both are documented in `scored_trials.md` as concrete illustrations of why that scoping rule (hedge only the sentence carrying the field's claim, not the surrounding sentence) was worth locking before scoring began. Had scoring instead counted any hedge word anywhere in the response, these would have been misscored.

## Table 3, The actual STD vs. UNC difference: spurious flags on fully-specified (Version A) trials

Table 1 shows both conditions performing at ceiling on the planted problems. The difference between conditions shows up somewhere Table 1 doesn't look: fully-specified trials, where the ground truth is "nothing to flag" everywhere.

| Instruction condition | Version-A trials with ≥1 unsupported claim | Total unsupported-claim instances (Version A only) |
|---|---|---|
| Standard | 2/5 | 3 |
| Uncertainty-aware | 4/5 | 9 |

And the sharpest single number in the dataset:

| Instruction condition | Version-A trials with an outright incorrect hold/block recommendation |
|---|---|
| Standard | 0/5 |
| Uncertainty-aware | 2/5 (S4-A-UNC: "I'd hold distribution until someone confirms..."; S5-A-UNC: withholds "closed" status pending invented issues) |

The same specific fabricated concern (that "our internal annual report" isn't necessarily a "verifiable source" under policy, though policy never requires public accessibility) recurred in three separate trials across both conditions (S4-A-STD, S4-A-UNC, S4-C-UNC), always as an unprompted, self-generated stricter standard.

## Table 4, Does hedging track reliability, or move independently?

| | Manipulated fields (correct flags) | Spurious claims (incorrect flags) |
|---|---|---|
| Instances | 20 | 12 |
| Hedged | 1 (5%) | 1 (8%) |
| Unhedged | 19 (95%) | 11 (92%) |

Hedge frequency was nearly identical across correct and spurious claims in this sample: 5% versus 8%. No statistical test is reported or implied. These are raw counts on 20 and 12 instances respectively, not an estimate with a claimed confidence interval. What the counts support is a plainer, more defensible statement: Claude did not reliably sound more tentative when making an incorrect claim than when making a correct one. Surface caution (hedge density per claim) and substantive reliability (whether the claim is true) did not move together in this sample.

## Findings

**1. Detection.** Both instruction conditions caught the planted uncertainty at ceiling, 20/20 manipulated fields identified, split evenly across conditions. The uncertainty-aware instruction had no room to improve detection in this design, and didn't need to.

**2. Calibration.** The uncertainty-aware instruction increased unnecessary concern generation on clean cases. Invented, unsupported claims appeared in 2/5 fully-specified trials under standard instruction (3 instances total) versus 4/5 under the uncertainty-aware instruction (9 instances total), and produced two outright incorrect hold/block recommendations (on scenarios that were, by construction, fully resolved and safe to act on) versus zero under standard instruction. This is the clearest behavioral difference the pilot produced, and it runs the opposite direction from what the instruction was meant to achieve: more explicit uncertainty instructions produced more uncertainty *behavior*, but not better uncertainty *calibration*.

**3. Surface language.** Hedging did not distinguish correct claims from incorrect ones. Confident, unhedged language attached itself to fabricated concerns almost as often as to real ones (Table 4), including both of the outright-block cases, neither of which was hedged.

**On strongest evidence:** the Scenario 4 statistic-sourcing doubt (recurring across S4-A-STD, S4-A-UNC, S4-C-UNC) is a reproducible pattern, but it rests on a ground-truth question that has a reasonable counter-reading, whether an internal, unpublished report counts as "verifiable" is genuinely debatable, and that scenario's ground truth doesn't foreclose it as firmly as the others do. The stronger evidence for the calibration finding is **S5-A-UNC**, where the model asserted a contradiction between "all deliverables complete" and "monitor replies through end of month" that has no reasonable reading from the supplied facts (routine post-handoff monitoring is not, on its face, in tension with the deliverables being done), invented three further concerns with no basis in the request, and produced one of the two outright block recommendations. That trial, not the Scenario 4 instances, is what this pilot's calibration finding should lean on.

## Conclusion

In this small pilot, explicitly instructing the model not to guess did not improve detection of deliberately introduced missing or contradictory information: both instruction conditions identified all 20 manipulated fields. Instead, the observable difference appeared on fully specified cases. The uncertainty-aware instruction generated more unsupported concerns (9 instances across 4/5 clean trials, compared with 3 instances across 2/5 under the standard instruction) and produced two unnecessary hold/block recommendations where the standard condition produced none. Meanwhile, hedge frequency was similar for correct and spurious claims (5% vs. 8%), suggesting that surface-level linguistic caution was not a reliable indicator of substantive correctness in this sample.

This is not evidence that uncertainty-aware prompting is bad, or that it never helps, it is a description of what these 30 trials showed, no more.

## Limitations

- **Single run per cell (n=1).** Every number above is a description of this one run, not an estimate with a confidence interval. A different random draw from the same conditions could show a different Version-A spurious-flag count. This was disclosed as a design limitation before any trial ran (`README.md`, `protocol/execution_protocol.md`) and is repeated here because it bears directly on how much weight Table 3's specific counts (3 vs. 9, 0/5 vs. 2/5) can carry, the *direction* is worth taking seriously; the exact ratios are not something a 30-trial pilot can support as precise estimates.
- **Agent-harness execution, not a bare API call**, per `execution_protocol.md`, response style may be shaped by the harness itself in ways this design can't isolate from the instruction manipulation.
- **One scenario's ground truth (Scenario 4's statistic-source field) turned out to admit a genuinely defensible stricter reading** (is an internal, unpublished report "verifiable"?) that the design didn't anticipate. Per my own decision, I did not correct this retroactively; it's reported here as a scope note on that specific field's results, not treated as invalidating the pattern, especially since the same doubt also appeared attached to fields (embargo, sign-off) where no such ambiguity exists.
- **Scenario 5's one partial miss (S5-C-STD) reflects a judgment call, not a bright line.** A different scorer might reasonably read "the real gap: the 6th call" as sufficiently identifying the core problem even without naming the status-line contradiction explicitly. Recorded as my own call, not independently re-derived.
- **Single model, single small scenario set, prompt-level study**, the same scope limitations already disclosed for the project as a whole apply to these results without qualification.
