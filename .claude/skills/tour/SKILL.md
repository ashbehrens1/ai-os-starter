---
name: tour
description: Shows someone around their own AI OS in plain English, one section at a time, using only what's in their repo - what pages and skills they have, how to ask for things, how to save and share, the owner's weekly jobs, bringing teammates in, and the shared Claude Project. Trigger on "/tour", "give me the tour", "how do I use this", "explain this to me", "explain it like I'm 12", "what can this do", and after /setup-os finishes.
---
> **File type: skill.** Claude follows this to explain a person's own AI OS to them. It reads the repo and explains; it changes nothing unless the person asks.

# Tour of your AI OS

**In:** nothing. Works for the owner right after setup, or a teammate who just joined.

**Read first:** `CLAUDE.md`, `index.md`, and `wiki/entities/company.md`. List the folders in
`.claude/skills/` (the skill names), `wiki/entities/clients/`, `wiki/entities/prospects/` and
`wiki/entities/people/` (skip files starting with `_`; those are templates). In Claude Code, run
`git remote -v` to get the repo's GitHub address.

In a claude.ai chat or Project you can't list folders, so work from `index.md` and whatever files
are in the Project, and say once that you're going from those.

## How to run it

- **One section at a time.** Each section is a few short lines, then ask "Want more on this, or
  next?" The person steers. If they ask about something out of order, go there.
- **Use their real stuff.** Name their actual pages, skills, clients and prospects. Never invent
  a page, a client or a fact. If there are no client or prospect pages yet, say so and use
  `[client name]` as a placeholder in the examples.
- **Plain words.** Explain any jargon in a few words the first time (repo, commit, pull request).
  If they said "explain it like I'm 12", keep it that simple the whole way through.
- **Don't do things during the tour** without asking. Offering is fine.
- Start with one line: "Here's a quick tour of your AI OS. Stop me any time or ask to skip
  ahead."

## The sections

**1. What you have.** The four layers, with their real contents:
- **Knowledge base:** name the pages that exist: the company, offers and pricing, sales process
  and voice pages, plus the client, prospect and people pages by name (or the count, if there are
  more than about eight). Mention `index.md` is the map Claude reads first.
- **Skills:** list each one in `.claude/skills/` with a few words on what it does, taken from its
  description.
- **Connectors:** what `connectors/crm.md` says about their CRM, and that every CRM write waits
  for a person to approve it.
- **Agents:** the files in `agents/`, and that they run as scheduled tasks once the owner sets
  them up (`HOW-TO-LOAD.md`).
If pages still say `NOT GIVEN` in important spots (prices, stages, "qualified"), say which ones
in a line.

**2. How to ask for things.** You just say it in plain words, or type the skill name. Give one
example each, using their real names where they exist:
- Call prep: "Prep me for my call with [client or prospect]."
- After a call: "Run /post-call-debrief on my call with [name]." and paste the notes or
  transcript.
- Account brief: "Write an account brief for [client]."
- New information: "Ingest this." with a transcript, CRM export or email thread dropped in.
- Health check: "Run /lint." to find stale pages, overdue promises and contradictions.
Say that Claude only uses what's in the pages and the CRM, and marks anything else `NOT FOUND`.

**3. How to save and share.** In Claude Code, two lines cover most days:
- "Pull the latest AI OS." when you start, so you have everyone's latest pages.
- "Save and share my changes." when you've changed something. Claude puts it on a branch, saves
  it, sends it to GitHub and opens a pull request (a request for the owner to add it).
The owner checks each pull request and merges it. `TEAM-WORKFLOW.md` has the details and the
by-hand version.

**4. What the owner does each week.** Point to `OWNER-CHECKLIST.md`. In short: Monday, merge the
week's pull requests and refresh the shared Claude Project; Friday, read the lint report and fix
the worst items. Offer to walk through it now.

**5. Bringing teammates in.** Two kinds of teammate:
- **People who'll use Claude Code:** the owner invites them on GitHub (the repo's Settings >
  Collaborators > Add people), then they open Claude Code in an empty folder that isn't synced
  by iCloud and paste:

  > Join my team's AI OS. The repo is {REPO_URL}. Get a copy on this computer in a folder that isn't synced by iCloud, open it, and walk me through how to use it.

  Fill in `{REPO_URL}` with the repo's real address from `git remote -v` (as a
  `https://github.com/...` link) so the owner can copy the prompt as-is.
- In Claude Code, offer to send the invites for the owner: ask for each teammate's GitHub
  username, show the exact list, and only after a clear yes run
  `gh api -X PUT repos/<owner>/<repo>/collaborators/<username> -f permission=push` once per
  person. Never send an invite without asking first, and never add anyone they didn't name.
- **Everyone else:** they don't need git. They use the shared Claude Project (section 6).

**6. The shared Claude Project.** For reps who won't use Claude Code. The owner bundles the pages
into a few files, uploads them to a shared Project on the Team plan, and uploads the skills for
the whole organization. `HOW-TO-LOAD.md` walks through it. In Claude Code, offer to run
`python3 tools/build_project_bundle.py` now, then tell them where the files landed
(`dist/project-files/` and `dist/skills/`).

**7. The one tip.** "If any of this seems confusing, just remember the way to learn AI is to ask
it questions." Any time, they can ask: "How do I use this? Explain it to me like I'm 12."

## At the end

Ask which part they want to go deeper on, or offer a first real task: "Want to try call prep on
one of your real calls?" If the tour turned up a gap (a `NOT GIVEN` price, no clients yet),
suggest the fix in one line: `/setup-os` to redo a section, or `/ingest` with a file.
