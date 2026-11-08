# Workspace operations

Use this reference for agent setup, simulations, campaign configuration and receptionist routing. For making an individual call, also load [the phone skill](../SKILL.md) and [the calling workflow](phone-tasks.md). If a required shared file is missing, repair the installation before acting.

## Context and authorization

Connect through the client's normal Skysay OAuth integration. Check `account_overview`, use the intended workspace and project, and omit `organization_id`. Read current schemas, including any client connection selector, before constructing requests. Respect scope challenges through OAuth; keep credentials and verification codes in the secure connection flow.

Read the existing agent, number rules and related resources before proposing changes. Preserve unrelated configuration and customer routing. Use the user's authorization for the intended configuration work. Before calls, messages, purchased resources, campaign launch or a new business commitment, establish the concrete recipients, terms, task and cost basis; reuse existing approval of that same plan.

Use a dedicated agent or list when isolation is needed. Duplicating an agent does not prove its integrations, credentials or publications are usable. Get valid model, voice and language options from `get_agent_catalog`; inspect saved results after changes. Do not insert placeholder credentials or invent an integration endpoint to get past validation.

## Requests and recovery

Check `isError` as well as returned business state. Keep resource IDs and exact request arguments. For an idempotent operation, persist the supported key and replay exactly that request after uncertainty. Otherwise reconcile with the resource's read tools before another create, publish or launch. An incomplete list or a timeout does not prove that the action failed. Stop when the state remains unknown.

Follow bounded pagination and `omitted` metadata. Read only the selected resources and fields needed for the task. Respect revision fields for configuration writes; if a revision conflict indicates another edit, reread it and rebuild the intended change rather than overwriting it.

## What counts as evidence

Report which stage was reached: prepared, saved, published, launched, simulated, live connected, or business outcome confirmed. A saved configuration is not a successful call. A simulation cannot establish carrier audio, DTMF delivery or real-recipient outcomes. A call result cannot establish that an external calendar or CRM was updated.

Use existing connected calendar, CRM or notification tools only when the requested workflow authorizes them. Verify their target and response. If an integration is unavailable, report that exact gap and preserve the pending work; do not claim a durable write from a table produced in chat.

Background work requires durable execution and an authorized notification channel in the host or service. Returning a resource ID permits resuming observation but does not create a job that survives the conversation. Use native campaign scheduling for scheduled calls.

## Published voice behavior

Use `create_agent`, `get_agent`, `update_agent`, `get_agent_voice_stack` and `set_agent_voice_stack` only as exposed by the current client. Voice-stack saves can create a publication; inspect the resulting revision and publication. Saved instructions, workflows and tool configuration constrain what per-call instructions can do.

Phone-menu navigation is configured through the agent's voice stack. Inspect the returned eligibility, hold/navigation budgets and the line's capabilities. Some engines or trunks cannot support the needed path. Configure an approved agent when requested; an errand does not permit silently changing a shared production agent. Do not invent a live DTMF, takeover or callback-monitoring tool.
