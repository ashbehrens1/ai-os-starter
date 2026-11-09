# AI OS Starter

This is the whole kit in one file: a knowledge base template, three sales skills and a setup
guide. There are no empty pages to fill in. You give this file to Claude, Claude interviews you
about how you actually work, and then it builds your AI OS around your answers.

- **Part 1 and 2** are for you: what an AI OS is and the structure Claude builds.
- **Part 3** is for Claude: how to interview you and build it.
- **Part 4** is for both: using it day to day and sharing it with your team.

**Quick start.** Open Claude Code in an empty folder that isn't synced by iCloud or OneDrive (for
example `~/Developer/my-ai-os`) and paste this:

> Set up my AI OS. Download https://raw.githubusercontent.com/ashbehrens1/ai-os-starter/main/README.md with curl, read all of it, and follow Part 3. Ask me before you install anything or create anything on my GitHub.

No Claude Code? Open this folder in Cowork, or drag this file and the `.claude/skills/` folder into
a Claude chat, and say "Read README.md and set up my AI OS."

If any of this is confusing, ask Claude. "How do I use this? Explain it like I'm 12" works.

---

## Part 1: What an AI OS is

An AI OS is one place your Claude reads from before it does anything: your clients, what you
sell, how you work and how you write. Set it up once and nobody on the team starts from a blank
chat and a pasted spreadsheet again.

It follows the pattern Andrej Karpathy described for an LLM wiki, with three layers:

1. **Raw sources** (`raw/`): call transcripts, exports, emails and docs, saved as they came in.
   Nobody edits them.
2. **The wiki** (`wiki/`): short pages Claude writes from the sources and keeps current. One page
   per client, offer or process.
3. **The schema** (`CLAUDE.md`): the rules. It says what page types exist, where they live, and
   how Claude adds sources, answers questions and checks the pages. Claude reads it first in
   every session.

On top of that sit three more pieces:

- **Skills** (`.claude/skills/`): the jobs you repeat, written once so Claude does them the same
  way every time. This kit ships three: call prep, post-call debrief and account brief.
- **Connectors**: live tools Claude can reach, like your CRM. Writes wait for a person to approve
  them.
- **Scheduled tasks (agents)**: jobs that run without anyone asking, like a weekly pipeline
  review.

## Part 2: The structure Claude builds

This is the knowledge base template. Claude builds it with your names, and only the parts your
work needs.

```
your-ai-os/
  CLAUDE.md          the schema: who you are, the layout, page types, rules
  index.md           one line per page; Claude reads it before opening anything
  log.md             dated list of what changed, newest at the bottom
  raw/               sources as they came in, never edited (transcripts/, exports/, docs/)
  wiki/
    entities/        one page per client, prospect and person
    offers/          what you sell and the prices
    playbooks/       how recurring work gets done, like your sales process
    brand/           how you write
    sources/         one summary page per raw file
  .claude/skills/    call-prep, post-call-debrief, account-brief, plus any built for you
```

The folders under `wiki/` are examples. The interview renames, merges or drops them. A marketing
ops lead might end up with `campaigns/`, `channels/` and `audiences/` and no prospects at all.

### Page types (sales example)

| Type | Folder | What it holds |
|---|---|---|
| Client | `wiki/entities/clients/` | Snapshot (contact, owner, what they bought, fee, renewal, health), open promises, last conversation, next step, risks, history |
| Prospect | `wiki/entities/prospects/` | Snapshot (contacts, owner, stage, deal size, close date), what they need, open promises, last conversation, next step, risks |
| Person | `wiki/entities/people/` | Role, accounts they own, how to work with them |
| Offer | `wiki/offers/` | Each offer, what's included, price, terms. The only place prices live |
| Playbook | `wiki/playbooks/` | Sales process: stages, what "qualified" means, the pipeline rule, objections |
| Brand | `wiki/brand/` | Voice: tone, word limits, sign-off, words you never use, two or three real emails |
| Source | `wiki/sources/` | One raw file summarised: date, who, key points, promises, path to the file |

### Page rules

