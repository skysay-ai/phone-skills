---
name: skysay-setup-and-test-agent
description: Check Skysay calling readiness, configure a compatible voice agent and verify an approved test call. Use for first-time setup or diagnosing why an existing agent or number cannot make the intended call.
---

# Set up and verify an agent

Load [workspace operations](../skysay-phone/references/workspace-operations.md), [the phone skill](../skysay-phone/SKILL.md) and [calling workflow](../skysay-phone/references/phone-tasks.md). If a shared file is unavailable, stop before changes or dialling. A readiness inspection is read-only; configuration work and a paid test are distinct stages.

## Inspect before configuring

Resolve the intended workspace, project, inbound/outbound use, task, supported languages and expected integrations. Inspect `account_overview`, `get_capabilities`, the selected number's rules, `get_agent` and `get_agent_voice_stack`. Find a compatible existing resource before creating another.

Produce a readiness result with separate states for authentication/scopes, funds, number activation/channels, caller-ID permission, agent configuration/publication and required integrations. Name the actual blocker and the smallest next action. A readiness request does not authorize a top-up, number purchase or change to customer routing.

## Configure the intended agent

Use options from `get_agent_catalog`. Resolve the agent's name, task boundaries, truthful opening, language policy, relevant integrations and ending behavior. Use a dedicated agent when task-specific behavior would conflict with a shared production role.

Use `create_agent` for an authorized new agent or the exposed update/voice-stack tools for the intended changes. Read their current required fields and revisions. `set_agent_voice_stack` can publish a voice configuration; inspect its resulting publication, validation and eligibility instead of assuming a draft is active. Verify credential bindings through their secure configuration path, not placeholders in chat.

Read back the saved agent and number rules. Apply a caller-ID allowlist or inbound route only when that change is part of the approved setup. Preserve unrelated permissions and routing. If a save is refused, do not switch models or relax controls silently to make it pass.

## Qualify the requested path

Use [agent testing](../skysay-test-and-review-agent/SKILL.md) for simulations if installed. Obtain authorization for a browser/trial test and its cost basis before starting it. Follow the actual client-supported flow and returned state; when using `create_trial_call`, respect its current `synthetic_only` requirement. Creating a trial record does not prove browser audio connected, and a browser/trial test is not PSTN evidence.

For an approved outbound phone test, establish the exact recipient, brief and cost basis, then use the shared calling workflow once. Verify the received conversation or recording as permitted, the actual task response and clean termination. Number readiness alone cannot establish audible two-way speech.

For inbound qualification, use an approved test number or the explicitly authorized business route and arrange a permitted incoming call. Do not change another number merely to obtain a passing test. Return a partial result if the necessary caller, browser audio or evidence is unavailable.

Report resource IDs, saved/publication state, checks passed, exact evidence and remaining gaps. Mark live calling verified only for the direction and path actually tested. Do not promise background monitoring or every provider/language combination from one call.
