---
name: post-call-debrief
description: Turns a pasted call transcript into a CRM note, promises, one dated next step, proposed CRM updates with old and new values, a follow-up email draft and conflict flags. Trigger on "/post-call-debrief", "debrief this call", "process this transcript".
---
> **File type: skill.** Claude follows this after a call. It drafts everything and changes nothing in the CRM until the rep says yes.

# Post-call debrief

**In:** the call transcript (pasted or attached). If it isn't clear which client or prospect it
was, ask.

**Read:** `index.md` first, then only: the client or prospect page (to catch conflicts);
`sales-process` (stages, the Monday rule); `voice` (email rules and word limit);
`services-and-pricing` if prices come up. If the CRM connector is on, read the company's open
deal to get current field values.

**Out, in this order:**
1. **CRM note:** paste-ready, 4 to 6 lines. Who was on, what was decided, what's next.
2. **What was promised:** ours (owner, date) and theirs (owner, date). Missing date =
   `NO DATE GIVEN`.
3. **Next step:** one single step with a date. If the call doesn't support one, say so and
   propose one for the rep to confirm.
4. **CRM updates proposed:** `field: old value → new value` for stage, amount, close date, next
   step. Old value reads `NOT CHECKED` if the connector is off. Stage names must match the
   `sales-process` page exactly.
5. **Follow-up email draft:** follows the `voice` page (tone, word limit, sign-off, never-say
   list). Draft only, written for the account owner to send.
6. **Flags:** anything in the transcript that conflicts with the client or prospect page (price,
   dates, contacts, scope, health), with both versions.

**Old transcripts:** if the CRM already shows the call's outcome, write "no change" for those
fields instead of proposing them again, and keep the rest of the output.

**CRM writes:** only after the rep says yes to the proposed list. Write tools are on Needs
Approval; the rep approves each one. Never write on your own, never delete, and never create a
record the rep hasn't confirmed. If the connector is off, stop at the proposal.

**Filing it:** offer to run `/ingest` on the transcript so the client page and a source page get
updated too.

**Never invent** facts, numbers, dates or promises that aren't in the transcript or pages.
Nothing is sent.
