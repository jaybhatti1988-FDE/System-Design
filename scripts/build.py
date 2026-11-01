#!/usr/bin/env python3
"""Split source/system-design-100.md into one page per question and refresh the README index.

Usage:  python scripts/build.py
"""
import re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "source" / "system-design-100.md"
DOCS = ROOT / "docs"
README = ROOT / "README.md"

PART_RE = re.compile(r"^## (Part ([A-Z]):\s*(.+))$", re.M)
Q_RE = re.compile(r"^### (\d+)\.\s*(.+)$", re.M)

PART_DIRS = {"A": "01-fundamentals", "B": "02-classic-designs", "C": "03-advanced-patterns"}

def slug(t):
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")[:60]

def main():
    if not SRC.exists():
        raise SystemExit(f"Missing {SRC}. Export your doc as Markdown and save it there.")
    text = SRC.read_text(encoding="utf-8").replace("%%", "%")
    parts = list(PART_RE.finditer(text))
    index = []
    for i, p in enumerate(parts):
        letter, title = p.group(2), p.group(3).strip()
        body = text[p.end(): parts[i + 1].start() if i + 1 < len(parts) else len(text)]
        d = DOCS / PART_DIRS.get(letter, f"part-{letter.lower()}")
        d.mkdir(parents=True, exist_ok=True)
        for old in d.glob("*.md"):
            old.unlink()
        qs = list(Q_RE.finditer(body))
        rows = []
        for j, q in enumerate(qs):
            num, qt = int(q.group(1)), q.group(2).strip()
            content = body[q.end(): qs[j + 1].start() if j + 1 < len(qs) else len(body)].strip()
            name = f"{num:03d}-{slug(qt)}.md"
            prev_l = f"[← Previous]({{prev}})" if j else ""
            (d / name).write_text(
                f"# {num}. {qt}\n\n> Part {letter}: {title}\n\n{content}\n\n---\n"
                f"[⬆ Back to index](../../README.md#-question-index)\n", encoding="utf-8")
            rows.append(f"| {num} | [{qt}](docs/{d.name}/{name}) |")
        index.append(f"### Part {letter}: {title}\n\n| # | Question |\n|--:|:--|\n" + "\n".join(rows) + "\n")
    block = "<!-- INDEX:START -->\n" + "\n".join(index) + "<!-- INDEX:END -->"
    r = README.read_text(encoding="utf-8")
    r = re.sub(r"<!-- INDEX:START -->.*?<!-- INDEX:END -->", lambda _: block, r, flags=re.S)
    README.write_text(r, encoding="utf-8")
    print(f"Built {sum(i.count('| [') for i in index)} question pages.")

if __name__ == "__main__":
    main()
