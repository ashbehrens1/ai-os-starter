---
name: account-brief
description: One-page handover brief for someone taking over a client account, built from everything the AI OS holds on that client. Trigger on "/account-brief", "I'm taking over [client]", "brief me on the [client] account".
---

> **Setup note (Claude: adapt this skill during setup, then delete this note).** Put in this AI OS's
> real page names and CRM, and cut any section the person doesn't want. Outside sales it works
> as a project or campaign brief: rename it and swap the sections, or delete the skill.

# Account brief

**In:** a client name. Optional: who is taking over and from whom.

**Read:** `CLAUDE.md` and `index.md` first, to find the pages below. Then open only:
- the client page
- the people pages for anyone named on it
- source pages or transcripts for that client
- the pricing page
- the sales process page, for how renewals are handled

If the AI OS has no page for one of these, write `NOT FOUND` for what it would have given you.
If a CRM connector is on, read their open deals. If not, say deals weren't checked.

**Out:** one page, in this order:
1. **Who they are:** industry, city, size, what they do
2. **What they bought and pay:** service, fee, start date, and how the fee compares to list
   (list prices from the pricing page only)
3. **Health and history:** current health, then a short dated timeline
4. **People:** their side (name, role, what they care about) and ours
5. **Open promises:** ours and theirs, with owners and dates
6. **Risks:** health, silence, late deliveries, anything pending
7. **Renewal:** date, and the plan from the sales process page
8. **First three things to do this week:** concrete, dated where the pages allow

**Prospects:** if the name is a prospect, say so in one line and replace sections 2, 3 and 7
with: Deal (stage, amount, close date), Timeline of conversations, and Decision process. Don't
make up a health rating, start date or renewal date.

**Never invent** history, contacts, prices or dates. Use `NOT FOUND` for gaps. Read-only.
