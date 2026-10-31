> **File type: guide.** The GitHub landing page. For people. Claude: read `START-HERE.md` and `CLAUDE.md` instead.

# AI OS Starter

A fill-it-in-yourself AI OS for a sales team. It takes your team from every rep starting new
chats and using scattered information to a shared AI OS ecosystem your whole team can use.

It comes empty. You set it up by telling Claude: it makes your private copy on GitHub, interviews
you about your company, offers, sales process, voice, team, clients and CRM, writes the pages,
then gives you a tour of how to use it.

**New here? Open [START-HERE.md](START-HERE.md).**

## The four layers

| Layer | What it is | Where it lives |
|---|---|---|
| 1. Knowledge base | One page per client, prospect and person, plus your company, offers, sales process and voice. Claude reads the index first and opens only what it needs | `wiki/`, `index.md`, `CLAUDE.md` |
| 2. Skills | The jobs your team repeats, written once: call prep, post-call debrief, account handover, plus setup, a guided tour and upkeep | `.claude/skills/` |
| 3. Connectors | Rules for the live tools Claude can reach, starting with your CRM. Writes need a person's approval | `connectors/` |
| 4. Agents | Scheduled jobs: a Monday pipeline review and a Friday health check on the knowledge base | `agents/` |

Raw files (call transcripts, CRM exports, example emails) go in `raw/` and never get edited.

## Quick start

Open Claude Code in an empty folder that isn't synced by iCloud or OneDrive (for example
`~/Developer/my-ai-os`) and paste this:

> Set up my AI OS from the AI OS Starter template at github.com/ashbehrens1/ai-os-starter. Fetch https://raw.githubusercontent.com/ashbehrens1/ai-os-starter/main/START-HERE.md and follow Part 2. Ask me before you install anything or create anything on my GitHub.

That's it. Claude checks you have git and a GitHub account, asks before it installs anything,
makes your private copy, runs `/setup-os` with you, then runs `/tour`. Skip any question you
can't answer; it gets marked `NOT GIVEN` and nothing gets made up.

The skills: `setup-os`, `tour`, `call-prep`, `post-call-debrief`, `account-brief`, `ingest` and
`lint` (seven in `.claude/skills/`).

**Doing it by hand instead:** click **Use this template** at the top of this page, make the new
repo **Private** (it will hold client information), clone it to a folder that isn't synced by
iCloud ([TEAM-WORKFLOW.md](TEAM-WORKFLOW.md) shows how), open it in Claude Code and type
`/setup-os`. No Claude Code? You can run setup in Cowork or a claude.ai Project;
[START-HERE.md](START-HERE.md) covers both, and [HOW-TO-LOAD.md](HOW-TO-LOAD.md) covers getting
it to the team in the Claude app.

## What's in here

| File | For |
|---|---|
| `START-HERE.md` | First read. How to set it up, whichever Claude app you use |
| `CLAUDE.md` | The schema Claude reads first: layout, page shapes, rules |
| `TEAM-WORKFLOW.md` | How the team shares changes with git, in plain English |
| `OWNER-CHECKLIST.md` | The owner's weekly and monthly upkeep |
| `HOW-TO-LOAD.md` | Getting it into a shared Claude Project, plus skills, connector and scheduled tasks |
| `tools/build_project_bundle.py` | Turns the wiki into a handful of Project upload files and zips the skills |

This kit hasn't been run end to end on your team yet. Check what Claude writes before you rely
on it.
