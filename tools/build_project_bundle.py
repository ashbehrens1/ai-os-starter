#!/usr/bin/env python3
"""Bundle the AI OS into a few upload files for a shared Claude Project, and zip each skill.

Run from the repo root:  python3 tools/build_project_bundle.py
Writes (both gitignored, safe to delete and rebuild):
  dist/project-files/0N-*.md   upload these to the Claude Project
  dist/skills/<name>.zip       upload these under Organization settings > Library
Standard library only. Re-run after every merge that changes wiki pages or skills.
"""
import pathlib
import re
import shutil
import zipfile

root = pathlib.Path(__file__).resolve().parent.parent
wiki = root / "wiki"
out = root / "dist"
shutil.rmtree(out, ignore_errors=True)
(out / "project-files").mkdir(parents=True)
(out / "skills").mkdir()

FRONTMATTER = re.compile(r"^---\n.*?\n---\n", re.S)
PLACEHOLDER = re.compile(r"\{[A-Z][A-Z0-9_]+\}")
used = set()
warnings = []


def pages(folder, pattern="*.md"):
    """Real pages in a folder, sorted. Files starting with _ are templates and are skipped."""
    folder = root / folder
    if not folder.exists():
        return []
    return sorted(p for p in folder.glob(pattern) if p.is_file() and not p.name.startswith("_"))


def existing(*paths):
    return [root / p for p in paths if (root / p).exists()]


def bundle(name, paths, header):
    parts = [f"# {header}\n"]
    if not paths:
        parts.append("\nNo pages yet. Run /setup-os or /ingest to add some.\n")
    for p in paths:
        used.add(p.resolve())
        text = FRONTMATTER.sub("", p.read_text(encoding="utf-8"), count=1)
        rel = p.relative_to(root).as_posix()
        left = sorted(set(PLACEHOLDER.findall(text)))
        if left:
            warnings.append(f"{rel}: {len(left)} placeholder(s) not filled, e.g. {', '.join(left[:3])}")
        parts.append(f"\n\n---\n<!-- source: {rel} -->\n{text.strip()}\n")
    (out / "project-files" / name).write_text("".join(parts), encoding="utf-8")


company = "AI OS"
lines = (root / "CLAUDE.md").read_text(encoding="utf-8").splitlines()
for line in lines:
    if line.startswith("# "):
        company = line[2:].strip()
        break

bundle("01-instructions.md",
       existing("CLAUDE.md", "index.md", "wiki/overview.md"),
       f"{company}: instructions and index")

core = (existing("wiki/entities/company.md", "connectors/crm.md")
        + pages("wiki/offers") + pages("wiki/playbooks") + pages("wiki/brand"))
# Any other wiki page that doesn't fit a folder below lands here, so nothing is left out.
later = {"wiki/entities/clients", "wiki/entities/prospects", "wiki/entities/people", "wiki/sources"}
skip = set(core) | {wiki / "overview.md"}
for p in sorted(wiki.rglob("*.md")):
    rel_dir = p.parent.relative_to(root).as_posix()
    if not p.name.startswith("_") and rel_dir not in later and p not in skip:
        core.append(p)
bundle("02-company-offers-process-voice.md", core, "Company, CRM rules, offers, sales process and voice")

clients = pages("wiki/entities/clients")
bundle("03-clients.md", clients, f"Clients ({len(clients)})")
prospects = pages("wiki/entities/prospects")
bundle("04-prospects.md", prospects, f"Prospects ({len(prospects)})")
people = pages("wiki/entities/people")
bundle("05-team.md", people, f"Team ({len(people)})")
notes = (pages("wiki/sources") + pages("raw/transcripts") + pages("raw/transcripts", "*.txt")
         + pages("raw/exports"))
bundle("06-call-notes-and-sources.md", notes, "Call notes, transcripts and source files")

skills_dir = root / ".claude" / "skills"
for d in sorted(skills_dir.iterdir()) if skills_dir.exists() else []:
    if (d / "SKILL.md").exists():
        with zipfile.ZipFile(out / "skills" / f"{d.name}.zip", "w", zipfile.ZIP_DEFLATED) as z:
            for f in sorted(d.rglob("*")):
                if f.is_file() and f.name not in (".gitkeep", ".DS_Store"):
                    z.write(f, f"{d.name}/{f.relative_to(d).as_posix()}")

total = 0
for f in sorted(out.rglob("*")):
    if f.is_file():
        total += f.stat().st_size
        print(f"{f.relative_to(out).as_posix():45} {f.stat().st_size / 1024:6.1f} KB")
print(f"{'total':45} {total / 1024:6.1f} KB")
if warnings:
    print("\nHeads up: these pages still have placeholders. Run /setup-os or fill them by hand:")
    for w in warnings:
        print(f"  {w}")
