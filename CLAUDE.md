> **File type: schema.** Claude reads this first in every session. It says how the AI OS is laid out, what each page looks like, and the three things Claude does with it: ingest, query and lint.

# {COMPANY_NAME} AI OS

Read this file first, then `index.md`. Open only the pages the task needs.

> **Not set up yet?** If this file still has capital-letter tokens in curly braces (like the company name above), the AI OS hasn't been
> filled in. Run `/setup-os` (or follow `START-HERE.md`) before using the other skills.

## Who we are

{COMPANY_NAME} {ONE_LINE_DESCRIPTION}. We are {TEAM_SIZE} people, based in {LOCATION}. Our
timezone is {TIMEZONE}. {SALES_MANAGER} runs the pipeline and gets the Monday pipeline review.
{OS_OWNER} owns the AI OS ({OS_OWNER_EMAIL}). Our CRM is {CRM_NAME}.

## Layout

| Layer | Where | What it holds | Who writes it |
|---|---|---|---|
| Schema | `CLAUDE.md` (this file) | Layout, page shapes, operations, rules | {OS_OWNER}, by hand |
| Map | `index.md`, `log.md` | Catalog of every page; append-only record of changes | Claude, during setup, ingest and lint |
| Sources | `raw/` | Call transcripts, CRM exports, datasets, example emails. Never edited | Anyone drops files in |
| Knowledge base | `wiki/` | One page per client, prospect and person, plus company, offers, playbooks and brand | Claude, from sources; {OS_OWNER} approves |
| Skills | `.claude/skills/` | The jobs we repeat, one `SKILL.md` each | {OS_OWNER} |
| Connectors | `connectors/` | Which live tools are connected, what each may read and write | {OS_OWNER} |
| Agents | `agents/` | Scheduled jobs and their prompts | {OS_OWNER} |

The wiki holds what changes slowly: who a client is, what they bought, what we promised. The CRM
connector holds what changes daily: deal stage, amount, last activity, owner. Don't copy CRM data
into the wiki; write down the decisions that come out of it.

## Page shapes

Every wiki page starts with frontmatter:

```yaml
---
title: Example Client Co
type: client          # client | prospect | person | entity | offer | playbook | brand | source
status: active        # active | prospect | churned | n/a
tags: [client]
sources: [setup-os]   # where the facts came from: setup-os, a raw file name, a CRM export
updated: YYYY-MM-DD
---
```

Each page shape has a template. Copy the template, keep the section order, and fill it in.

- **Client** (`wiki/entities/clients/`, template `_client-template.md`): Snapshot (table: industry,
  city, contact, account owner, service, monthly fee, start date, renewal date, status, health),
  Who they are, What they bought, Open promises, Last conversation, Next step, Renewal and risks,
  History.
- **Prospect** (`wiki/entities/prospects/`, template `_prospect-template.md`): Snapshot (table:
  industry, size, city, contacts and their roles, account owner, evaluating, stage, deal amount,
  close date), Who they are, What they need, Open promises, Last conversation, Next step, Risks and
  blockers, Timeline.
- **Person** (`wiki/entities/people/`, template `_person-template.md`): Role, Email, What they do,
  Accounts they own, How to work with them, Notes.
- **Source** (`wiki/sources/`, template `_source-template.md`): one raw file summarised: date,
  attendees, key points, what was promised, outcome, and the raw file's path.
- **Company, offers, playbooks, brand:** one page each, already in the folder as templates
  (`company`, `services-and-pricing`, `sales-process`, `voice`). Keep their section headings.

File names are lowercase with hyphens: `example-client-co.md`. Templates start with `_` and are
never treated as real pages. Link pages with `[[page-name]]`. One fact lives on one page; other
pages link to it. Prices live only in `services-and-pricing`.

Anything the owner hasn't told us is written `NOT GIVEN`. Anything a skill looked for and couldn't
find is written `NOT FOUND`. Both get flagged; neither gets guessed.

## Operations

### Ingest: a new source comes in
Run `/ingest` with the file (a transcript, an export, an email thread).
1. Save the file to `raw/` unchanged.
2. Write a source page in `wiki/sources/`.
3. Update every page the source touches: the client or prospect page (Last conversation, Open
   promises, Next step, History), and people pages if roles changed.
4. Update `index.md` if a page was added, and add a line to `log.md`.
5. If the source contradicts a page, don't overwrite it. Flag it for {OS_OWNER} with both versions.

### Query: someone asks a question
1. Read `index.md`, then open only the pages the question needs.
2. For a client or prospect, open that one page. For prices use `services-and-pricing`, for how we
   sell and what "qualified" means use `sales-process`, for how we write use `voice`.
3. For live deal data, use the CRM connector (`connectors/crm.md`). If the wiki and the CRM
   disagree, show both.
4. Anything not in the wiki, a connector or the chat is NOT FOUND. Say so and ask.
5. If the answer is worth keeping (a decision, a new promise), offer to file it back to the page.

### Lint: weekly health check
Run `/lint`, or let the `weekly-lint` agent do it on Fridays. It checks for contradictions between
pages, pages not updated in 60 days, open promises past their date, pages missing from `index.md`,
broken `[[links]]`, leftover placeholder tokens (capital words in curly braces), and wiki facts that disagree with the CRM. It
reports; {OS_OWNER} fixes.

In the Claude app, Project files are read-only to Claude, so setup, ingest and lint there produce
the updated page text for {OS_OWNER} to save and re-upload. In Claude Code they edit the files
directly.

## Saving and sharing (git)

In Claude Code, when someone asks you to save, share, update or "push" their changes, do the git
steps for them:

1. Pull the latest first (`git pull`) so you start from everyone's current pages.
2. Make the change on a branch named for it, like `ingest-acme-call`, never straight on `main`.
   The owner's small fixes (a typo, a date) are the one exception, and only if they ask.
3. Commit with a short message that says what changed, like "Add call notes for Acme".
4. Push the branch and open a pull request (`gh pr create` if GitHub CLI is set up; otherwise give
   the person the link GitHub prints). Say in the pull request what changed and which sources it
   came from.
5. Tell the person what you did in two or three lines, with the pull request link.

Never force-push, never delete branches or files without being asked, and never merge a pull
request yourself. Only {OS_OWNER} merges. If git asks for a login or something fails, stop and
tell the person what it said instead of trying workarounds.

## Rules

- Never invent client names, prices, dates or facts.
- Only quote prices that are in `services-and-pricing`. Anything marked NOT GIVEN gets flagged.
- Drafts only. Nothing is sent, and no CRM record changes, without the account owner's OK.
- CRM write tools are set to Needs Approval. Propose the change, show old and new values, and
  wait. See `connectors/crm.md`.
- Today's date is stated in the chat or the task. If it isn't, ask.
- Write like us. See `voice` for the rules and the word limit on client emails.
- If it's true about a client, it goes on the client page, not into somebody's chat. Tell
  {OS_OWNER} when a page or skill is wrong; don't work around it.
