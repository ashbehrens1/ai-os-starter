---
name: lint
description: Health check on the AI OS knowledge base. Finds contradictions between pages, stale pages, overdue promises, missing index entries, broken links, leftover placeholders and wiki facts that disagree with the CRM. Trigger on "/lint", "check the knowledge base", "what's stale", "wiki health check".
---
> **File type: skill.** Claude follows this for the weekly health check. It reports problems and fixes nothing.

# Lint

**In:** nothing. Optional: a date to treat as today (otherwise ask) or one area to check
("just the clients").

**Read:** `index.md`, every client and prospect page, the people pages, `services-and-pricing`,
`sales-process`. Skip files whose names start with `_` (they're templates). If the CRM connector
is on, read open deals and companies.

**Checks**
1. **Contradictions:** the same fact with two values on two pages (a fee, a renewal date, an
   owner, a contact's role). Prices: any fee that isn't explained against `services-and-pricing`.
2. **Stale pages:** `updated` more than 60 days before today.
3. **Overdue promises:** an Open promises line with a date before today.
4. **Index:** a page missing from `index.md`, or an index entry with no page.
5. **Links:** `[[links]]` that point at no page.
6. **Gaps:** leftover placeholder tokens (capital words in curly braces) and `NOT GIVEN` on
   pages the skills depend on: prices, stages, the "qualified" test, the voice rules.
7. **CRM drift** (if connected): owner, stage or next step on a page that disagrees with the
   deal. The CRM is right about live data; flag the page.

**Out:** one list, most serious first, grouped by check. Each line: the page, what's wrong, both
values where there are two, and the fix. End with "Clean: N pages". Then one `log.md` line:
`## [YYYY-MM-DD] lint | N issues`.

Don't fix anything. Report it; the owner decides. Never write to the CRM.
