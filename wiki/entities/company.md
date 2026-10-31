---
title: {COMPANY_NAME}
type: entity
status: n/a
tags: [company, team, tools]
sources: [setup-os]
updated: {SETUP_DATE}
---
> **File type: template page.** `/setup-os` fills this in from the owner's answers. Anything not given stays `NOT GIVEN`.

# {COMPANY_NAME}

{ONE_LINE_DESCRIPTION}. Founded {FOUNDED_YEAR}, {TEAM_SIZE} people, based in {LOCATION}.
Website {WEBSITE}. Email pattern {EMAIL_PATTERN}.

## What we sell, to whom
{WHAT_WE_SELL} (details and prices live only in [[services-and-pricing]]).

**Who buys:** {BUYER_ROLES} at {TARGET_CUSTOMER}.

**Why they buy us:** {WHY_THEY_BUY}

## Team
| Name | Role | Owns |
|---|---|---|
| [[person-page-name]] | {ROLE} | {ACCOUNTS_OR_AREA} |

Who signs what: {SIGNING_RULES}

## Tools
- **CRM:** {CRM_NAME}. Rules for the Claude connector are in `connectors/crm.md`. Stages and
  required fields are in [[sales-process]].
- **Other tools the team uses daily:** {OTHER_TOOLS}

## AI setup
Claude {CLAUDE_PLAN} plan. The AI OS lives in a GitHub repo (the master copy) and is mirrored into
a shared Claude Project for the team. {OS_OWNER} owns it. Drafts only: nothing goes to a client or
into the CRM without the account owner's OK.
