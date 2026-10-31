---
title: CRM connector
type: connector
status: active
tags: [connector, crm]
sources: [setup-os]
updated: {SETUP_DATE}
---
> **File type: connector rules.** Every skill and agent that touches the CRM follows this page. `/setup-os` fills in the CRM name and admin. HubSpot is the worked example; other CRMs are at the bottom.

# CRM connector

{CRM_NAME} is our CRM and the source of truth for anything that changes daily: deal stage, amount,
close date, next step, last activity, owner. The wiki holds the relationship; the CRM holds the
pipeline. Stages and required fields are on [[sales-process]].

CRM admin: {CRM_ADMIN}.

## Who uses it

| Used by | Reads | Writes |
|---|---|---|
| `/call-prep` | The company's open deal | None |
| `/post-call-debrief` | The deal's current values | Note, next step, stage, close date, after the rep says yes |
| `/account-brief` | Open deals for the client | None |
| `/lint` | Open deals and companies, to compare with the wiki | None |
| `monday-pipeline-review` agent | All open deals and their activity | None |

## Rules
- Propose every write as `field: old value → new value`. The rep approves it in the Needs
  Approval prompt. Nothing writes silently.
- Never delete or merge records.
- Never change a deal owner, or touch a closed deal, without {SALES_MANAGER}'s OK.
- {EXTRA_CRM_RULES}
- If the CRM and a wiki page disagree, show both and flag it for {OS_OWNER}. Don't pick one
  silently.

## Worked example: HubSpot

- Add HubSpot from the connector directory in the Claude app. A HubSpot Super Admin approves it
  and picks the data permissions.
- Each person connects with their own HubSpot login. Claude sees only what that person can see in
  HubSpot.
- The connector can view, create and update records. It can't delete, and it has no read-only
  mode.
- So in Claude's connector settings, set HubSpot's **Write tools** to **Needs Approval**. That
  setting is the safety: every write shows up for the person to approve first.

## Other CRMs

Check the Claude app's connector directory for your CRM. If it's there, look for the same three
things before you turn it on: who has to approve it, whether it respects each user's own
permissions, and whether write tools can be set to Needs Approval. If write tools can't be
gated, keep the skills read-only: delete the "after the rep says yes" write from
`/post-call-debrief` and have reps paste the proposed changes in by hand.

No connector yet? Everything still works. The skills mark CRM fields `NOT CHECKED`, and you can
drop a weekly CRM export into `raw/exports/` and run `/ingest` on it.

## Adding another connector
Add a page here in the same shape (setup, who uses it, rules) before turning it on. Start with
the tool the team opens most; add the next once that one is used every day.
