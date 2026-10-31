---
name: setup-os
description: Interviews the AI OS owner a few questions at a time (company, offers and pricing, sales process and what "qualified" means, voice with example emails, team and roles, first clients and prospects, CRM) and writes the wiki pages, CLAUDE.md, index.md and log.md from the templates. Gaps stay NOT GIVEN. Trigger on "/setup-os", "set up the AI OS", "fill in the AI OS", "set this up for me".
---
> **File type: skill.** Claude follows this to fill in a blank AI OS by interviewing the owner. Run it once at the start, and again any time you want to redo a section.

# Set up the AI OS

**In:** nothing. The owner answers questions in the chat. They can also drop files in at any
point: a price sheet, a CRM export, a few sent emails, an org chart.

**Read first:** `CLAUDE.md`, `index.md`, and the templates: `wiki/overview.md`,
`wiki/entities/company.md`, `wiki/offers/services-and-pricing.md`,
`wiki/playbooks/sales-process.md`, `wiki/brand/voice.md`, and the four `_...-template.md` files.
If the templates aren't available (a plain chat with no files), use the section lists in
`CLAUDE.md` § Page shapes. If `CLAUDE.md` isn't available either, ask the owner to add the AI OS
files before starting.

## Where you're running

Work this out before the first question and say it in one line.

- **You can edit files** (Claude Code, or Cowork with the AI OS folder open): write each page
  straight into the folder as you go. Show a short summary of what changed after each batch.
- **You can't edit files** (a claude.ai chat or Project): after each batch, output every page that
  batch filled, in full, each under a heading with its exact path (e.g. `wiki/brand/voice.md`), in
  a code block. Tell the owner to save each one over the file with that path. At the end, remind
  them to run `tools/build_project_bundle.py` (or ask someone technical to) and re-upload.

## How to run the interview

1. Say what's about to happen in two or three lines: seven short batches,
   skip anything, answer in rough notes, files are welcome.
2. Ask **one batch at a time**. Number the questions so the owner can answer "1: ..., 2: ...".
3. After each answer, play back what you heard in a few bullets and ask "Anything wrong or
   missing?" before writing. Then write that batch's pages.
4. Anything skipped or unknown is written `NOT GIVEN`. Never fill a gap with a guess, an example
   or a typical industry number. If an answer is vague ("depends"), write what they said and
   flag it.
5. If a page already has real content (not template tokens), show what's there and ask before
   replacing it. Don't overwrite real facts silently.
6. Keep it moving. One follow-up question at most per batch, only when an answer is needed for a
   skill to work (stage names, the "qualified" test, prices).

## The batches

**Batch 1: Company.** Company name? What you sell, in one line? Who buys (job titles, type and
size of customer)? Team size and location? Timezone? Who owns this AI OS (name and email)?
Writes: `wiki/entities/company.md` (top half), the Who we are section of `CLAUDE.md`.

**Batch 2: Offers and pricing.** Each offer or tier: name, what's included, price (or "from"
price)? Add-ons? Contract length and renewal terms? Discount rules, who signs off a quote, who
signs contracts? How you work out a deal amount for the CRM?
Writes: `wiki/offers/services-and-pricing.md`.

**Batch 3: Sales process.** Your pipeline stages, named exactly as they are in your CRM, and
what each one means? What does "qualified" mean for you (the checklist a deal has to pass)? The
Monday rule: by default, every open deal needs a next step and activity in the last 14 days; keep
14 or change it? Who gets the Monday review (name and email)? Discovery questions you always ask?
Two or three objections you hear most, and your answer?
Writes: `wiki/playbooks/sales-process.md`.

**Batch 4: Voice.** How do you want client emails to sound, in a few words? Word limit? How do
you sign off? Phrases you never want to see? Paste two or three real emails you were happy with
(take out anything private first).
Writes: `wiki/brand/voice.md`, and the pasted emails to `raw/exports/email-examples.md`.

**Batch 5: Team and roles.** For each person who sells or touches clients: name, role, email,
which accounts they own, and anything they sign off on? Who manages the reps?
Writes: one `wiki/entities/people/<first-last>.md` per person, and the Team table in
`company.md`.

**Batch 6: First clients and prospects.** Pick three to five to start with (your biggest or most
active). For each: name, client or prospect, main contact and role, account owner, what they
bought or are looking at, fee or deal amount, stage, the next step with a date, anything promised
either way. A CRM export or tracker dropped into the chat works too.
Writes: one page per client or prospect from the templates.

**Batch 7: CRM.** Which CRM? Is it connected to Claude yet? Who is the CRM admin? Fields every
deal must have? Anything Claude must never change (owners, amounts, closed deals)?
Writes: `connectors/crm.md` (fill in the CRM name, admin and rules; keep the HubSpot section
only if they use HubSpot), the Required CRM fields table in `sales-process.md`, the Tools
section of `company.md`.

## After the last batch

1. **Fill the placeholders** everywhere else: `CLAUDE.md`, `index.md`, `wiki/overview.md`,
   `agents/monday-pipeline-review.md`, `agents/weekly-lint.md`, `connectors/crm.md`. Replace each
   capital-letter token in curly braces with the answer, or `NOT GIVEN`. Don't touch the
   `_...-template.md` files; they stay as templates.
2. **Swap the banners.** On every page you filled, replace the "template page" banner line with
   `> **File type: wiki page.** Part of the {company} AI OS. Edit by hand or with /ingest.`
   (with the real company name).
3. **Update `index.md`:** list every new client, prospect and person page, with the counts.
4. **Add one entry to `log.md`:** `## [YYYY-MM-DD] setup | AI OS filled in by /setup-os`, then
   bullets for the pages written and how many `NOT GIVEN` gaps are left.
5. **Report back** in one short list: pages written, the `NOT GIVEN` gaps grouped by page (most
   important first: prices, stages, "qualified"), and any placeholder tokens still left.
6. **Next steps for the owner:**
   - Read the pages. Fix anything that's wrong; this is your team's source of truth now.
   - Try it: "Run /call-prep for [one of the clients you gave me]."
   - In Claude Code, suggest the first save to GitHub and offer to run it:
     `git add -A`, `git commit -m "Set up the AI OS"`, `git push`. Then point to
     `TEAM-WORKFLOW.md` for how the team works with it.
   - For the team's Claude Project, point to `HOW-TO-LOAD.md`.

## Rules

- Never invent a client, price, date, person or fact. `NOT GIVEN` is a fine answer.
- Prices go only in `services-and-pricing.md`. Other pages link to it.
- Use the owner's words for stage names, offer names and the "qualified" test. Don't tidy them
  into something else.
- Don't connect, read or write the CRM during setup. This skill only writes AI OS files.
- If the owner wants to stop partway, write what you have, log it, and tell them which batch to
  pick up from next time ("run /setup-os and start at batch 5").
