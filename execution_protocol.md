# Execution protocol, locked

## The decision: fresh, isolated subagent calls, not an external API

Two options were on the table: Claude via the Anthropic API with a controlled system+user message pair (mirroring Project 1's OpenRouter setup), or fresh, isolated Claude conversations spawned as subagents inside this working environment, with no shared memory of this conversation, the experiment, or any other trial.

**Decision: subagent calls.** My reasoning:

- It satisfies the original constraint I built this project around (no external API key, no billing, no service setup) while still guaranteeing genuine context isolation. Each trial is launched as an independent agent instance with zero access to this conversation, to the research question, to the scoring rubric, or to any other trial's prompt or response. That isolation is enforced by the tool itself, not by convention.
- It's immediately executable, at zero marginal cost, entirely within this environment.

**Disclosed limitation, not concealed:** a subagent launched this way runs inside this environment's general agent harness, which carries its own system-level framing (tool availability, task-completion conventions) rather than being a bare two-message chat completion the way Project 1's API calls were. This is a different instrument than a raw API call, and it's not established that response style (hedging, verbosity, how confidently something is asserted) is unaffected by that framing. I'm naming this here as a scope limitation for the eventual write-up, not something to gloss over: Project 1 and Project 2 are not perfectly comparable instruments even though both ultimately query Claude.

**Mitigation (partial, not a fix):** every trial prompt opens with a one-line instruction to respond directly and conversationally, as if replying to a colleague's message, and not to use any tools. This narrows the harness effect without eliminating it. The rest of the prompt is exactly the scenario content and instruction condition; no mention of an experiment, a study, scoring, or prior trials.

## Trial construction

Each of the 30 trial prompts is built from the same template:

```
Respond directly and conversationally, as if replying to a colleague's message. Do not use any tools, and do not add meta-commentary about this being a task.

{policy or requirements text, if the scenario has one}

{scenario body for this information condition (A/B/C), with its own closing question removed}

{instruction-condition sentence(s): standard, or uncertainty-aware, exactly as locked in the relevant scenario file}
```

Nothing else is added. No condition labels, no scenario numbers, no mention of "Project 2" or ground truth appear in any trial prompt.

## Model and settings

- **Model:** the session default (recorded per trial as `claude-sonnet-5 (agent-tool subagent, default catch-all agent type)`, not a separately configured model or temperature; no override was applied).
- **Runs per cell:** 1 (30 trials total = 5 scenarios x 3 information conditions x 2 instruction conditions). Single-run-per-cell is a disclosed limitation already noted in the README: this supports descriptive comparison, not a within-cell reliability estimate.
- **Randomization:** not applied to execution order for this run. Given the small size (30) and that trials are independently isolated with no shared state or memory across calls, execution order cannot leak into any individual trial's output the way it could in Project 1's single long-running API loop. Order-independence here is a property of the isolation itself, not something that needs a separate shuffle to protect.

## Data capture

Each trial record captures: scenario number and domain, information condition (A/B/C), instruction condition (standard/uncertainty-aware), the exact prompt sent, and the raw response text. I recorded these before applying any scoring, per the locked rule that scoring rules aren't touched after seeing outputs.
