# Research behind Phone Skills

Research date: 8 November 2026. This research informed the 13 skills now authored in this repository. The priorities below describe the original selection rationale. See the [skill catalog](../README.md) for the current package.

The best next additions are appointment management, product/service enquiries and quote comparison. A setup-and-test skill would remove a practical adoption obstacle: the task skills currently depend on an outbound-ready number and a compatible configured voice agent.

## What others actually publish

| Source | Observed offering | Useful lesson for Skysay |
| --- | --- | --- |
| [PhoneZero](https://github.com/function1st/PhoneZero) | A shared calling runtime, a restaurant task and custom task briefs. Its setup combines Telnyx with xAI. | Keep a common execution workflow and add task-specific facts and outcome requirements. |
| [Nous Research Hermes telephony skill](https://github.com/NousResearch/hermes-agent/blob/main/optional-skills/productivity/telephony/SKILL.md) | Number setup, messaging and inbox polling, outbound AI calls, recorded messages and keypad menu entry. | Readiness diagnostics and returning to an existing number are useful. Skysay can use its hosted service instead of copying the provider credential scripts. Its claims about comparative voice quality were not independently verified. |
| [Vapi agent skills](https://docs.vapi.ai/agent-skills) and [source repository](https://github.com/VapiAI/skills) | Saved-agent setup, prompting, tool configuration, calls, campaigns, post-call extraction, handoffs and simulations. | Offer business task skills and developer setup/testing skills. These developer instructions are different from an agent that completes a consumer errand. |
| [OpenClaw voice-call plugin](https://docs.openclaw.ai/plugins/voice-call) | Notifications, conversations and inbound calls, with setup diagnostics and dry-run smoke checks. | A readiness check should work before a paid test. Its local gateway is an architectural alternative, not something Skysay needs to recreate. |
| [Google AI Mode availability and pricing](https://support.google.com/websearch/answer/17104441?hl=en) | Business enquiries covering service prices, available appointments and stock; it can call when online information is insufficient. | Product availability and service quote comparison have a clear consumer-facing precedent. This is a product feature, not an installable SKILL.md. |
| [Bland appointment scheduling](https://www.bland.ai/solutions/appointments) | Booking changes, confirmations, reminders and waitlist outreach. | One appointment lifecycle skill is more reusable than separate skills for each trade. Published customer metrics are vendor claims and are not used as Skysay forecasts. |
| [Retell proactive customer service](https://www.retellai.com/learn/proactive-customer-service) | Appointment, delivery, renewal and payment follow-ups, plus customer surveys, with explicit recorded outcomes. | Business skills should start with an actual trigger and end with a recorded result. Repeated outreach needs a durable scheduler and stop rules. |

## Recommended consumer task skills

All rows reuse the shared Skysay call workflow. “Existing tools” means the necessary primitives exist in the inspected application source.

| Priority | Proposed skill | Example | Existing support and work still needed |
| --- | --- | --- | --- |
| 1 | `skysay-manage-appointment` | Book a haircut, move a garage visit, or cancel an appointment the user identifies. | Existing outbound call instructions and transcripts. Define allowed dates, confirmation details, fees and cancellation ordering. Replacing an appointment is not an atomic operation; preserve the original unless the user authorized the tradeoff. No new scheduling backend is needed to phone a third-party office. |
| 2 | `skysay-check-availability` | Ask whether a particular product, part or repair is available, its price, and pickup timing. | Existing call tools. Capture exact product/model/size, branch, tax/currency and whether availability is confirmed or merely estimated. A hold or purchase is a separate commitment requiring authorization. |
| 3 | `skysay-compare-service-quotes` | Ask several approved businesses for the price and earliest date for the same repair or cleaning job. | Existing single-call tools can run bounded, sequential attempts. Agree the business list, attempt count and spend basis. Return comparable inclusions, exclusions and evidence for each call; do not book the cheapest option automatically. |
| 4 | `skysay-follow-up-case` | Check a delivery, repair, existing refund request or support ticket. | Existing call tools; some destinations require menu navigation. Use approved case references and identity details. Distinguish “request received”, “refund approved” and “money received”. |

Keep restaurant booking as a specialization because its confirmation fields are useful. Avoid a new skill for every restaurant, salon or country. A new skill earns its place when its collection, commitment or evidence rules differ from the shared workflow.

## Recommended setup and business skills

| Priority | Proposed skill | What it would do | Qualification boundary |
| --- | --- | --- | --- |
| 1 | `skysay-setup-and-test-agent` | Check OAuth scopes, number readiness, funds and agent compatibility; help configure a dedicated agent, then run an explicitly approved test. | MCP has agent creation, catalog, voice-stack publication, trial calls and call-result tools. A readiness report must not silently purchase a number or dial. Validate publication and real outbound audio before calling setup complete. |
| 2 | `skysay-test-and-review-agent` | Build conversation scenarios, preview costs, run approved simulations and review call evidence. | MCP has simulation suites, preview/start/results/cancel. Tests must pin the intended agent snapshot; a base-agent simulation alone does not prove per-call task overlays work. Separate simulated behavior, latency observations and real PSTN proof. |
| 3 | `skysay-appointment-reminders` | Prepare an approved contact list, schedule confirmations and record confirmed/reschedule/callback outcomes. | Contact-list and campaign tools exist. Use their durable scheduling, calling windows, retries and pause/cancel controls. A changed customer calendar requires a verified integration; a phone transcript alone does not update it. |
| 4 | `skysay-call-review` | Review a bounded set of calls for unanswered questions, commitments, outcomes and follow-up actions. | Call, transcript, summary and translation tools exist. Preserve evidence gaps and provenance. Writing to a CRM or sending follow-ups needs the corresponding authorized integration; report-only review can stand alone. |
| 5 | `skysay-feedback-survey` | Ask an approved short questionnaire after a service and return answers and scores. | Existing outbound/campaign and transcript primitives. Add durable contact/opt-out handling and verify the destination for storing structured responses. A skill must not pretend that a table in chat is a persisted customer record. |
| 6 | `skysay-setup-receptionist` | Configure a business's answering agent, number routing, FAQs and approved handoff destination. | Agent configuration and number-rule tools exist. Confirm actual knowledge, calendar and handoff integration access; verify an inbound call before calling the receptionist ready. This changes business routing and needs a concrete approved configuration. |

## Phone menus and hold: use the implementation already present

[Vapi's IVR guide](https://docs.vapi.ai/ivr-navigation) confirms that keypad menus require actual DTMF capability and timing, not merely an instruction to say a digit. Skysay already contains native menu-navigation and hold-control code, including trunk capability checks, duplicate-action prevention and transfer safety. MCP exposes `navigation` through voice-stack configuration and reports eligibility. In the inspected schema, GPT-Live is explicitly described as ineligible for this navigation path.

Therefore an IVR/support skill is an opportunity to configure and qualify existing behavior. Do not claim universal menus, unlimited hold, arbitrary callback acceptance or live human takeover based on a prompt alone. Check the selected engine and line, the hold/navigation time budget and the actual target menu. There is no exposed general-purpose live DTMF or take-over tool in the inspected MCP catalog. A chat assistant should not invent one.

## Small implementation shape

Use one shared call workflow for workspace selection, readiness, per-call briefs, idempotency, observation and evidence. Add compact task-specific briefs and success requirements. Use the agent's supported languages as configuration shared across the tasks. Use existing campaigns for persistent schedules and existing simulations for agent tests. Keep the task wrappers small and use the existing hosted calling service.

Background custom errands need a separate qualification: a skill cannot promise to keep working or notify the user after its conversation ends unless the host provides durable execution and a permitted notification channel. Saving a call ID supports resuming observation; it does not by itself create an unattended multi-business research job. Similarly, connecting a calendar or CRM is separate from making an appointment-related call. These are integration requirements to verify before advertising those promises.

Suggested qualification sequence: first the shared workflow, restaurant booking and hours enquiries on approved test destinations; then setup/testing, appointment management and availability enquiries; then quote comparison and business campaigns. Each new skill needs happy-path and refusal/uncertainty examples plus at least one controlled end-to-end qualification relevant to its promises. No demand, conversion or reliability improvement has been measured in this research.

## Evidence scope

Research used first-party repositories and product documentation above. Advertised behavior was not exercised on competitors. Skysay capability mapping used the service's tool contracts and inspected implementation. Actual deployed availability and each client's OAuth scopes require live discovery. No calls, purchases or production changes were made for this research.
