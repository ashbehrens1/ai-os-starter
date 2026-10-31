---
title: Sales process
type: playbook
status: n/a
tags: [sales, pipeline, monday-rule, discovery, renewals]
sources: [setup-os]
updated: {SETUP_DATE}
---
> **File type: template page.** `/setup-os` fills this in. Skills read it for stages, what "qualified" means, the Monday rule and how to handle objections.

# Sales process

Our CRM is {CRM_NAME}. {PIPELINE_SETUP}, e.g. "One pipeline for new business and renewals".

## Stages
Use the stage names exactly as they appear in the CRM.

| Stage | Means |
|---|---|
| {STAGE_NAME} | {WHAT_IT_MEANS} |
| {WON_STAGE} / {LOST_STAGE} | Done |

## Qualified means
{QUALIFIED_DEFINITION}. Write it as a short checklist, e.g. a problem we solve, a named
decision-maker, a start date, a budget at or above list.

## Deal amount
{DEAL_AMOUNT_RULE}

## Required CRM fields
| By stage | Required |
|---|---|
| Any open deal | {REQUIRED_FIELDS} |

## The Monday rule
Every open deal needs (1) a next step and (2) some logged activity in the last {STALE_DAYS} days.
The Monday pipeline review flags any open deal that breaks either and sends the list to
{SALES_MANAGER}. Open means any stage except {WON_STAGE} and {LOST_STAGE}.

- If a deal is flagged, the owner adds the real next step or logs the touch the same day, or
  closes the deal if it's dead. Don't make up a next step to clear the flag.
- The rule is a hygiene check. It doesn't look at deal size or stage.

## Discovery questions we always ask
- {QUESTION}
- Agree the next step with a date before hanging up. Log it in the CRM the same day.

## Objections and answers
| They say | We say |
|---|---|
| {OBJECTION} | {ANSWER} |

## Renewals
{RENEWAL_MOTION}, e.g. when the renewal call gets booked and when terms go out.
