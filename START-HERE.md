> **File type: start-here guide.** Part 1 is for you to read. Part 2 is what Claude follows. Not a skill, so don't install it. Drop it into Claude with the rest of this folder and say **"Set this up for me."**

# AI OS Starter: start here

> **If any of this seems confusing, just remember the way to learn AI is to ask it questions.**
> Once you've dragged the files in, ask Claude: "How do I use this? Explain it to me like I'm 12."

> **Read this first:** this kit hasn't been run end to end on your team yet. Screens and menu
> names in the Claude app change, so if a step doesn't match what you see, check the current
> Claude docs or send Claude a screenshot. And check what Claude writes.

---

# Part 1: For you to read

## What this is

Right now each rep starts a new chat, re-explains the company, and pastes in whatever notes they
can find. This folder is one shared setup instead: Claude reads the same pages about your
company, clients and process every time, for everyone.

It has four layers:
1. **Knowledge base** (`wiki/`): one page per client, prospect and person, plus your company,
   offers and pricing, sales process and voice.
2. **Skills** (`.claude/skills/`): `/call-prep`, `/post-call-debrief`, `/account-brief`, plus
   `/setup-os`, `/ingest` and `/lint` to set it up and keep it current.
3. **Connectors** (`connectors/crm.md`): the rules for Claude reading and writing your CRM.
   Every write waits for a person to approve it.
4. **Agents** (`agents/`): a Monday pipeline review and a Friday health check, run as
   scheduled tasks.

In my own setup, call prep went from about 45 minutes to about 10. Your mileage depends on how
much you put in the pages.

## How you fill it in

Run `/setup-os` and Claude asks you seven short batches of
questions: company, offers and pricing, sales process, voice (with two or three real emails),
team, your first few clients and prospects, and your CRM. Answer in rough notes. Skip anything.
Whatever you skip is marked `NOT GIVEN`, and Claude won't make it up.

## Pick your path

**A. Claude Code (best for whoever owns the AI OS).** Claude edits the files directly and you
save them to GitHub.
1. Make your own private copy on GitHub (Use this template), then clone it. `TEAM-WORKFLOW.md`
   walks through it.
2. Open the folder in Claude Code (the VS Code extension or the terminal).
3. Type `/setup-os`.

**B. Cowork.** Open the `ai-os-starter` folder in Cowork, drag in this file and say "Set this up
for me."

**C. A claude.ai chat or Project.** Claude can't edit files here, so it gives you each page's text
to save.
1. Download the folder (on GitHub: Code > Download ZIP) and unzip it.
2. Start a chat, drag in this file, `CLAUDE.md`, `index.md`, the `wiki/` folder and
   `.claude/skills/setup-os/SKILL.md`, and say "Set this up for me."
3. Save each page Claude gives you over the file with the same name.

## After setup

- Try it: "Run /call-prep for [a client you gave it]."
- Get it to the team: `HOW-TO-LOAD.md` (shared Claude Project, skills, CRM connector, scheduled
  tasks).
- Keep it current: `TEAM-WORKFLOW.md` for how changes flow, `OWNER-CHECKLIST.md` for the weekly
  upkeep.

---

# Part 2: For Claude

You're helping someone set up their AI OS. They may not be technical. Keep every message short,
one step at a time, and explain any jargon in a few plain words.

1. **Work out where you're running** and say it in one line:
   - Claude Code, or Cowork with the folder open: you can edit files. Make the changes directly.
   - A claude.ai chat or Project: you can't edit files. Output each finished page in full, in a
     code block, under its exact path, so the person can save it.
2. **Check the files are here.** You need `CLAUDE.md`, `index.md`, the `wiki/` templates and
   `.claude/skills/setup-os/SKILL.md`. If any are missing, tell the person which ones to add.
   Don't start without `CLAUDE.md`.
3. **If they asked "how do I use this?"** or seem lost, explain the four layers in plain words
   first, then offer to start setup.
4. **Run setup** by following `.claude/skills/setup-os/SKILL.md` exactly. In Claude Code the
   person can also type `/setup-os`.
5. **Rules:** never invent facts, prices, names or dates; gaps are `NOT GIVEN`. Don't connect to
   or change the CRM during setup. Don't send anything.
6. **When setup is done:**
   - Claude Code: offer to commit and push ("Set up the AI OS"), then point to
     `TEAM-WORKFLOW.md`.
   - Cowork or claude.ai: list every file they need to save, then point to `HOW-TO-LOAD.md`.
