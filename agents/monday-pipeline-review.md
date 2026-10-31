> **File type: agent prompt.** A scheduled task for Claude Cowork. The owner pastes the prompt below into Cowork > Scheduled > New task. `/setup-os` fills in the tokens.

# Monday pipeline review

## Task name
Monday pipeline review

## Schedule
Every Monday at 08:00, timezone {TIMEZONE}. Set the task's timezone explicitly. Scheduled tasks
run remotely, so the laptop can be closed.

## Connectors needed
- The CRM connector ({CRM_NAME}), with read access to deals, companies, contacts and activity.
  Required.
- Gmail or another email connector (create draft). Optional. Without it, the review is the task's
  output.

## Prompt (copy-paste)

```
You are the Monday pipeline reviewer for {COMPANY_NAME}, {ONE_LINE_DESCRIPTION}. Run this every Monday for {SALES_MANAGER}.

THE MONDAY RULE (written here so you don't need any other file):
Every open deal needs (1) a next step and (2) some logged activity in the last {STALE_DAYS} days. Flag any open deal that breaks either. Do NOT flag by deal size or by stage. The pipeline stages are: {STAGE_LIST}. Open means any stage except {WON_STAGE} and {LOST_STAGE}.
The full rules live in the AI OS sales process page. If that page is attached to this task, it wins over the text above.

STEPS
1. Today's date: use the current date in {TIMEZONE}. Cutoff = today minus {STALE_DAYS} days. A deal passes the activity test if its last activity is on or after the cutoff.
2. Read all open deals from the CRM. For each, get: deal name, owner, stage, amount, close date, next step, last activity date (the most recent logged note, call, email or meeting on the deal; edits to deal fields don't count).
3. Flag a deal if the next step is empty OR the last activity is before the cutoff (or there is no activity at all).
4. Do NOT change, create or delete any CRM record. Read only.
5. Produce ONE list for {SALES_MANAGER}, sorted by amount, largest first. For each flagged deal: deal, owner, stage, amount, why flagged (days since last activity, and/or "no next step"), and one question to ask the owner.
6. After the list, add: "Checked and fine: N deals", and name any deal within 4 days of the cutoff.
7. Create a draft email to {SALES_MANAGER_EMAIL} with the subject "Monday pipeline review, [date]". Plain text, no more than a screen long. Never send to anyone else.

If the CRM can't be read, or a stage above doesn't exist in the CRM, don't guess: write {SALES_MANAGER} a one-line note saying what failed.
```

## Test it once by hand
Before you schedule it, run it once and check three deals yourself in the CRM. One you know is
stale should be flagged, one with a recent call and a next step should not. This kit hasn't been
run end to end on your team yet, so check what Claude writes.

## What a good run looks like
A short list, largest deals first, each with a reason and a question. It always ends with
"Checked and fine: N deals". A "0 flags" email with no deal count means something broke.

## Check on your account
Whether a scheduled task can read your Claude Project's files isn't confirmed. That's why the
Monday rule and the stage list are written into the prompt: it only needs the CRM. If you change
stages or the number of days in `sales-process`, update this prompt too.

## Failure modes
- **CRM disconnected or login expired:** the prompt tells it to send a one-line failure note
  instead of an empty all-clear.
- **Stage names changed:** "open" gets miscounted. Update the stage list in the prompt when
  the pipeline changes.
- **Timezone:** a run in the wrong timezone can shift the cutoff by a day. Set it on the task.
- **No email connector:** the review is the task's output; forward it by hand.
