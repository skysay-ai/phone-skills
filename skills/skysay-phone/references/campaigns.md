# Bounded campaign workflow

Load [workspace operations](workspace-operations.md), [the phone skill](../SKILL.md) and [the calling workflow](phone-tasks.md) before preparing an outbound campaign. If any is unavailable, stop before launch. A specialty supplies its task-specific facts and outcome rules.

## Prepare the list and agent

Resolve the project, compatible published agent, caller numbers, authorized recipients, consent basis, timezone rules, calling windows, finite attempt limits, end time and cost basis. Confirm whether the task is a draft or an approved launch. Check workspace capabilities and number rules. A draft approval does not authorize launch.

Use `list_contact_lists`, `get_contact_list` and `list_contacts` to inspect an existing list, or `create_contact_list` and `add_contacts` for the requested import. Use only source data the user authorized. Preserve external references and task variables, deduplicate the intended recipient/task pairs and report missing or invalid entries. Read the current contact and campaign schemas before choosing field names. A display name alone is not a stable match for a customer or appointment.

Provide each call with its own appointment, survey or other task facts using the agent's supported variables/templates. Verify the actual mapping in the published agent. Do not rely on an ad hoc `runtime_config` field in `create_campaign`, and do not insert every customer's details into one common prompt. Never invent absent dates, consent records, appointment identifiers or callback numbers.

Use a dedicated list or campaign when the requested population differs from an existing one. Record the IDs and reconcile uncertain creates/imports before repeating them. A second campaign is a new calling job, not an idempotent recovery mechanism.

## Save and launch

Use `create_campaign` for a draft with the actual required project, agent, caller numbers, contact list, purpose and consent basis. The live schema also governs schedule, timezone behavior, windows, retries and concurrency. Pick values appropriate to the approved population and workspace limits. Do not copy a sales or collections retry preset into a reminder or feedback task without checking what it does.

Read the saved draft with `get_campaign` and verify the audience, agent, schedule, windows, attempts and stop conditions. Launch only under authorization for that concrete plan, using `launch_campaign` once and saving the returned ID/state. Reconcile an uncertain response with `get_campaign` before another action.

Use `pause_campaign`, `resume_campaign` and `cancel_campaign` only for the selected campaign and requested action. Inspect resulting state: cancellation or pausing may not end an already connected call. Use the shared call workflow's documented live hangup path if stopping an active call is authorized.

## Observe and report

Use campaign and call read tools to report progress, individual outcomes and evidence gaps. Follow pagination and state exactly which population was reviewed. Job completion, answered calls, confirmed appointments and completed surveys are separate counts.

If a recipient opts out, stop further outreach to them in this program. Use the exposed `add_do_not_call` mechanism for a workspace-wide withdrawal and verify the result; do not silently expand a narrower request to every workspace campaign. If the needed scope of opt-out storage or enforcement is unavailable, pause affected future outreach and return the blocker to the owner before it can continue. Do not promise that later campaigns will honor a chat-only note.

Calendar changes, CRM records and exported survey answers require their actual destination integration. Save or send them only as authorized, and verify the external response. Report a follow-up request separately when no write was made.
