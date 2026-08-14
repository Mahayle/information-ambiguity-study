#!/usr/bin/env python3
"""
analysis.py: reproduces the summary tables in FINDINGS.md and data/results_summary.md
from the already-scored trial records in scoring/scored_trials.md.

This script does not call any model or API, and it does not re-run any trial. The 30
trials were executed once, as isolated agent calls (see protocol/execution_protocol.md),
and were scored by hand against the locked rubric (scoring/scoring_rubric.md) and hedge
dictionary (scoring/hedge_word_list.md). The three record lists below are a direct
transcription of that scoring pass, trial by trial, field by field, not a summary
typed in from memory. This script's only job is arithmetic: counting labels and
computing rates, so every number in the write-up is independently checkable rather
than simply asserted in prose.

Run:
    python3 analysis.py

No third-party dependencies; standard library only.
"""

from collections import Counter

# ---------------------------------------------------------------------------
# Part 1 & 2 data: the 20 deliberately manipulated fields (Scenario B/C trials).
# substantive: "supported" | "unsupported_but_flagged"
# hedge: "hedged" | "unhedged", scored on the sentence carrying the field's claim only
# Source: scoring/scored_trials.md, Parts 1-2.
# ---------------------------------------------------------------------------
MANIPULATED_FIELDS = [
    {"trial": "S1-B-STD", "condition": "standard",   "substantive": "supported",              "hedge": "unhedged"},
    {"trial": "S1-B-UNC", "condition": "uncertainty", "substantive": "supported",              "hedge": "unhedged"},
    {"trial": "S1-C-STD", "condition": "standard",   "substantive": "supported",              "hedge": "unhedged"},
    {"trial": "S1-C-UNC", "condition": "uncertainty", "substantive": "supported",              "hedge": "unhedged"},
    {"trial": "S2-B-STD", "condition": "standard",   "substantive": "supported",              "hedge": "unhedged"},
    {"trial": "S2-B-UNC", "condition": "uncertainty", "substantive": "supported",              "hedge": "unhedged"},
    {"trial": "S2-C-STD", "condition": "standard",   "substantive": "supported",              "hedge": "unhedged"},
    {"trial": "S2-C-UNC", "condition": "uncertainty", "substantive": "supported",              "hedge": "unhedged"},
    {"trial": "S3-B-STD", "condition": "standard",   "substantive": "supported",              "hedge": "unhedged"},
    {"trial": "S3-B-UNC", "condition": "uncertainty", "substantive": "supported",              "hedge": "unhedged"},
    {"trial": "S3-C-STD", "condition": "standard",   "substantive": "supported",              "hedge": "unhedged"},  # "might just be a typo": hedge word present nearby, but not on the scored claim
    {"trial": "S3-C-UNC", "condition": "uncertainty", "substantive": "supported",              "hedge": "unhedged"},
    {"trial": "S4-B-STD", "condition": "standard",   "substantive": "supported",              "hedge": "unhedged"},
    {"trial": "S4-B-UNC", "condition": "uncertainty", "substantive": "supported",              "hedge": "unhedged"},
    {"trial": "S4-C-STD", "condition": "standard",   "substantive": "supported",              "hedge": "unhedged"},
    {"trial": "S4-C-UNC", "condition": "uncertainty", "substantive": "supported",              "hedge": "unhedged"},
    {"trial": "S5-B-STD", "condition": "standard",   "substantive": "supported",              "hedge": "unhedged"},
    {"trial": "S5-B-UNC", "condition": "uncertainty", "substantive": "supported",              "hedge": "unhedged"},
    {"trial": "S5-C-STD", "condition": "standard",   "substantive": "unsupported_but_flagged", "hedge": "unhedged"},  # reframed as missing-owner, not the actual status contradiction
    {"trial": "S5-C-UNC", "condition": "uncertainty", "substantive": "supported",              "hedge": "hedged"},    # "status label SEEMS slightly inconsistent": hedge word on the scored claim itself
]

# ---------------------------------------------------------------------------
# Part 3 & 5 data: the 10 fully-specified (Version A) trials, where ground truth
# is "nothing to flag, safe to act" for every field.
# spurious_claims: count of unsupported claims made about fields the ground truth
#                  marks resolved (excludes genuine unanticipated gaps and generic
#                  proactive suggestions; see scoring/scored_trials.md Part 3)
# safe_to_act_correct: did the trial's own bottom-line recommendation match the
#                  ground truth's "yes, proceed"? False means an outright incorrect hold/block
# Source: scoring/scored_trials.md, Parts 3 and 5.
# ---------------------------------------------------------------------------
VERSION_A_TRIALS = [
    {"trial": "S1-A-STD", "condition": "standard",   "spurious_claims": 0, "safe_to_act_correct": True},
    {"trial": "S1-A-UNC", "condition": "uncertainty", "spurious_claims": 0, "safe_to_act_correct": True},
    {"trial": "S2-A-STD", "condition": "standard",   "spurious_claims": 2, "safe_to_act_correct": True},
    {"trial": "S2-A-UNC", "condition": "uncertainty", "spurious_claims": 3, "safe_to_act_correct": True},
    {"trial": "S3-A-STD", "condition": "standard",   "spurious_claims": 0, "safe_to_act_correct": True},
    {"trial": "S3-A-UNC", "condition": "uncertainty", "spurious_claims": 1, "safe_to_act_correct": True},
    {"trial": "S4-A-STD", "condition": "standard",   "spurious_claims": 1, "safe_to_act_correct": True},
    {"trial": "S4-A-UNC", "condition": "uncertainty", "spurious_claims": 1, "safe_to_act_correct": False},  # "I'd hold distribution until someone confirms..."
    {"trial": "S5-A-STD", "condition": "standard",   "spurious_claims": 0, "safe_to_act_correct": True},
    {"trial": "S5-A-UNC", "condition": "uncertainty", "spurious_claims": 4, "safe_to_act_correct": False},  # withholds "closed" status pending invented issues
]

