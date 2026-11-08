---
name: skysay-appointment-reminders
description: Prepare and schedule Skysay appointment reminder or confirmation calls using an approved contact list and bounded campaign controls. Use for business outreach about existing appointments, not booking a personal appointment by phone.
---

# Appointment reminders and confirmations

Load [the campaign workflow](../skysay-phone/references/campaigns.md) and its required shared files. If any is unavailable, stop before launch. For a personal call to book or change an appointment, use [appointment management](../skysay-manage-appointment/SKILL.md).

## Build the correct population

Resolve the authoritative appointment source, selected date range, project, caller numbers, compatible agent, intended recipients, consent basis and timezone behavior. Each record needs a stable appointment reference, current status, date/time/location and only the approved contact details and spoken facts.

Identify duplicates, canceled appointments, changes, missing timezones and already completed confirmations. Exclude or resolve them before launch. Map contact variables to the published agent's actual supported fields. Do not put multiple customers' appointment details into one shared prompt.

Establish the reminder timing, calling windows, finite retry limits, voicemail content, program end and cost basis. Distinguish a one-off campaign using an approved data snapshot from a continuing program kept in sync with the calendar. If freshness cannot be guaranteed, disclose the snapshot time and obtain authorization for that bounded snapshot; do not advertise state-aware automatic reminders.

## Define what the call may do

- Confirm the recipient using approved minimal identity checks before disclosing personal appointment details.
- State the appointment in the intended timezone and ask whether the person can attend.
- Record explicit confirmed, cannot-attend, reschedule-requested, wrong-person, callback-requested or opted-out outcomes.
- Change or cancel an appointment only through an actually configured, authorized integration that verifies current state and returns confirmation.
- If that integration is absent, record a reschedule/cancellation request for staff; do not claim the calendar changed.
- Leave only the approved voicemail content and follow the campaign's real stop/retry rules.

## Launch and reconcile

Follow the shared list, draft, inspection, authorization and single-launch sequence. Use native scheduling; the chat does not keep a reminder program alive. If appointments change before launch, refresh the list and reread the draft. For scheduled or active work, use an existing verified synchronization mechanism, or pause/cancel affected outreach until the records are corrected.

Observe actual campaign/call outcomes and honor opt-outs through the shared workflow. Report attempted, answered, confirmed, change-requested, unresolved and pending counts separately with their reviewed population. Preserve call and appointment references for authorized staff follow-up. Send confirmations or write the calendar only through the requested integrations and verify their results.
