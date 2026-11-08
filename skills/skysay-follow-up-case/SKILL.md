---
name: skysay-follow-up-case
description: Call a business through Skysay to follow up an existing order, delivery, repair, refund request or support case and obtain a verified next step. Use for case-status calls, not automatic new purchases or cancellations.
---

# Follow up an existing case

Load [the phone skill](../skysay-phone/SKILL.md), [calling workflow](../skysay-phone/references/phone-tasks.md) and [workspace operations](../skysay-phone/references/workspace-operations.md). If any is unavailable, stop before dialling. Use the shared authorization, navigation eligibility and submit-once rules.

## Resolve the case and permitted action

Verify the business, department and number. Collect the approved order/case reference, relevant dates and minimal identifying facts. Establish what the user wants to learn or request: current status, promised deadline, escalation, an existing refund's progress, or another explicit next step.

Define any permitted remedy and commitments. A status enquiry does not authorize canceling an order, accepting store credit, changing a delivery address or agreeing to a fee. Request missing material decisions together.

If a menu or long hold is likely, check the chosen agent's navigation eligibility and configured budgets. Use existing native navigation where supported. Do not claim a prompt can add keypad, identity-verification or live-transfer capabilities the configured service lacks. Ask the user to complete a secure verification step through the business's proper channel when needed; never invent identity details.

## Per-call brief

- Identify the intended case and department before disclosing approved case details.
- Ask for current status, the last action actually taken and the next responsible party.
- Distinguish a request logged, a remedy approved, a refund initiated and funds received.
- Ask for a concrete date or bounded estimate, a reference and any action required from the user.
- Read back the agreed next step and wait for confirmation. Escalate only within the approved request.
- Leave only the approved voicemail and return unapproved remedies or commitments to the user.

## Report and recover

An enquiry succeeds when the business confirms the requested status and next step, even if the case remains open. Report task success separately from the underlying case outcome. A promised refund is not evidence of money arriving; a delivered-status claim is not proof the user received the item.

Use `needs_user` for verification, an offer needing a decision or a callback that this skill cannot monitor. Use `unknown` for conflicting references, missing confirmation or unclear action state. Report the reference, confirmed status, deadlines/timezone, responsible party, commitments and call ID.

Before an authorized follow-up repeats an escalation, cancellation or refund request, check whether the earlier call already created it. Reconcile uncertain call creation first. Update an external case system or notify another person only through an available authorized integration.
