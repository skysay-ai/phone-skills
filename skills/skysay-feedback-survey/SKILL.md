---
name: skysay-feedback-survey
description: Conduct an approved short feedback questionnaire by Skysay phone call or campaign and report actual answers, missing responses and opt-outs. Use for customer feedback after a service or completed case.
---

# Collect feedback by phone

For one call, load [the phone skill](../skysay-phone/SKILL.md) and [calling workflow](../skysay-phone/references/phone-tasks.md). For scheduled or multiple recipients, also load [the campaign workflow](../skysay-phone/references/campaigns.md). Stop before dialling or launch if a required shared file is unavailable.

## Define the questionnaire

Resolve the service or event being reviewed, approved recipients, caller identity, permitted spoken context, questionnaire, response scale and follow-up rules. Use exact questions and an unambiguous scale, including its endpoints. Ask about only the information the program needs.

Establish timing/timezones, call-cost basis, finite attempt limits, voicemail policy and whether participation is optional. Verify the event/contact match before mentioning personal details. For a group, use the campaign workflow's consent, list mapping and durable scheduling.

Decide where answers must be saved. Verify that integration and its fields before promising persistence. A report-only survey can return results in chat; a program requiring CRM/database records is incomplete without a verified write destination.

## Per-call behavior

- Explain the approved purpose and ask whether the recipient is willing to answer.
- Ask the questionnaire without steering toward a positive score.
- Clarify an ambiguous score rather than guessing it. Preserve a refusal or skipped question as missing, never as zero.
- Capture an explanation in the recipient's own meaning; do not convert a complaint into a positive response.
- End when the recipient declines or opts out. Follow the shared opt-out handling before future outreach.
- Escalate a complaint or arrange a callback only within the approved program and real handoff capabilities.

## Assess and store

Use conversation evidence to distinguish completed, partial, declined, no-answer and unknown surveys. A completed call is not a completed questionnaire. Do not count an AI-generated answer as a customer response.

Return response counts with denominators for attempted, reached, agreed and answered questions. Calculate a score only from actual responses using the defined scale. Do not generalize a small responding group to the entire customer base.

For authorized persistence, write through the configured destination using stable survey/contact/call references and its supported duplicate-prevention method; verify the response. Reconcile an uncertain write before repeating it. Report saved records separately from responses that remain only in call evidence or the chat report.
