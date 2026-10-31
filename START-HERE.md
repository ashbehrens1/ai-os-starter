> **File type: start-here guide.** Part 1 is for you to read. Part 2 is what Claude follows. Not a skill, so don't install it. In Claude Code you don't need to download anything: paste the prompt in Part 1 and Claude fetches this file itself.

# AI OS Starter: start here

> **If any of this seems confusing, just remember the way to learn AI is to ask it questions.**
> Once Claude has set it up, ask it: "How do I use this? Explain it to me like I'm 12."

> **Read this first:** this kit hasn't been run end to end on your team yet. Screens and menu
> names in the Claude app change, so if a step doesn't match what you see, check the current
> Claude docs or send Claude a screenshot. And check what Claude writes.

---

# Part 1: For you to read

## What this is

Right now each rep starts a new chat, re-explains the company, and pastes in whatever notes they
can find. This is one shared setup instead: Claude reads the same pages about your company,
clients and process every time, for everyone.

It has four layers:
1. **Knowledge base** (`wiki/`): one page per client, prospect and person, plus your company,
   offers and pricing, sales process and voice.
2. **Skills** (`.claude/skills/`): `/call-prep`, `/post-call-debrief`, `/account-brief`, plus
   `/setup-os`, `/tour`, `/ingest` and `/lint` to set it up, learn it and keep it current.
3. **Connectors** (`connectors/crm.md`): the rules for Claude reading and writing your CRM.
   Every write waits for a person to approve it.
4. **Agents** (`agents/`): a Monday pipeline review and a Friday health check, run as
   scheduled tasks.

In my own setup, call prep went from about 45 minutes to about 10. Your mileage depends on how
much you put in the pages.

## Set it up by telling Claude

You don't need to run git or click around GitHub yourself. Claude does that part and asks you
before it installs or creates anything.

1. **Make an empty folder** somewhere that isn't synced by iCloud or OneDrive. A good spot is
   `~/Developer/my-ai-os` (a `Developer` folder in your home folder). On a Mac, Desktop and
   Documents are often synced by iCloud, and git can hang there.
2. **Open Claude Code in that folder** (the VS Code extension or the terminal).
3. **Paste this:**

   > Set up my AI OS from the AI OS Starter template at github.com/ashbehrens1/ai-os-starter. Fetch https://raw.githubusercontent.com/ashbehrens1/ai-os-starter/main/START-HERE.md and follow Part 2. Ask me before you install anything or create anything on my GitHub.

4. **Answer Claude's questions.** First it makes your own private copy on GitHub and on your
   computer. You'll need a free GitHub account; if you don't have one, Claude walks you through
   it. Then it interviews you in seven short batches: company, offers and pricing, sales process,
   voice (with two or three real emails), team, your first few clients and prospects, and your
   CRM. Answer in rough notes. Skip anything. Whatever you skip is marked `NOT GIVEN`, and Claude
   won't make it up.
5. **Take the tour.** When setup is done, Claude shows you around your own AI OS and how to use
   it day to day.

After that, two lines cover most days: "Pull the latest AI OS." when you start, and "Save and
share my changes." when you've changed something.

## If Claude Code isn't an option

- **Cowork:** download the repo (on GitHub: Code > Download ZIP), unzip it, open the
  `ai-os-starter` folder in Cowork and say "Set this up for me."
- **A claude.ai chat or Project:** Claude can't edit files here, so it gives you each page's text
  to save. Download and unzip the repo, start a chat, drag in this file, `CLAUDE.md`, `index.md`,
  the `wiki/` folder and `.claude/skills/setup-os/SKILL.md`, and say "Set this up for me." Save
  each page Claude gives you over the file with the same name.
- Either way, `HOW-TO-LOAD.md` covers getting it to the team in the Claude app.

## After setup

- Try it: "Run /call-prep for [a client you gave it]."
- Learn it: "Give me the tour." Claude explains your AI OS one part at a time.
- Get it to the team: `HOW-TO-LOAD.md` (shared Claude Project, skills, CRM connector, scheduled
  tasks) and `TEAM-WORKFLOW.md` (how teammates get a copy and share changes).
- Keep it current: `OWNER-CHECKLIST.md` for the weekly upkeep.

