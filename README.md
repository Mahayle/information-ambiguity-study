# Information Ambiguity and Epistemic Honesty in AI-Mediated Organizational Decisions

A 30-trial pilot examining whether explicitly instructing a model not to guess actually improves substantive reliability, or mainly changes how cautious its language sounds.

**Start here: [FINDINGS.md](FINDINGS.md)**, the full write-up: research question, design, method, results, conclusion, and limitations.

This is Project 2, a companion to [Project 1](../instruction-strength-study/README.md) (instruction strength and behavioural conflict under competing instructions). I deliberately didn't merge the two: they test different mechanisms. But both take the same approach: turn a messy systems question into something measurable, control the variables, run trials, inspect failures, and revise the methodology before locking it.

## What's in this repository

```text
information-ambiguity-study/
│
├── README.md                          this file, start with FINDINGS.md instead
├── FINDINGS.md                        the write-up: question, design, results, conclusion, limitations
├── analysis.py                        reproduces the summary tables from the already-scored data
│
├── protocol/
│   └── execution_protocol.md          how the 30 trials were actually run, and why
│
├── scenarios/                         5 organizational domains, each a matched fully-specified /
│   ├── scenario-1-expense-reimbursement.md      missing-information / contradictory-information
│   ├── scenario-2-meeting-coordination.md       triplet, with a ground-truth key and a construction-
│   ├── scenario-3-hiring-recruitment.md         time stress-test log recording what was checked and
│   ├── scenario-4-communications.md             revised before the pilot ran
│   └── scenario-5-project-handoff.md
│
├── scoring/
│   ├── scoring_rubric.md              the locked substantive + hedging labels, safe-to-act checklist
│   ├── hedge_word_list.md             the locked, mechanical hedge-word dictionary
│   ├── scoring_schema_notes.md        why ground truth and scored claims are kept separate
│   └── scored_trials.md               the full per-field, per-trial scoring pass
│
└── data/
    ├── raw_trial_outputs.md           all 30 raw responses, verbatim, before any scoring
    └── results_summary.md             the detailed tables behind FINDINGS.md
```

## Why there's barely any code

The methodological contribution here is the experimental design: the controlled scenario construction, the isolation protocol, the scoring framework, and the analysis, not software. I ran the 30 trials as fresh, isolated agent calls rather than through an API, so there's no execution script that produced this data. `analysis.py` is the one exception, and it's deliberately narrow: it doesn't call a model, doesn't touch an API, and doesn't re-run anything. It transcribes the already-scored, per-field records from `scoring/scored_trials.md` and recomputes the summary tables from them, with assertions checking the output against what's published in `FINDINGS.md`. Its purpose is to make the arithmetic behind the headline numbers independently checkable, not to make this look like a software project it isn't.

Run it with `python3 analysis.py` (standard library only, no dependencies).
