# Information Ambiguity and Epistemic Honesty in AI-Mediated Organisational Decisions

A 30-trial pilot examining whether explicitly instructing a model not to guess actually improves substantive reliability, or mainly changes how cautious its language sounds.

**Start here: [FINDINGS.md](FINDINGS.md)**, the full write-up: research question, design, method, results, conclusion, and limitations.

This is Project 2, a companion to [Project 1](../instruction-strength-study/README.md) (instruction strength and behavioural conflict under competing instructions). I deliberately didn't merge the two: they test different mechanisms. But both take the same approach: turn a messy systems question into something measurable, control the variables, run trials, inspect failures, and revise the methodology before locking it.

## What's in this repository
Information Ambiguity Study
   ├── README
   ├── FINDINGS
   ├── analysis
   ├── Scenario 1
   ├── Scenario 2
   ├── Scenario 3
   ├── Scenario 4
   ├── Scenario 5
   ├── Scoring Rubric
   ├── Scored Trials
   └── ...


## Why there's barely any code

The methodological contribution here is the experimental design: the controlled scenario construction, the isolation protocol, the scoring framework, and the analysis, not software. I ran the 30 trials as fresh, isolated agent calls rather than through an API, so no execution script produced this data. `analysis.py` is the one exception, and it's deliberately narrow: it doesn't call a model, doesn't touch an API, and doesn't re-run anything. It transcribes the already-scored, per-field records from `scoring/scored_trials.md` and recomputes the summary tables from them, with assertions checking the output against what's published in `FINDINGS.md`. Its purpose is to make the arithmetic behind the headline numbers independently checkable, not to make this look like a software project it isn't.

Run it with `python3 analysis.py` (standard library only, no dependencies).
