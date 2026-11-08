---
name: skysay-test-and-review-agent
description: Build and review Skysay conversation simulation suites, preview their costs and run approved tests against a chosen agent snapshot. Use for voice-agent regression testing and evaluating failure handling before live qualification.
---

# Test and review an agent

Load [workspace operations](../skysay-phone/references/workspace-operations.md). If unavailable, stop before saving a suite or starting a run. For real phone tests, also load [the phone skill](../skysay-phone/SKILL.md) and [calling workflow](../skysay-phone/references/phone-tasks.md).

## Define the evaluation

Resolve the agent/project, draft or published snapshot, intended use cases and concrete acceptance criteria. Inspect the agent and existing suites with `get_agent`, `get_agent_voice_stack`, `list_simulation_suites` and `get_simulation_suite`. Preserve an existing suite unless its modification is requested and supported by an actual exposed tool.

Choose realistic scenarios for normal completion, refusal or unsupported requests, interruption, silence, missing information, unapproved commitments and relevant tool failures. Add language or handoff cases only for the behavior the agent is configured to support. Use synthetic identifying details and test destinations, not copied customer transcripts.

Specify observable success criteria: required facts obtained, a permitted action confirmed, an unapproved action declined or a call ended appropriately. A simulation completing or an evaluator giving a high score is insufficient when the underlying turns contradict it.

## Save, preview and run

Use `create_simulation_suite` with the live schema's scenario and policy format. Inspect the saved suite. Do not assume an unsupported update method exists; if a replacement is necessary, make the replacement explicit and preserve prior evidence.

Use `preview_simulation_run` to inspect the cost/plan before an approved run. Simulations can consume funds even without PSTN. If no usable estimate is returned, disclose that gap before obtaining approval for the run. Use `start_simulation_run` with a stable idempotency key and the intended snapshot source. Save the suite/run IDs and inspect which snapshot was actually pinned.

Recover an uncertain start with the same exact supported request/key or the run's read tools. Do not generate another key to obtain a result. Poll `get_simulation_run` within a bounded wait, and page `get_simulation_run_results`. Use `cancel_simulation_run` only for the selected run when requested; confirm its state rather than claiming immediate termination.

## Assess and report

Inspect scenario outcomes and available conversation/action evidence. Distinguish product behavior from fixture, evaluator or provider failures. Report passed/failed/unknown scenarios, observed behavior, unresolved evidence and the smallest supported correction.

Report latency only from actual timestamps or telemetry, naming the measured interval and sample size. Do not infer end-to-end response time from a single provider estimate. A base-agent simulation does not prove per-call `runtime_config` briefs, carrier audio, menu tones or live transfers work; qualify those paths separately.

Give the agent snapshot, suite/run IDs, covered cases, cost evidence and limits. A proposed prompt fix is a proposal until saved and retested through the intended path.
