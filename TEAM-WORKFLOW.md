> **File type: guide.** For the whole team. How changes to the AI OS get shared using git and GitHub, in plain English. Claude: if someone asks how to save, share or update the AI OS, walk them through the matching section here one step at a time.

# Team workflow: sharing the AI OS with git

## The idea in one paragraph

The copy of the AI OS on GitHub is the master. Everyone who works on it has their own copy on
their computer. **Pull** means "get the latest from GitHub". **Commit** means "save a snapshot of
my changes with a note". **Push** means "send my snapshot up to GitHub". A **branch** is your own
side copy, so your changes don't land on the master until someone checks them. A **pull request**
(PR) is you asking the owner "please add my changes to the master". The owner reviews it and
**merges** it, then everyone pulls.

You don't need to remember git commands. Every step below has a button in VS Code and in GitHub
Desktop. And if you're stuck, ask Claude: "Walk me through pulling the latest AI OS, step by
step."

## Who edits what

| Who | Does | How |
|---|---|---|
| Reps | Add call transcripts and notes | Drop the file in `raw/transcripts/` and run `/ingest`, or send it to the owner. Open a PR with the result |
| Reps | Fix a wrong fact on a client page | Edit the page (or ask Claude to), open a PR |
| Owner | Reviews and merges every PR to `wiki/` | GitHub, in the pull request |
| Owner only | Changes `CLAUDE.md`, `.claude/skills/`, `connectors/`, `agents/`, `tools/` | Same flow; nobody else merges these |
| Everyone else | Uses the shared Claude Project | No git needed. The owner keeps the Project in sync |

Reps who'd rather not touch git at all can work only in the Claude Project and send transcripts
to the owner, who runs `/ingest`.

## One-time setup

1. Accept the GitHub invite the owner sends you.
2. Get a copy on your computer (this is called **cloning**):
   - **VS Code:** open the Source Control panel (the branch-shaped icon on the left) and click
     **Clone Repository**. Paste the repo's URL from GitHub (green **Code** button), pick a
     folder, then click **Open**.
   - **GitHub Desktop:** **File > Clone repository**, pick the AI OS repo from the list, choose a
     folder, **Clone**.
   - **Terminal:** `git clone <repo URL>`
3. If you use Claude Code, open that folder in it. The skills show up as `/call-prep` and so on.

## Every day: pull before you start

- **VS Code:** Source Control panel > the **...** menu > **Pull**. (Or click the sync arrows in
  the bottom-left status bar.)
- **GitHub Desktop:** click **Fetch origin**, then **Pull origin** if it appears.
- **Terminal:** `git pull`

Pulling first means Claude reads this week's pages, and your changes won't clash with someone
else's.

## Making a change

1. **Start a branch.** Name it after what you're doing, like `ingest-acme-call`.
   - VS Code: click the branch name in the bottom-left corner > **Create new branch**.
   - GitHub Desktop: **Current Branch > New Branch**.
   - Terminal: `git switch -c ingest-acme-call`
2. **Make the change.** Drop a transcript in `raw/transcripts/` and run `/ingest`, or edit a page.
   Read what Claude changed before you go on.
3. **Commit** (save a snapshot with a short note like "Ingest Acme call 2026-11-03").
   - VS Code: in Source Control, click **+** next to each changed file (or **+** on the "Changes"
     row for all of them), type the note in the message box, click **Commit**.
   - GitHub Desktop: tick the changed files, type the note in **Summary**, click **Commit to
     <branch>**.
   - Terminal: `git add -A` then `git commit -m "Ingest Acme call 2026-11-03"`
4. **Push** (send it to GitHub).
   - VS Code: click **Publish Branch** (first time) or **Sync Changes**.
   - GitHub Desktop: **Publish branch** (first time) or **Push origin**.
   - Terminal: `git push -u origin ingest-acme-call`
5. **Open a pull request.** Go to the repo on GitHub. A yellow banner offers **Compare & pull
   request**; click it, say in a line what changed, and click **Create pull request**. In GitHub
   Desktop you can also use **Branch > Create Pull Request**.
6. **Wait for the owner to merge it.** Then switch back to `main` and pull.

## For the owner: reviewing and merging

1. Open the pull request on GitHub and click **Files changed**. Read the diff: red is removed,
   green is added.
2. Check the facts. Watch for prices that aren't in `services-and-pricing`, dates that don't match
   the CRM, and anything Claude may have guessed.
3. Comment if something needs fixing, or click **Merge pull request**.
4. If wiki pages changed, re-sync the Claude Project (below).

Tip: in the repo's Settings you can add a branch rule for `main` that requires a pull request
before merging. Then nobody can change the master by accident.

## Re-syncing the Claude Project after a merge

The shared Claude Project holds a snapshot, so it doesn't update itself.

1. Pull `main` on your computer.
2. Run `python3 tools/build_project_bundle.py` (or ask Claude Code to run it).
3. In the Claude Project, delete the old numbered files and upload the new ones from
   `dist/project-files/`.
4. If a skill changed, upload its new zip from `dist/skills/` under Organization settings >
   Library.

Doing this once a week (Monday) is usually enough. See `OWNER-CHECKLIST.md`.

## When something goes wrong

- **"Merge conflict":** two people changed the same lines. Don't panic and don't force anything.
  Ask Claude Code "help me resolve this merge conflict", or ask the owner.
- **"Your branch is behind":** pull, then try again.
- **Committed to `main` by mistake:** tell the owner before pushing. It's an easy fix.
- **Never** use "force push" on `main`.
