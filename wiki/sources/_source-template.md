---
title: {CLIENT_OR_PROSPECT} {WHAT}, {YYYY-MM-DD}
type: source
status: n/a
tags: [source]
sources: [{RAW_FILE_NAME}]
updated: {DATE}
---
> **File type: template.** `/ingest` copies this to `wiki/sources/<client>-<what>-<YYYY-MM-DD>.md` for each new raw file (a call transcript, an export, an email thread). One source page per raw file.

# {CLIENT_OR_PROSPECT} {WHAT}, {YYYY-MM-DD}

Raw file: `raw/{FOLDER}/{FILE_NAME}`

**Attendees:** {OUR_SIDE} ({COMPANY_NAME}), {THEIR_SIDE} ({CLIENT_OR_PROSPECT}).
**Date:** {YYYY-MM-DD}, {LENGTH}.

## Key points
- {POINT}

## Promises made
- Ours: {PROMISE} (owner, date, or NO DATE GIVEN)
- Theirs: {PROMISE} (owner, date, or NO DATE GIVEN)

## Outcome
{WHAT_CHANGED}: stage, next step, anything that contradicts a page. See [[{CLIENT_OR_PROSPECT_PAGE}]].
