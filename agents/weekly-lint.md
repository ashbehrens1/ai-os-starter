> **File type: agent prompt.** A scheduled task for Claude Cowork. The owner pastes the prompt below into Cowork > Scheduled > New task. `/setup-os` fills in the tokens.

# Weekly lint

## Task name
Weekly AI OS lint

## Schedule
Every Friday at 15:00, timezone {TIMEZONE}. Friday afternoon gives {OS_OWNER} time to fix pages
before Monday's pipeline review.

## Needs
- The `lint` skill (uploaded under Organization settings > Library).
- The AI OS pages. Scheduled tasks run remotely; a task that needs local files has to run on your
  computer instead. Two options:
  - Run it locally, pointed at your copy of the AI OS folder (pull first so it's current).
  - Or attach the bundle files from `dist/project-files/` to the task. Check on your account
    whether a scheduled task can read your Project's files.
  If the task can't read the pages, it says so and stops; lint has nothing to check without them.
- CRM connector, read only. Optional; without it the CRM drift check is skipped.
- Gmail or another email connector (create draft). Optional; without it the report is the task's
  output.

## Prompt (copy-paste)

```
Run /lint on the {COMPANY_NAME} AI OS. Today is the current date in {TIMEZONE}.
Create a draft email to {OS_OWNER} ({OS_OWNER_EMAIL}) with the subject "Weekly lint, [date]".
Plain text, most serious issues first, no more than a screen long.
Don't change any page or CRM record. If you can't read the AI OS pages or the CRM, write
{OS_OWNER} one line saying what failed instead of a clean report.
```

## What a good run looks like
A short list the owner can work through in under an hour: a few overdue promises, any page older
than 60 days, any page whose owner or stage disagrees with the CRM, and any `NOT GIVEN` gaps on
pages the skills need. "Clean: N pages" at the end. A report with no page count means the task
couldn't read the files.
