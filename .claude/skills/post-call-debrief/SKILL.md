---
name: post-call-debrief
description: Turns a call transcript or notes into a CRM note, promises, one dated next step, proposed CRM updates with old and new values, a follow-up email draft and conflict flags. Trigger on "/post-call-debrief", "debrief this call", "process this transcript".
---

> **Setup note (Claude: adapt this skill during setup, then delete this note).** Put in this AI OS's
> real page names, stage names and CRM, and cut any output the person doesn't want. No CRM? Drop
> section 4. If they don't do sales calls, turn it into a debrief for the meetings they do run,
> or delete the skill.

# Post-call debrief

**In:** the call transcript or notes (pasted or attached). If it isn't clear which client or
prospect it was, ask.

**Read:** `CLAUDE.md` and `index.md` first, to find the pages below. Then open only:
- the page for this client or prospect (to catch conflicts)
- the page with the sales stages and pipeline rule
- the voice page (email rules and word limit)
- the pricing page, if prices come up

If the AI OS has no page for one of these, say which and carry on. If a CRM connector is on,
read the company's open deal to get current field values.

**Out, in this order:**
1. **CRM note:** paste-ready, 4 to 6 lines. Who was on, what was decided, what's next.
2. **What was promised:** ours (owner, date) and theirs (owner, date). Missing date =
   `NO DATE GIVEN`.
3. **Next step:** one step with a date. If the call doesn't support one, say so and propose one
   for the rep to confirm.
4. **CRM updates proposed:** `field: old value → new value` for stage, amount, close date, next
   step. Old value is `NOT CHECKED` if the connector is off. Stage names must match the stages
   page exactly.
5. **Follow-up email draft:** follows the voice page (tone, word limit, sign-off, words to
   avoid). A draft for the account owner to send.
6. **Flags:** anything in the call that conflicts with the client or prospect page (price, dates,
   contacts, scope, health), with both versions.

**Old calls:** if the CRM already shows the call's outcome, write "no change" for those fields.

**CRM writes:** only after the rep says yes to the proposed list, one approval per write. Never
write on your own, never delete, and never create a record the rep hasn't confirmed. If the
connector is off, stop at the proposal.

**Filing it:** offer to file the transcript in the AI OS the way `CLAUDE.md` says (save it to
`raw/`, write a source page, update the client or prospect page).

**Never invent** facts, numbers, dates or promises that aren't in the call or the pages. Nothing
is sent.
