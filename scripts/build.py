#!/usr/bin/env python3
"""Build the handbook.

* Splits the questions .md in source/ into one page per question
* Replaces ASCII diagrams with Mermaid flowcharts (scripts/diagrams.py)
* Links questions to deep-dive pages
* Refreshes the README question index and deep-dive list

Usage:  python scripts/build.py
"""
import re, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from diagrams import DIAGRAMS, DEEP_DIVES  # noqa: E402

DOCS = ROOT / "docs"
README = ROOT / "README.md"
PART_RE = re.compile(r"^## (Part ([A-Z]):\s*(.+))$", re.M)
Q_RE = re.compile(r"^### (\d+)\.\s*(.+)$", re.M)
FENCE_RE = re.compile(r"```[^\n]*\n.*?```", re.S)
PART_DIRS = {"A": "01-fundamentals", "B": "02-classic-designs", "C": "03-advanced-patterns"}


def find_src():
    c = sorted(f for f in (ROOT / "source").glob("*.md") if f.name.lower() != "readme.md")
    if not c:
        raise SystemExit("No questions file found. Put your .md file in the source/ folder.")
    return c[0]


def slug(t):
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")[:60]


def deep_title(path):
    first = path.read_text(encoding="utf-8").splitlines()[0]
    return re.sub(r"^#\s*(Deep Dive:\s*)?", "", first).strip()


def replace_marked(text, name, block):
    pat = re.compile(rf"<!-- {name}:START -->.*?<!-- {name}:END -->", re.S)
    new = f"<!-- {name}:START -->\n{block}\n<!-- {name}:END -->"
    return pat.sub(lambda _: new, text)


def main():
    text = find_src().read_text(encoding="utf-8").replace("%%", "%")
    parts = list(PART_RE.finditer(text))
    index, total = [], 0
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
            if num in DIAGRAMS:
                mer = "```mermaid\n" + DIAGRAMS[num] + "\n```"
                content = FENCE_RE.sub(lambda _: mer, content, count=1)
            extra = ""
            if num in DEEP_DIVES:
                dd = DOCS / "deep-dives" / DEEP_DIVES[num]
                if dd.exists():
                    extra = f"\n\n> 📘 **Want more?** Read the [deep dive: {deep_title(dd)}](../deep-dives/{dd.name})"
            name = f"{num:03d}-{slug(qt)}.md"
            (d / name).write_text(
                f"# {num}. {qt}\n\n> Part {letter}: {title}\n\n{content}{extra}\n\n---\n"
                f"[⬆ Back to index](../../README.md#-question-index)\n", encoding="utf-8")
            star = " 📘" if num in DEEP_DIVES else ""
            rows.append(f"| {num} | [{qt}](docs/{d.name}/{name}){star} |")
            total += 1
        index.append(f"### Part {letter}: {title}\n\n| # | Question |\n|--:|:--|\n" + "\n".join(rows) + "\n")

    deep = sorted((DOCS / "deep-dives").glob("*.md"))
    dlines = ["| # | Deep dive |", "|--:|:--|"] + [
        f"| {k} | [{deep_title(f)}](docs/deep-dives/{f.name}) |" for k, f in enumerate(deep, 1)]
    r = README.read_text(encoding="utf-8")
    r = replace_marked(r, "INDEX", "\n".join(index))
    r = replace_marked(r, "DEEP", "\n".join(dlines))
    README.write_text(r, encoding="utf-8")
    print(f"Built {total} question pages, {len(DIAGRAMS)} Mermaid diagrams, {len(deep)} deep dives.")


if __name__ == "__main__":
    main()
