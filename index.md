> **File type: index.** Claude reads this right after `CLAUDE.md`, then opens only the pages a task needs. Claude keeps it current during setup, ingest and lint.

# {COMPANY_NAME} AI OS: index

Read this first, then open only the page the task needs. Every client and prospect page has the
same sections. `log.md` records every change.

## Start here
- [[overview]]: where things stand this week.
- `CLAUDE.md`: the schema. Layout, page shapes, and how to ingest, query and lint.

## Company
- [[company]]: what we sell, to whom, the team, our tools.

## Offers
- [[services-and-pricing]]: offers, prices, add-ons, contract terms, how to quote.

## Playbooks
- [[sales-process]]: stages, what "qualified" means, the Monday rule, objections, renewals.

## Brand
- [[voice]]: how we write to clients.

## Clients (0)
| Client | Owner | Service | Health |
|---|---|---|---|
| None yet. `/setup-os` or `/ingest` adds them. | | | |

## Prospects (0)
- None yet.

## People (0)
- None yet.

## Sources (0)
- None yet. Raw files live in `raw/transcripts/`, `raw/exports/` and `raw/datasets/`.

## Templates (not real pages)
`wiki/entities/clients/_client-template.md`, `wiki/entities/prospects/_prospect-template.md`,
`wiki/entities/people/_person-template.md`, `wiki/sources/_source-template.md`.

## Skills
In `.claude/skills/`. Setup: `setup-os`. Sales: `call-prep`, `post-call-debrief`,
`account-brief`. Upkeep: `ingest`, `lint`.

## Connectors
- `connectors/crm.md`: what the CRM connector reads and writes, and the Needs Approval rule.

## Agents
- `agents/monday-pipeline-review.md`: Mondays, flags open deals with no next step or no recent
  activity, sent to {SALES_MANAGER}.
- `agents/weekly-lint.md`: Fridays, runs `/lint` and sends the report to {OS_OWNER}.