- Every page starts with frontmatter: `title`, `type`, `status`, `sources`, `updated`.
- File names are lowercase with hyphens: `acme-co.md`. Pages link with `[[page-name]]`.
- One fact lives on one page. Other pages link to it. A price changes in one place.
- The wiki holds what changes slowly. The CRM holds what changes daily (stage, amount, last
  activity). Write down decisions, don't copy CRM fields.
- Anything nobody told Claude is `NOT GIVEN`. Anything a skill looked for and couldn't find is
  `NOT FOUND`. Neither gets guessed.

### Why small pieces

Models get less reliable as you feed them more text. Chroma's 2025 context rot study tested 18
models and every one got worse as the input grew. So the AI OS keeps pages short and specific,
Claude reads `index.md` first and opens only the two or three pages a task needs, and each skill
does one job. Don't upload everything you have. Add a page when a task needs it.

---

## Part 3: For Claude

You're setting up an AI OS for someone who may not be technical. Keep messages short, one step
at a time, and explain jargon in a few plain words. Ask before you install anything, create
anything on their GitHub, or change anything outside the AI OS folder. Never invent facts,
names, prices or dates: write `NOT GIVEN`. Don't connect to or change their CRM during setup,
and don't send anything.

### Step 0: Work out where you are and get the files

Say in one line which of these you're in.

- **Claude Code** (you can run commands):
  1. Run `pwd`. If it's under `~/Desktop`, `~/Documents`, iCloud Drive or OneDrive, warn them that
     git can hang in synced folders and suggest `~/Developer/` (ask before making it).
  2. If this folder already has this README and `.claude/skills/` (for example, unzipped from
     the kit), you have the files. If it isn't a git repo and they want GitHub, offer `git init`
     and, once logged in, `gh repo create <name> --private --source . --push`. Then go to Step 1.
  3. Check `git --version`, `gh --version` and `gh auth status`. If something is missing, say
     what it is and ask before installing (`xcode-select --install` for git on a Mac,
     `brew install gh` for GitHub CLI). For login, offer `gh auth login` (GitHub.com, HTTPS, web
     browser). Never ask for a password or token in the chat.
  4. Ask what to call their AI OS (suggest `<company>-ai-os`). Say what you'll do, wait for yes,
     then run `gh repo create <name> --template ashbehrens1/ai-os-starter --private --clone`
     and `cd` into it. Private, because it will hold client information.
  5. If they won't use GitHub: download
     `https://github.com/ashbehrens1/ai-os-starter/archive/refs/heads/main.zip`, unzip it, `cd` in,
     run `git init`. Sharing with a team needs GitHub later.
  6. Skills load when Claude Code starts, so tell them to open Claude Code in the new folder from
     now on. For this session, read the skill files directly.
- **Cowork with the folder open:** you can write files but may not have git. Skip to Step 1. At
  the end, list what you created.
- **A Claude chat or Project:** you can't write files. Skip to Step 1. Output each finished file
  in full, in a code block under its exact path, and at the end list every file to save.

### Step 1: Interview

Ask in batches of three to five questions. Take rough notes, pasted docs and exports as answers.
"Skip" means `NOT GIVEN`. Follow up on vague answers, and skip batches that don't apply.

1. **You and the team:** their role, the company in one line, team size, timezone, who will use
   the AI OS, and who owns it (keeps it current, approves changes).
2. **What you sell or do:** offers or services, prices, terms, who buys. For a non-sales role:
   what they deliver and to whom.
3. **Recurring jobs:** what they do every day, week and month that Claude could help with. Ask
   them to walk through one in detail: what goes in, what comes out, how long it takes now. This
   decides which skills to keep or build.
4. **Tools and files:** their CRM or main system of record, where their files live (Drive,
   SharePoint, Notion, a local folder), email and calendar. For a pipeline: stage names, and the
   rule for a deal that needs attention (default: no next step, or no activity in 14 days).
5. **How they write:** tone, word limits, sign-off, words they never use, and two or three real
   emails or posts to learn from.
6. **First things to load:** three to five real clients, accounts or projects, or files to drop
   into `raw/`. A CRM export works.
