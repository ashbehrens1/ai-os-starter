> **File type: guide.** The GitHub landing page. For people. Claude: read `START-HERE.md` and `CLAUDE.md` instead.

# AI OS Starter

A fill-it-in-yourself AI OS for a sales team. It takes your team from every rep starting new
chats and using scattered information to a shared AI OS ecosystem your whole team can use.

It comes empty. You fill it in by answering questions: run `/setup-os` and Claude interviews you
about your company, offers, sales process, voice, team, clients and CRM, then writes the pages.

**New here? Open [START-HERE.md](START-HERE.md).**

## The four layers

| Layer | What it is | Where it lives |
|---|---|---|
| 1. Knowledge base | One page per client, prospect and person, plus your company, offers, sales process and voice. Claude reads the index first and opens only what it needs | `wiki/`, `index.md`, `CLAUDE.md` |
| 2. Skills | The jobs your team repeats, written once: call prep, post-call debrief, account handover, plus setup and upkeep | `.claude/skills/` |
| 3. Connectors | Rules for the live tools Claude can reach, starting with your CRM. Writes need a person's approval | `connectors/` |
| 4. Agents | Scheduled jobs: a Monday pipeline review and a Friday health check on the knowledge base | `agents/` |

Raw files (call transcripts, CRM exports, example emails) go in `raw/` and never get edited.

## Quick start

1. Click **Use this template** at the top of this page. Make the new repo **Private**; it will
   hold your client information.
2. Clone your copy to your computer (VS Code, GitHub Desktop or `git clone`; see
   [TEAM-WORKFLOW.md](TEAM-WORKFLOW.md)).
3. Open the folder in Claude Code and type `/setup-os`. Answer the questions. Skip anything you
   don't know; it gets marked `NOT GIVEN` and nothing gets made up.
4. Read what it wrote, fix anything wrong, then commit and push.
5. Give the rest of the team access: technical folks clone the repo, everyone else uses a shared
   Claude Project. See [HOW-TO-LOAD.md](HOW-TO-LOAD.md).

No Claude Code? You can run setup in Cowork or a claude.ai Project instead.
[START-HERE.md](START-HERE.md) covers all three.

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
