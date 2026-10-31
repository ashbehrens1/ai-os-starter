> **File type: guide.** For the AI OS owner. How to get the AI OS into the Claude app for the whole team: a shared Project, org skills, the CRM connector and two scheduled tasks.

# How to load this into the Claude app

For a Claude Team plan, using a shared Project. Do `/setup-os` first, so there's something to
load.

## 0. Build the upload files

From the `ai-os-starter` folder:

```
python3 tools/build_project_bundle.py
```

That writes `dist/project-files/` (6 files) and `dist/skills/` (one zip per skill). The wiki is
bundled so the Project holds 6 files instead of dozens. Re-run it after every merge that changes
a page. If it lists pages that still have placeholders, finish setup first.

Can't run Python? Ask Claude Code to run it for you, or skip the bundle and upload the filled-in
wiki pages, `CLAUDE.md` and `index.md` to the Project directly.

## 1. The shared Project (the knowledge base)

Create a Project, name it after your company (e.g. "Acme AI OS"), share it with the team, and upload the six files
in `dist/project-files/`:

| File | What's in it |
|---|---|
| 01-instructions.md | `CLAUDE.md`, the index, this week's overview |
| 02-company-offers-process-voice.md | Company, CRM rules, pricing, sales process, voice, any other playbooks |
| 03-clients.md | Every client page |
| 04-prospects.md | Every prospect page |
| 05-team.md | Every person page |
| 06-call-notes-and-sources.md | Source pages, transcripts, example emails |

Paste the contents of `CLAUDE.md` into the Project's custom instructions too, so the rules apply
even if the file isn't pulled in.

**Keeping it current.** Project files are a snapshot and read-only to Claude. When pages change,
re-run the script and replace the files (see `OWNER-CHECKLIST.md`). Live deal data comes from the
CRM connector, not from these files.

Not uploaded: `log.md`, `agents/`, `tools/`, the git guides, and the templates.

## 2. Skills (organization-wide)

An Owner uploads skills under **Organization settings > Library**. Upload each zip in
`dist/skills/`: setup-os, tour, call-prep, post-call-debrief, account-brief, ingest and lint.

- On Team, owner-uploaded skills are available to everyone and on by default. People can switch
  individual ones off. Targeting a skill at one group is Enterprise only.
- Under **Organization settings > Library > Policy**, turn on "Cloud code execution and file
  creation", then "Skills". Skills is being renamed Plugins on 2026-11-30; if it's left off,
  plugins stop working in Claude Desktop, Cowork and the Code tab from that date.
- A Plugins page is rolling out, with general availability for Team expected 2026-11-09, so
  the screen may look different from these steps.
- Run skills from inside the Project so they can read its files.

## 3. CRM connector

The rules are in `connectors/crm.md`. For HubSpot:

1. Add HubSpot from the connector directory. A HubSpot Super Admin approves it and picks the data
   permissions.
2. In Claude's connector settings, set HubSpot's **Write tools** to **Needs Approval**. The
   connector can view, create and update records but not delete, and has no read-only mode, so
   Needs Approval is the safety.
3. Each person connects with their own login, and Claude respects their HubSpot permissions.

Other CRMs: see the bottom of `connectors/crm.md`.

## 4. Monday pipeline review (scheduled task)

Scheduled tasks work on all paid plans. In Cowork: **Scheduled > New task**. Paste the prompt
from `agents/monday-pipeline-review.md`.

- Needs the CRM connector. An email connector is optional, for delivery as a draft.
- Mondays 08:00, with the task's timezone set. Scheduled tasks run remotely, so the laptop can be
  closed. They can use connectors and skills.
- Run it once by hand first and spot-check a few deals.
- Check on your account whether a scheduled task can read your Project's files. The prompt
  doesn't depend on it: the Monday rule is written into the prompt and the deal data comes from
  the CRM.

## 5. Weekly lint (scheduled task)

Same place. Paste the prompt from `agents/weekly-lint.md`. Fridays 15:00. It needs the `lint`
skill and the AI OS pages; that file explains the two ways to give it the pages.

## In Claude Code

None of the bundling is needed. Open the folder, and the skills in `.claude/skills/` show up as
`/call-prep`, `/ingest` and so on. `[[links]]` resolve as file names there.
