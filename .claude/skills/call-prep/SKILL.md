---
name: call-prep
description: One-page brief before a sales, renewal or client call, built from the account's page in the AI OS, the last call notes, the open deal in the CRM and the sales process and pricing pages. Trigger on "/call-prep", "prep me for my call with [name]", "call prep for [name]".
---

> **Setup note (Claude: adapt this skill during setup, then delete this note).** Put in this AI OS's
> real page names, stage names, pipeline rule and CRM, and cut any section the person doesn't
> want. If they don't run sales calls, turn it into prep for the meetings they do run, or delete
> the skill.

# Call prep

**In:** a client or prospect name. Optional: the call topic or time ("pricing call with their CFO").

**Read:** `CLAUDE.md` and `index.md` first, to find the pages below. Then open only:
- the page for this client or prospect
- the newest source page or transcript for them
- the page with the sales stages, pipeline rule and objections
- the pricing page

If the AI OS has no page for one of these, write `NOT FOUND` for what it would have given you.
If a CRM connector is on, read the company's open deal (stage, amount, close date, next step,
last activity, owner). If it's off or the deal isn't there, say what you couldn't check.

**Steps**
1. Match the name to a page. If it's ambiguous or missing, ask. Don't guess.
2. Pull the call date, attendees and goal from the page or the topic given. If the goal isn't
   written down, infer it from the last call and say "goal inferred from the last call".
3. Check the deal against the pipeline rule. Say plainly if it would be flagged.
4. Write the brief.

**Out:** one page, under about 350 words, in this order:
1. **Call at a glance:** who, when, goal
2. **Where we left off:** last call or email, in two or three lines
3. **Open promises:** ours (owner, date) and theirs
4. **Deal status:** stage, amount, close date, next step, last activity, and "Flagged by the
   pipeline rule: yes/no, why"
5. **Likely questions and answers:** two or three, from the page and the objections. Quote prices
   only from the pricing page.
6. **Suggested agenda:** three to five items with rough minutes
7. **Watch-outs:** risks, people not on the call, stalled items

**Never invent** facts, prices, dates or names. Anything not in the pages or the CRM is `NOT FOUND`.
If a page says `NOT GIVEN` for something the brief needs, say so and suggest the owner fills it
in. Read-only: never change the CRM.
