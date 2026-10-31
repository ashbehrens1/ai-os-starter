---
name: ingest
description: Files a new source (call transcript, CRM export, email thread, meeting notes) into the AI OS knowledge base. Writes a source page and updates every client, prospect or person page it touches. Trigger on "/ingest", "file this call", "add this to the knowledge base", "update the wiki from this transcript".
---
> **File type: skill.** Claude follows this to keep the knowledge base current. In Claude Code it edits files; in the Claude app it drafts the text for the owner to save.

# Ingest

**In:** one source: a transcript, export, email thread or notes. Optional: which client it's about.

**Read:** `index.md`; the client or prospect page the source is about; the people pages for
anyone named; `sales-process` if a deal moved; `wiki/sources/_source-template.md`.

**Steps**
1. Identify the client or prospect. If the source doesn't make it clear, ask. Don't guess. If
   it's a new company, offer to start a page from the client or prospect template.
2. Save the source to `raw/` unchanged (transcripts in `raw/transcripts/`, exports in
   `raw/exports/`) as `YYYY-MM-DD-<company>-<what>.md` if it isn't there already.
3. Write a source page for `wiki/sources/`, named `<company>-<what>-<YYYY-MM-DD>.md`, from the
   source template: date, attendees, key points, what each side promised (with dates where
   given), outcome, and the raw file path.
4. For each page the source touches, update only these sections: Last conversation, Open
   promises, Next step, History (one new dated line). Keep every other section as it is, and set
   `updated:` to today.
5. If the source contradicts something on a page (a price, a date, an owner), don't change it.
   List it under "For the owner" with both versions.
6. Add the `index.md` line if a page is new, and one `log.md` entry:
   `## [YYYY-MM-DD] ingest | <source title>` plus the pages changed.

**Out:**
1. The new source page, in full.
2. Each changed section, under the page name.
3. The `index.md` and `log.md` lines.
4. For the owner: contradictions and anything NOT FOUND.

**Where you're running:** in Claude Code (or Cowork with the folder open), make the edits
directly and show what changed. Remind the person to commit on a branch and open a pull request
(see `TEAM-WORKFLOW.md`). In a claude.ai Project, files are read-only, so output each changed
page in full under its path for the owner to save.

Never invent a promise, date or price that isn't in the source. Never write to the CRM from this
skill; `/post-call-debrief` handles CRM updates.