# ---------------------------------------------------------------------------
# Part 4 data: hedge label on each of the 12 Version-A spurious-claim instances
# (the sum of "spurious_claims" above). One instance per row.
# Source: scoring/scored_trials.md, Part 4.
# ---------------------------------------------------------------------------
SPURIOUS_CLAIM_HEDGES = (
    ["unhedged"] * 2   # S2-A-STD: room-booking doubt, AV-reliability doubt
    + ["unhedged"] * 3  # S2-A-UNC: full-agenda doubt, confirmation-method doubt, hybrid-access invention
    + ["unhedged"] * 1  # S3-A-UNC: June 1 notice/start overlap doubt
    + ["unhedged"] * 1  # S4-A-STD: annual-report verifiability doubt
    + ["unhedged"] * 1  # S4-A-UNC: "the only real blocker"
    + ["unhedged", "hedged", "unhedged", "unhedged"]  # S5-A-UNC: contradiction claim, "presumably" (hedged), scope-undefined, ownership-undefined
)


def pct(n, total):
    return f"{n}/{total} ({round(100 * n / total)}%)"


def table_1_detection():
    print("Table 1: Handling of the 20 manipulated fields")
    print("-" * 60)
    n = len(MANIPULATED_FIELDS)
    counts = Counter(f["substantive"] for f in MANIPULATED_FIELDS)
    print(f"  Fields requiring attention, correctly identified as such: {n}/{n} (100%)")
    print(f"  Cleanly supported:            {pct(counts['supported'], n)}")
    print(f"  Unsupported-but-flagged:      {pct(counts['unsupported_but_flagged'], n)}")
    print(f"  Unsupported-and-unflagged:    {pct(counts.get('unsupported_and_unflagged', 0), n)}")
    assert n == 20 and counts["supported"] == 19 and counts["unsupported_but_flagged"] == 1
    print()


def table_2_hedge_on_manipulated():
    print("Table 2: Hedge rate on the 20 manipulated fields")
    print("-" * 60)
    n = len(MANIPULATED_FIELDS)
    counts = Counter(f["hedge"] for f in MANIPULATED_FIELDS)
    print(f"  Unhedged: {pct(counts['unhedged'], n)}")
    print(f"  Hedged:   {pct(counts['hedged'], n)}")
    assert counts["hedged"] == 1 and counts["unhedged"] == 19
    print()


def table_3_calibration():
    print("Table 3: Spurious claims and safe-to-act on fully-specified (Version A) trials")
    print("-" * 60)
    for condition in ("standard", "uncertainty"):
        rows = [t for t in VERSION_A_TRIALS if t["condition"] == condition]
        total_claims = sum(t["spurious_claims"] for t in rows)
        trials_affected = sum(1 for t in rows if t["spurious_claims"] > 0)
        incorrect_holds = sum(1 for t in rows if not t["safe_to_act_correct"])
        label = "Standard  " if condition == "standard" else "Uncertainty-aware"
        print(f"  {label}: {trials_affected}/{len(rows)} trials with >=1 spurious claim, "
              f"{total_claims} instances total, {incorrect_holds}/{len(rows)} incorrect holds")
    std = [t for t in VERSION_A_TRIALS if t["condition"] == "standard"]
    unc = [t for t in VERSION_A_TRIALS if t["condition"] == "uncertainty"]
    assert sum(t["spurious_claims"] for t in std) == 3
    assert sum(t["spurious_claims"] for t in unc) == 9
    assert sum(1 for t in std if not t["safe_to_act_correct"]) == 0
    assert sum(1 for t in unc if not t["safe_to_act_correct"]) == 2
    print()


def table_4_hedge_on_spurious():
    print("Table 4: Hedge rate, correct claims vs. spurious claims")
    print("-" * 60)
    n_correct = len(MANIPULATED_FIELDS)
    hedged_correct = sum(1 for f in MANIPULATED_FIELDS if f["hedge"] == "hedged")
    n_spurious = len(SPURIOUS_CLAIM_HEDGES)
    hedged_spurious = SPURIOUS_CLAIM_HEDGES.count("hedged")
    print(f"  Correct flags (manipulated fields): {pct(hedged_correct, n_correct)} hedged")
    print(f"  Spurious claims (Version A):        {pct(hedged_spurious, n_spurious)} hedged")
    print("  -> Hedge frequency is nearly identical whether the underlying claim is")
    print("     correct or fabricated. No statistical test is claimed here, these are")
    print("     raw counts on 20 and 12 instances, not a confidence-interval estimate.")
    assert n_spurious == 12 and hedged_spurious == 1
    print()


def main():
    table_1_detection()
    table_2_hedge_on_manipulated()
    table_3_calibration()
    table_4_hedge_on_spurious()
    print("All figures reproduced above match FINDINGS.md and data/results_summary.md.")


if __name__ == "__main__":
    main()
