# Information Ambiguity and Epistemic Honesty in AI-Mediated Organisational Decisions

A 30-trial pilot examining whether explicitly instructing a model not to guess actually improves substantive reliability, or mainly changes how cautious its language sounds.

**Start here: [FINDINGS.md](FINDINGS.md)**, the full write-up: research question, design, method, results, conclusion, and limitations.


## What's in this repository

## Repository guide
```text
information-ambiguity-study/
│
├── README.md
├── FINDINGS.md
├── analysis.py
├── execution_protocol.md
│
├── scenario-1-expense-reimbursement.md
├── scenario-2-meeting-coordination.md
├── scenario-3-hiring-recruitment.md
├── scenario-4-communications.md
├── scenario-5-project-handoff.md
│
├── scoring_rubric.md
├── hedge_word_list.md
├── scoring_schema_notes.md
├── scored_trials.md
│
├── raw_trial_outputs.md
└── results_summary.md
```


## Why there's barely any code

The methodological contribution here is the experimental design: the controlled scenario construction, the isolation protocol, the scoring framework, and the analysis, not software. I ran the 30 trials as fresh, isolated agent calls rather than through an API, so no execution script produced this data. `analysis.py` is the one exception, and it's deliberately narrow: it doesn't call a model, doesn't touch an API, and doesn't re-run anything. It transcribes the already-scored, per-field records from `scoring/scored_trials.md` and recomputes the summary tables from them, with assertions checking the output against what's published in `FINDINGS.md`. Its purpose is to make the arithmetic behind the headline numbers independently checkable, not to make this look like a software project it isn't.

Run it with `python3 analysis.py` (standard library only, no dependencies).