---

# Part 2: For Claude

You're helping someone set up their AI OS. They may not be technical. Keep every message short,
one step at a time, and explain any jargon in a few plain words. Ask before you install anything,
create anything on their GitHub, or change anything outside the AI OS folder.

**Work out where you're running** and say it in one line:
- **Claude Code** (you can run commands): do Phase 0, then Phase 1, then Phase 2.
- **Cowork with the folder open:** you can edit files but may not have git. Skip Phase 0, run
  Phase 1, and at the end list what changed so they can save it to GitHub later.
- **A claude.ai chat or Project:** you can't edit files. Skip Phase 0. Check you have `CLAUDE.md`,
  `index.md`, the `wiki/` templates and `.claude/skills/setup-os/SKILL.md`; if any are missing,
  tell the person which ones to add. Run Phase 1, outputting each finished page in full, in a
  code block, under its exact path. At the end, list every file to save and point to
  `HOW-TO-LOAD.md`.

If they asked "how do I use this?" or seem lost, explain the four layers in plain words first,
then offer to start.

## Phase 0: get the repo (Claude Code only)

Skip this if you're already inside an AI OS repo (a `CLAUDE.md` whose first heading ends in
"AI OS", plus a `.claude/skills/setup-os/` folder).

1. **Check the folder.** Run `pwd`. If it's under `~/Desktop`, `~/Documents`,
   `~/Library/Mobile Documents` (iCloud Drive) or a OneDrive folder, warn them: those are often
   synced, and git can hang or lose files there. Suggest `~/Developer/` instead and offer to make
   it (ask first). Carry on in their folder only if they say so.
2. **Check git.** Run `git --version`. If it's missing, say so and ask before installing. On a
   Mac, `xcode-select --install` installs it (a system window pops up; they click Install).
3. **Check GitHub CLI.** Run `gh --version`, then `gh auth status`.
   - **No `gh`:** explain it's GitHub's own command-line tool and you'll use it to make their
     copy. Ask before installing. With Homebrew: `brew install gh`. No Homebrew: point them to
     cli.github.com and wait.
   - **Not logged in:** explain they need a GitHub account (free, at github.com/signup) and offer
     to run `gh auth login`. It opens a browser and they log in there; choose GitHub.com, HTTPS,
     and log in with a web browser. Never ask them to paste a password or token into the chat.
   - **Won't use GitHub:** fall back to a local-only copy. Download
     `https://github.com/ashbehrens1/ai-os-starter/archive/refs/heads/main.zip` into the folder,
     unzip it, cd into it, and run `git init`. Tell them sharing with the team needs GitHub later,
     and `TEAM-WORKFLOW.md` covers it. Then go to Phase 1.
4. **Pick a name.** Ask what to call their repo. Suggest `<company>-ai-os`, lowercase with
   hyphens (for example `acme-ai-os`).
5. **Create their private copy.** Say what you're about to do in one line ("I'll make a private
   repo called acme-ai-os on your GitHub, copied from the template, and download it here"), wait
   for a yes, then run:

   ```
   gh repo create <name> --template ashbehrens1/ai-os-starter --private --clone
   ```

   It's private because it will hold client information. If GitHub says the name is taken, ask
   for another. If it fails for any other reason, show them the message and stop.
6. **Move in.** `cd <name>` and check that `CLAUDE.md` and `.claude/skills/` are there. Say one
   line: "Your AI OS is at <full path> and on GitHub at <URL>."

Skills in `.claude/skills/` load when Claude Code starts in a folder, so `/setup-os` may not show
as a command yet. That's fine: read `.claude/skills/setup-os/SKILL.md` and follow it directly.
Tell them that from now on they should open Claude Code in the new folder.

## Phase 1: fill it in

Follow `.claude/skills/setup-os/SKILL.md` exactly. Never invent facts, prices, names or dates;
gaps are `NOT GIVEN`. Don't connect to or change the CRM during setup. Don't send anything.

At the end, setup-os commits to `main` and pushes (first setup only, since it's their private
repo), then hands off to the tour.

## Phase 2: show them around

Follow `.claude/skills/tour/SKILL.md`. It explains their AI OS from what's actually in the
folder, one section at a time, and lets them steer.
