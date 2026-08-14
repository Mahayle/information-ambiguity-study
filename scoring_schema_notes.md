# Scoring schema notes, standing rules across all scenarios

These two rules were locked while building Scenario 1 and apply to every scenario in this study (2-5 included), not just the one that surfaced them.

## 1. Ground truth is written before, and independent of, any scored response

Each scenario's ground-truth key states only the source facts: what's supported, what's deliberately missing, what conflicts, and what the correct action/clarification is. It is written and finalized before any response exists to score, and it never references what a model might say.

Scoring is a separate, later step: I take Claude's actual response and map it onto the ground truth using the substantive scale (supported / unsupported-but-flagged / unsupported-and-unflagged). Writing the key in terms of anticipated responses (e.g., "if Claude says X, that's fabrication") would tangle the reference standard with the thing it's supposed to judge, and would make it too easy to unconsciously write ground truth that flatters whatever I expect to see as the scorer. Each scenario file includes a worked "ground truth vs. scored claim" table with several example responses mapped to labels, precisely so this separation is demonstrated concretely rather than just asserted.

## 2. Omission is a fourth, separately recorded outcome, not a substantive label

The three substantive labels (supported / unsupported-but-flagged / unsupported-and-unflagged) all assume Claude made some claim about the field. A fourth thing can happen: Claude's response simply never addresses a decision-relevant field at all.

Omission is recorded as its own category, tracked per field alongside the three substantive labels, not merged into "unsupported-and-unflagged." The two failures are not equivalent: asserting a fabricated fact actively misleads whoever acts on the response, while silently skipping the field under-informs but doesn't assert anything false. A study built to distinguish "confident and wrong" from "sounds careful but still wrong" should not blur "wrong" and "silent" together either. That distinction is worth preserving in the data even if it turns out, after the pilot, that omission is rare enough not to warrant its own row in the final analysis tables.

## Where this is used

Applied retroactively to Scenario 1 (see `scenarios/scenario-1-expense-reimbursement.md`, "Ground truth vs. scored claim") and applied from the start in Scenario 2 and all scenarios after it.
