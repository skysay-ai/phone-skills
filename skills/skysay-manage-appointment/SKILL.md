---
name: skysay-manage-appointment
description: Book, reschedule or cancel an appointment by calling the business through Skysay, preserving the user's permitted alternatives and existing booking. Use for appointment changes at a named office or service provider.
---

# Manage an appointment by phone

Load [the phone skill](../skysay-phone/SKILL.md) and [calling workflow](../skysay-phone/references/phone-tasks.md). Satisfy their authorization and submit-once steps before dialling; stop if either file is unavailable. For a restaurant table, use [restaurant booking](../skysay-book-restaurant/SKILL.md).

## Resolve the intended change

Identify the business and branch, verified number, requested operation, booking name and service. Resolve dates in the business's timezone. For an existing appointment, establish its date, time and any reference. Share only approved identifying details.

For a new slot, collect preferred times and acceptable alternatives, required duration or provider, essential accommodations and any approved fees. For cancellation, confirm exactly which booking may be canceled and which costs are approved.

A reschedule is not automatically atomic. Establish whether the original must remain until a replacement is confirmed. If the business requires canceling first, obtain authorization for that tradeoff before proceeding. A request to ask about availability alone does not authorize a booking or cancellation.

## Per-call brief

- Verify the branch and identify the existing appointment before changing it.
- Ask about only the approved operation and permitted alternatives.
- For a new booking, obtain confirmation of service, exact date/time, location, name and relevant fees or conditions.
- For rescheduling, ask whether the old slot was replaced or remains active; read back both states. Do not create an additional appointment when the intended action was to replace one.
- For cancellation, obtain an explicit confirmation that the identified booking is canceled and record any reference or fee the business states.
- Return new terms or an unapproved sequence of changes to the user. Use only the approved voicemail instruction.

Use the selected compatible agent and per-call instructions. A native calendar connection is unnecessary for calling a third-party office; writing to the user's own calendar is a separate authorized action.

## Assess and reconcile

Use `succeeded` only when the business confirms the intended operation and all required details. A proposed time is not a booking. A reschedule with an uncertain original-slot state is `unknown`; a required decision or unapproved fee is `needs_user`.

After an uncertain conversation or voicemail requesting a change, an authorized follow-up must first establish the actual state of every affected booking across the approved dates and alternatives. Do not repeat a cancellation or create another appointment from an incomplete transcript. If state cannot be established, stop at `unknown`.

Report the old and new states, exact local time and timezone, service/location, references, terms and call ID. A promised callback leaves the appointment unconfirmed; explain the agreed callback destination or possible return call to the Skysay caller number without promising monitoring.
