> **File type: guide.** For the AI OS owner. The weekly and monthly upkeep that keeps the AI OS worth using. Claude: if the owner asks "what do I need to do this week?", work through this list with them.

# Owner checklist

## Once, at the start
- [ ] Ask Claude Code to set up your AI OS (the prompt in `START-HERE.md`). It makes your
      private repo and runs `/setup-os`. Read every page it wrote and fix what's wrong.
- [ ] Let Claude save the first version to GitHub, then take the `/tour`. Invite the people
      who'll edit it (Claude can send the GitHub invites if you ask).
- [ ] Add a branch rule on `main` that requires a pull request (repo Settings).
- [ ] Build the bundle and set up the shared Claude Project, skills, CRM connector and both
      scheduled tasks (`HOW-TO-LOAD.md`).
- [ ] Run `/call-prep` on two real upcoming calls and check every fact against what you know.

## Every Monday
- [ ] Merge the week's pull requests. Read each diff; check prices, dates and owners.
- [ ] Pull `main` and run `python3 tools/build_project_bundle.py`.
- [ ] Replace the files in the Claude Project with the new ones in `dist/project-files/`.
- [ ] Upload any changed skill zips under Organization settings > Library.
- [ ] Refresh `wiki/overview.md` for the week (or ask Claude: "update the overview for this
      week from the client and prospect pages").
- [ ] Glance at the Monday pipeline review. If it flagged the same deal two weeks running, talk
      to the owner of that deal.

## Every Friday
- [ ] Read the weekly lint report.
- [ ] Fix the most serious items first: contradictions, overdue promises, prices.
- [ ] Fill in any `NOT GIVEN` gaps you now know the answer to.
- [ ] Commit and push your fixes, so Monday's bundle has them.

## Monthly
- [ ] Prune: move lost prospects to `status: churned` or delete them, and remove people who
      left.
- [ ] Check `services-and-pricing` against your current price list.
- [ ] Check stage names in `sales-process` and the Monday prompt still match the CRM.
- [ ] Ask the team which skill output they keep fixing by hand. Change that skill.
- [ ] Add one new skill only when the team repeats the same job every week.

## Rules of thumb
- If a fact is true about a client, it goes on the client page.
- When a skill gets something wrong, fix the page or the skill, not the chat.
- This kit hasn't been run end to end on your team yet. For the first few weeks, check what
  Claude writes before anyone sends it.