7. **Sharing and policy:** just them, or a team? Does the team use Claude Code or only the
   Claude app? Does their company allow client information in GitHub and Claude? If they're
   unsure, keep it local (no GitHub) until they've checked.

### Step 2: Propose, then wait

Before creating anything, show:

- the tree from Part 2 with their folder names, and anything renamed or dropped
- each page type with its sections
- the pages you'll write now from their answers (only the ones they gave facts for)
- the three skills: keep, adapt (say how) or delete, and at most two new skills for the jobs from
  batch 3. Start small; more can come once these are used.
- whether to set up the weekly pipeline review (Step 5)

Wait for a yes. Change the plan if they ask.

### Step 3: Build the knowledge base

1. Write `CLAUDE.md`, under about 150 lines, with these sections:
   - **Who we are:** two or three lines, the owner, timezone, CRM.
   - **Layout:** a table of every folder and file and what it holds.
   - **Page types:** each type, its folder and its sections in order.
   - **Page rules:** the rules from Part 2.
   - **Adding a source:** save it to `raw/` unchanged, write a source page, update every page it
     touches, update `index.md`, add a line to `log.md`. If it contradicts a page, flag both
     versions for the owner instead of overwriting.
   - **Answering:** read `index.md`, open only the pages needed, use the CRM for live data, show
     both when the wiki and CRM disagree, say `NOT FOUND` for gaps, offer to file anything worth
     keeping.
   - **Weekly check:** when asked, list pages not updated in 60 days, promises past their date,
     broken `[[links]]`, pages missing from `index.md`, contradictions, and open `NOT GIVEN`s.
     Report; the owner fixes.
   - **Rules:** never invent; drafts only, nothing sent; CRM writes only after a person approves
     the old → new values; today's date comes from the chat or task, otherwise ask.
   - **Git** (only if they use GitHub): pull before working; changes go on a branch named for the
     change; short commit message; push and open a pull request; only the owner merges; never
     force-push or delete without being asked; if git asks for a login or fails, stop and say
     what it said.
2. Write the wiki pages from their answers, with frontmatter and `sources: [setup interview]`.
3. Write `index.md` (one line per page: link, type, one-line summary) and start `log.md`.
4. Make the `raw/` folders they'll use.

### Step 4: Adapt the skills

Each skill in `.claude/skills/` has a setup note at the top. For each one:

- **Adapt:** put in their page names, stage names, CRM and voice page, cut sections they don't
  want, then delete the setup note.
- **Repurpose:** if they don't do sales, turn one into their own recurring job (call prep becomes
  meeting prep, account brief becomes a project or campaign brief). Rename the folder and the
  `name:` to match.
- **Delete** any they don't need.

New skills follow the same shape: `name`, a `description` with trigger phrases, then In, Read,
Steps, Out and a "Never invent" line. One job per skill.

### Step 5: Offer the weekly pipeline review

