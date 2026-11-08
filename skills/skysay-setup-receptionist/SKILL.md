---
name: skysay-setup-receptionist
description: Configure a Skysay inbound receptionist's answering behavior, business facts, number routing and approved handoff destination, then verify the requested path. Use for setting up a business answering agent rather than an outbound errand.
---

# Set up an inbound receptionist

Load [workspace operations](../skysay-phone/references/workspace-operations.md) and [the phone skill](../skysay-phone/SKILL.md). If unavailable, stop before changing configuration. Read the existing number rules and agent before proposing the route or replacing behavior.

## Resolve the business contract

Identify the project, inbound number, intended agent, verified business facts and their source, hours/timezone, supported languages and caller needs. Establish which questions can be answered, which facts must be collected, when a person should be involved and the fallback when unavailable.

Resolve the approved greeting and disclosures, recording configuration, callback handling and handoff destination. A caller's requested destination does not replace the owner's configured transfer number. Calendar booking, order lookup, ticket creation and live transfers require actual configured tools and access; a prompt alone cannot supply them.

## Configure and preserve routing

Use `get_agent_catalog`, `get_agent` and `get_agent_voice_stack` to select compatible options. Create or update the intended agent through exposed configuration tools. Use authoritative supplied business content. If needed content or an integration is absent, configure an honest collection/handoff path or return the blocker rather than fabricating answers.

Configure tool behavior only through the live schema and validated integration configuration. Verify the approved destination and failure behavior for handoff. Keep credentials in secure service settings. Read back the saved/publication state, languages, tools, ending behavior and any navigation eligibility required for the business flow.

Read `get_number_rules` and record the prior incoming route. Show the intended number and route before an authorized customer-routing change. Use `update_number_rules` with only the intended incoming fields, such as answering with the selected Skysay agent when supported by the live schema. Preserve outgoing caller-ID permissions, recording settings and unrelated number rules. Reread the saved rules and preserve a concrete restoration plan for the original route.

## Verify the inbound path

Arrange an explicitly permitted inbound test using a disposable/test route where available, or the exact business route the owner authorized. Check greeting, two-way audio, a factual enquiry, a missing-information case, the real handoff or callback fallback and clean termination. Verify calendar or ticket writes independently if that capability is part of the setup.

Use the returned call evidence and configured state to identify failures. A published agent does not establish that the carrier routed an incoming call to it; an attempted transfer does not establish that the human answered. Restore a failed route only under the approved rollback scope and verify the restored state.

Report the number/agent IDs, route before/after, publication, tested scenarios and unresolved gaps. Distinguish saved setup, live inbound qualification and readiness for customer traffic.
