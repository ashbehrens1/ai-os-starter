---
name: account-brief
description: One-page handover brief for a rep taking over a client account, built from everything the AI OS holds on that client. Trigger on "/account-brief", "I'm taking over [client]", "brief me on the [client] account".
---
> **File type: skill.** Claude follows this when an account changes hands. Read-only.

# Account brief

**In:** a client name. Optional: who is taking over and from whom.

**Read:** `index.md` first, then only: the client page; the people pages for anyone named on it;
source pages or transcripts for that client; `services-and-pricing`; `sales-process` (Renewals).
If the CRM connector is on, read their open deals. If not, say that deals weren't checked.

**Out:** one page, in this order:
1. **Who they are:** industry, city, size, what they do
2. **What they bought and pay:** service, fee, start date, and how the fee compares to list
   (list prices from `services-and-pricing` only)
3. **Health and history:** current health, then a short dated timeline of what happened
4. **People:** their side (name, role, what they care about) and ours
5. **Open promises:** ours and theirs, with owners and dates
6. **Risks:** health, silence, late deliveries, anything pending
7. **Renewal:** date, and the plan from the Renewals section of `sales-process`
8. **First three things to do this week:** concrete, dated where the pages allow

**Prospects:** if the name is a prospect, say so in one line, use the prospect page, and replace
sections 2, 3 and 7 with: Deal (stage, amount, close date), Timeline of conversations, and
Decision process. Don't make up a health rating, start date or renewal date.

**Never invent** history, contacts, prices or dates. Use `NOT FOUND` for gaps. Read-only.
