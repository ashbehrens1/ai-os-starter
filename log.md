> **File type: log.** Append-only record of every change to the AI OS. Newest at the bottom. Claude adds one entry per setup, ingest or lint run.

# Log

Entry format: `## [YYYY-MM-DD] <operation> | <what>` then a few bullets naming the pages changed.

## [start] init | Created from the AI OS Starter template

- Empty template. No company facts yet. Run `/setup-os` to fill it in.