If they have a pipeline in a CRM, offer this as a scheduled task. Fill in the brackets from the
interview (anything they didn't give stays `NOT GIVEN` and you ask for it) and give them the
finished prompt with these steps:

1. Connect the CRM (Part 4, Connect your CRM).
2. In Cowork: **Scheduled** → **New task**. Paste the prompt. Weekly, Monday 08:00, with their
   timezone set on the task. Turn on the CRM connector for it.
3. Run it once by hand and check three deals against the CRM before trusting the schedule.

```
You are the weekly pipeline reviewer for [company], [one-line description]. Run this every Monday for [who gets it]. Review [all open deals / deals owned by name].

THE RULE: every open deal needs (1) a next step and (2) logged activity in the last [N] days. Flag any open deal that breaks either. Don't flag by size or stage. Stages: [stage list]. Open means any stage except [won stage] and [lost stage].

1. Today's date is the current date in [timezone]. Cutoff = today minus [N] days.
2. Read all open deals from the CRM: name, owner, stage, amount, close date, next step, last activity date (the latest note, call, email or meeting; field edits don't count).
3. Flag a deal if the next step is empty, or the last activity is before the cutoff or missing.
4. Read only. Don't change, create or delete any CRM record.
5. Write one list for [who gets it], largest amount first: deal, owner, stage, amount, why flagged, and one question to ask the owner.
6. End with "Checked and fine: N deals" and name any deal within 4 days of the cutoff.
7. If an email connector is on, save it as a draft to [their email], subject "Pipeline review, [date]". Never send.

If the CRM can't be read or a stage doesn't exist, don't guess. Write one line saying what failed.
```

Not in sales? Offer the same shape for their own weekly review (open campaigns, overdue
projects) only if they want it.

### Step 6: Finish

1. In Claude Code with GitHub: show what you'll commit, then commit to `main` and push (first
   setup only, since it's their private repo).
2. Offer to replace this README with a short one for their team: what's in the AI OS, who owns it,
   the everyday prompts from Part 4. This full guide stays at github.com/ashbehrens1/ai-os-starter.
3. Tell them in five lines or fewer how to use it, and suggest a first try with one of their
   skills on something real, like "/call-prep [a client they gave you]".

---

## Part 4: Using it and sharing it

### Every day

- **Claude Code:** open the folder. The skills show up as `/call-prep`, `/post-call-debrief` and
  `/account-brief`. Ask questions in plain words; Claude reads the index and the pages it needs.
- **New information:** drop the file in `raw/` (or paste it) and say "File this in the AI OS."
- **With a team on GitHub:** say "Pull the latest AI OS." when you start, and "Save and share my
  changes." when you're done. Claude makes a branch and a pull request, and the owner merges it.

### Connect your CRM (HubSpot example)

1. Add HubSpot from the connector directory in Claude. A HubSpot Super Admin approves it and
   picks which data it can reach.
2. In Claude's connector settings, set HubSpot's **Write tools** to **Needs Approval**. The
   connector can view, create and update records but not delete, and it has no read-only mode,
   so this setting is the safety.
3. Each person connects with their own login, and Claude sees only what they can see in HubSpot.
4. Test it read-only: "List my open deals with no next step," and check the answer in HubSpot.

Another CRM: check the same three things before turning it on (who approves it, whether it
respects each user's permissions, whether writes can be gated). If writes can't be gated, keep
the skills read-only. No connector yet: drop a CRM export in `raw/exports/` each week and file it.

### Share it with the team

- **Teammates who use Claude Code:** the owner says "Invite [email] to my AI OS repo" (or on
  GitHub: Settings → Collaborators → Add people). The teammate opens Claude Code in an empty
  folder and says: "Join my team's AI OS at [repo URL]. Clone it into a folder that isn't synced
  by iCloud, open it, and show me how to use it."
- **Everyone else, in a shared Claude Project (Team plan):**
  1. In Claude Code, say "Prepare the Project upload." Claude combines the wiki into a few files
     by page type in `dist/project-files/` and zips each skill into `dist/skills/`.
  2. Create a Project named after your company, share it with the team, upload the files, and
     paste `CLAUDE.md` into the Project's instructions.
  3. An Owner uploads the skill zips under **Organization settings → Library**, then under
     **Library → Policy** turns on **Cloud code execution and file creation**, then **Skills**.
     Skills becomes Plugins on 2026-11-30; leave it off and plugins stop working in Claude
     Desktop, Cowork and the Code tab from that date.
  4. Project files are a snapshot that Claude can't edit. When the owner merges changes, rebuild
     and replace them. In the Project, Claude writes updated page text for the owner to save.
- **Cowork:** open the folder in Cowork to work on the files. Scheduled tasks live here.

### The owner's week

- **Monday:** merge pull requests, refresh the shared Project, read the pipeline review.
- **During the week:** new transcripts and exports go into `raw/` and get filed. If it's true
  about a client, it goes on the client page, not into somebody's chat.
- **Friday:** say "Run the weekly check" and fix what it finds.
- **Monthly:** archive dead clients and prospects, update people pages, clear old `NOT GIVEN`s.

This kit hasn't been run end to end on your team. Check what Claude writes before you rely on it.
