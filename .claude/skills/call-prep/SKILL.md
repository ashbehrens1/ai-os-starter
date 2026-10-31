---
name: call-prep
description: One-page brief before any sales, renewal or client call, built from the client or prospect page, the last call notes, the open deal in the CRM and the sales process and pricing pages. Trigger on "/call-prep", "prep me for my call with [name]", "call prep for [name]".
---
> **File type: skill.** Claude follows this to prep a rep for a call. Read-only: it never changes the CRM.

# Call prep

**In:** a client or prospect name. Optional: the call topic or time ("pricing call with their CFO").

**Read:** `index.md` first, then only: the client or prospect page for that name; the latest
source page or transcript for them; `sales-process` (stages, the Monday rule, objections);
`services-and-pricing`. If the CRM connector is on, read that company's open deal (stage, amount,
close date, next step, last activity, owner). If it's off or the deal isn't found, say what you
couldn't check.

**Steps**
1. Match the name to a page. If it's ambiguous or missing, ask. Don't guess.
2. Pull the call date, attendees and goal from the page or the topic the rep gave. If the goal
   isn't written down, infer it from the last call and say "goal inferred from the last call".
   Other missing items are NOT FOUND.
3. Check the deal against the Monday rule on the sales process page. Say plainly if it would trip.
4. Write the brief.

**Out:** one page, under about 350 words, these sections in this order:
1. **Call at a glance:** who, when, goal
2. **Where we left off:** last call or email, in two or three lines
3. **Open promises:** ours (owner, date) and theirs
4. **Deal status:** stage, amount, close date, next step, last activity, and "Would trip the
   Monday rule: yes/no, why"
5. **Likely questions and answers:** two or three, drawn from the page and the objections table.
   Quote prices only from `services-and-pricing`.
6. **Suggested agenda:** three to five items with rough minutes
7. **Watch-outs:** risks, people not on the call, stalled items

**Never invent** facts, prices, dates or names. Anything not in the pages or the CRM is written
`NOT FOUND`. If a page still shows `NOT GIVEN` for something the brief needs, say so and suggest
the owner fills it in. Read-only: don't change the CRM.
