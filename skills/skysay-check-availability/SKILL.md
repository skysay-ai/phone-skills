---
name: skysay-check-availability
description: Call a business through Skysay to check exact product stock, part availability, prices or repair pickup readiness. Use for a factual availability enquiry rather than an order or purchase.
---

# Check availability and prices

Load [the phone skill](../skysay-phone/SKILL.md) and [calling workflow](../skysay-phone/references/phone-tasks.md). Follow authorization and submit-once requirements before dialling. If either shared file is unavailable, repair the installation first.

## Specify what to check

Resolve the business and branch, verified number and exact item or service reference. Product variants can require model, size, color, quantity, part number or condition. A repair enquiry needs only the approved identifying reference and details. Clarify which substitutions, if any, are acceptable.

Resolve the date or pickup window in the branch's timezone. Establish whether the user wants only information or also an explicitly authorized hold. Buying, placing a deposit or authorizing extra repair work is a separate commitment.

## Per-call brief

- Verify the branch and repeat the identifying product or repair details.
- Ask whether the exact item/quantity is physically available now, available at another location, expected later, or merely listed in a system.
- Ask the price and currency, whether tax and mandatory fees are included, and whether the quote has an expiry when relevant.
- Confirm the expected collection time, opening/service cutoff and any conditions the user requested.
- Distinguish exact matches from substitutions and estimates from confirmed readiness.
- Do not reserve, order, approve repairs or share extra contact details unless those actions are in the approved plan.

## Assess the enquiry

A confirmed out-of-stock or not-ready answer can be `succeeded`: the information request was answered. Report the availability as a separate field. Use `unknown` for an ambiguous item, branch, price or missing confirmation. Use `needs_user` for a substitution, charge or new action needing a decision.

Give the exact item/variant, branch, as-of time and timezone, availability, quantity, quoted total or missing price components, pickup conditions, evidence source and call ID. Do not treat today's stock answer as an inventory guarantee for a later visit.

If a separately authorized hold may already have been made, reconcile it before a follow-up requests another. A factual price recheck should not silently place an order.
