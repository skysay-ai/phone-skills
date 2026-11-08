# Phone Skills

Practical phone tasks and voice-agent operations, powered by [Skysay](https://skysay.ai).

This repository contains 13 Agent Skills: instructions that compatible assistants can load when a task needs them. They use Skysay's hosted tools for calls, messages, configuration and results. The shared workflow handles authorization, duplicate prevention and evidence; each specialty adds its own task brief and success checks.

## Skills

### Everyday phone tasks

| Skill | What it does |
| --- | --- |
| [skysay-phone](skills/skysay-phone/SKILL.md) | Shared calling workflow, custom errands, numbers, SMS and results |
| [skysay-book-restaurant](skills/skysay-book-restaurant/SKILL.md) | Reserve a table within approved dates and alternatives |
| [skysay-confirm-business-hours](skills/skysay-confirm-business-hours/SKILL.md) | Check branch hours, holidays and service cutoffs |
| [skysay-manage-appointment](skills/skysay-manage-appointment/SKILL.md) | Book, change or cancel an identified appointment |
| [skysay-check-availability](skills/skysay-check-availability/SKILL.md) | Check stock, product prices, parts or repair readiness |
| [skysay-compare-service-quotes](skills/skysay-compare-service-quotes/SKILL.md) | Collect comparable quotes from approved businesses |
| [skysay-follow-up-case](skills/skysay-follow-up-case/SKILL.md) | Follow up an order, repair, delivery, refund or support case |

### Agent setup, testing and business operations

| Skill | What it does |
| --- | --- |
| [skysay-setup-and-test-agent](skills/skysay-setup-and-test-agent/SKILL.md) | Check readiness, configure an agent and verify an approved test |
| [skysay-test-and-review-agent](skills/skysay-test-and-review-agent/SKILL.md) | Prepare simulation scenarios, preview costs and assess results |
| [skysay-appointment-reminders](skills/skysay-appointment-reminders/SKILL.md) | Prepare and schedule bounded appointment-confirmation campaigns |
| [skysay-call-review](skills/skysay-call-review/SKILL.md) | Review selected calls for outcomes, evidence gaps and next actions |
| [skysay-feedback-survey](skills/skysay-feedback-survey/SKILL.md) | Run an approved questionnaire and report actual responses |
| [skysay-setup-receptionist](skills/skysay-setup-receptionist/SKILL.md) | Configure answering behavior, number routing and handoff rules |

## Install and connect

Use a compatible skills installer:

```sh
npx skills add skysay-ai/phone-skills
```

Select all 13 skills so shared instructions and specialty links are available. Their folders must remain siblings. A specialty stops if a required shared file is missing. For manual installation, copy every directory from `skills/` into your client's skill directory, preserving that layout. Start a new conversation if your client discovers skills only at startup.

Connect Skysay separately in your client's supported integrations settings:

| Setting | Value |
| --- | --- |
| Server | `https://api.skysay.ai/mcp` |
| Transport | Streamable HTTP |
| Authentication | Skysay OAuth; sign in and grant the permissions needed for the task |

The client needs access to the relevant tools. A read-only connection cannot place calls. Outbound calls require an outbound-ready number, a compatible configured agent, purchased funds and permission for the intended task. Transcripts need the corresponding read scope. Skills themselves contain no credentials. See [connection and scope documentation](https://skysay.ai/docs/mcp).

## Examples

- “Use skysay-book-restaurant to prepare a booking for four tomorrow at 19:00. You may accept 18:30–20:00. Show the plan before calling.”
- “Use skysay-manage-appointment to move my garage visit to an approved afternoon. Keep the existing booking until a replacement is confirmed.”
- “Use skysay-check-availability to ask this branch whether it has the exact part I specified and what the total price is.”
- “Use skysay-compare-service-quotes to compare these three cleaners for the same job. Collect quotes without booking.”
- “Use skysay-test-and-review-agent to draft a test suite for this agent and preview its cost before running it.”
- “Use skysay-call-review to review these call IDs and identify confirmed commitments and unresolved questions.”

## Qualification and boundaries

All 13 skill instructions are authored. Package validation and tool-contract checks are separate from model behavior, provider behavior and real phone-call qualification. **Live calls for this package have not been qualified.** A skill cannot add a capability missing from the connected service or client.

Task approval is assistant behavior; OAuth consent and workspace controls do not verify approval of every task. Per-call briefs append to a saved agent prompt, so the selected agent must be compatible. Scheduled campaigns use Skysay's durable scheduling. Calendar/CRM writes and notifications after a chat ends require actual connected integrations or host automation.

The installation command installs instructions. It does not purchase numbers, change number routing, launch campaigns or authorize test calls. Costs and availability come from the connected workspace and [current Skysay pricing](https://skysay.ai/pricing).

## Maintain the package

```sh
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate_skills.py
python3 -m unittest discover -s tests
```

Python and PyYAML are needed only for contributor validation. The skills call the hosted service through their client.

The [research and rationale](docs/research.md) explain the sources and scope of the skills. Original task instructions were inspired by [PhoneZero](https://github.com/function1st/PhoneZero); the workflows here use Skysay. [MIT license](LICENSE) applies to this repository; the hosted service has its own [terms](https://skysay.ai/terms).
