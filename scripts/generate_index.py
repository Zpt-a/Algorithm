# -*- coding: utf-8 -*-
# @Time    : 2026/10/20 11:07
# @Author  : Zpt
# @Email   : zpta_super@163.com
# @File    : generate_index.py
# @Project : Algorithm
# @Software: PyCharm
#!/usr/bin/env python3
"""扫描所有题目，重新生成根 README 索引和按标签聚合的索引页。"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RANGE_DIR_RE = re.compile(r"^\d{4}-\d{4}$")
PROBLEM_DIR_RE = re.compile(r"^(\d{4})\.(.+)$")

LANG_BY_EXT = {
    ".py": "Python",
    ".cpp": "C++",
    ".cc": "C++",
    ".cxx": "C++",
    ".java": "Java",
    ".go": "Go",
    ".rs": "Rust",
    ".ts": "TypeScript",
    ".js": "JavaScript",
    ".kt": "Kotlin",
    ".cs": "C#",
    ".swift": "Swift",
    ".rb": "Ruby",
    ".php": "PHP",
    ".scala": "Scala",
}


def parse_problem(path: Path, match: re.Match) -> dict:
    number = int(match.group(1))
    slug = match.group(2)
    readme = path / "README.md"
    title = slug
    difficulty = ""
    tags: list[str] = []

    if readme.exists():
        text = readme.read_text(encoding="utf-8")
        lines = text.splitlines()
        if lines:
            hm = re.match(r"^#\s*\d+\.\s*(.+?)\s*$", lines[0])
            if hm:
                title = hm.group(1)
        dm = re.search(r"\*\*难度\*\*\s*[:：]\s*(.+)", text)
        if dm:
            difficulty = dm.group(1).strip()
        tm = re.search(r"\*\*标签\*\*\s*[:：]\s*(.+)", text)
        if tm:
            tags = [t.strip() for t in re.split(r"[,，]", tm.group(1)) if t.strip()]

    langs: list[str] = []
    for f in sorted(path.iterdir()):
        if f.is_file() and f.stem.startswith("solution"):
            lang = LANG_BY_EXT.get(f.suffix.lower())
            if lang and lang not in langs:
                langs.append(lang)

    review_count = 0
    last_review = ""
    reviews_dir = path / "reviews"
    if reviews_dir.is_dir():
        review_files = sorted(reviews_dir.glob("*.md"))
        review_count = len(review_files)
        if review_files:
            last_review = max(f.stem[:10] for f in review_files)

    return {
        "number": number,
        "slug": slug,
        "title": title,
        "difficulty": difficulty,
        "tags": tags,
        "langs": langs,
        "review_count": review_count,
        "last_review": last_review,
        "rel": path.relative_to(ROOT),
    }


def find_problems() -> list[dict]:
    problems = []
    for d in sorted(ROOT.iterdir()):
        if not d.is_dir() or not RANGE_DIR_RE.match(d.name):
            continue
        for sub in sorted(d.iterdir()):
            if not sub.is_dir():
                continue
            m = PROBLEM_DIR_RE.match(sub.name)
            if m:
                problems.append(parse_problem(sub, m))
    problems.sort(key=lambda p: p["number"])
    return problems


def render_review_cell(p: dict) -> str:
    if not p["review_count"]:
        return "-"
    if p["last_review"]:
        return f"{p['review_count']} 次（最近 {p['last_review']}）"
    return f"{p['review_count']} 次"


def render_problem_index(problems: list[dict]) -> str:
    if not problems:
        return "_还没有题目。运行 `python scripts/new_problem.py ...` 创建第一道题。_"
    lines = [
        "| 题号 | 题目 | 难度 | 标签 | 语言 | 复习 |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for p in problems:
        num = f"{p['number']:04d}"
        link = f"[{num}](./{p['rel'].as_posix()}/)"
        tags = ", ".join(p["tags"]) if p["tags"] else "-"
        langs = ", ".join(p["langs"]) if p["langs"] else "-"
        diff = p["difficulty"] or "-"
        lines.append(
            f"| {link} | {p['title']} | {diff} | {tags} | {langs} | {render_review_cell(p)} |"
        )
    return "\n".join(lines)


def tag_slug(tag: str) -> str:
    slug = re.sub(r"[^\w]+", "-", tag.strip().lower(), flags=re.UNICODE)
    return slug.strip("-")


def build_tag_map(problems: list[dict]) -> dict[str, dict]:
    tag_map: dict[str, dict] = {}
    for p in problems:
        for tag in p["tags"]:
            slug = tag_slug(tag)
            if not slug:
                continue
            entry = tag_map.setdefault(slug, {"name": tag.strip(), "problems": []})
            if p not in entry["problems"]:
                entry["problems"].append(p)
    for entry in tag_map.values():
        entry["problems"].sort(key=lambda x: x["number"])
    return tag_map


def write_tag_pages(tag_map: dict[str, dict]) -> None:
    index_dir = ROOT / "index"
    index_dir.mkdir(exist_ok=True)
    for old in index_dir.glob("*.md"):
        old.unlink()
    for slug, entry in tag_map.items():
        lines = [
            f"# 标签：{entry['name']}",
            "",
            f"共 {len(entry['problems'])} 题。",
            "",
            "| 题号 | 题目 | 难度 | 语言 | 复习 |",
            "| --- | --- | --- | --- | --- |",
        ]
        for p in entry["problems"]:
            num = f"{p['number']:04d}"
            link = f"[{num}](../{p['rel'].as_posix()}/)"
            langs = ", ".join(p["langs"]) if p["langs"] else "-"
            diff = p["difficulty"] or "-"
            lines.append(
                f"| {link} | {p['title']} | {diff} | {langs} | {render_review_cell(p)} |"
            )
        (index_dir / f"{slug}.md").write_text(
            "\n".join(lines) + "\n", encoding="utf-8"
        )


def render_tag_index(tag_map: dict[str, dict]) -> str:
    if not tag_map:
        return "_还没有标签。在题目的 README.md 中填写 `**标签**：...` 后重新运行。_"
    lines = []
    for slug in sorted(tag_map):
        entry = tag_map[slug]
        count = len(entry["problems"])
        lines.append(f"- [{entry['name']}](./index/{slug}.md)（{count} 题）")
    return "\n".join(lines)


def replace_block(text: str, name: str, content: str) -> str:
    start = f"<!-- {name}_START -->"
    end = f"<!-- {name}_END -->"
    if start not in text or end not in text:
        print(
            f"警告：README.md 中缺少标记 {start} 或 {end}，跳过 {name} 更新。",
            file=sys.stderr,
        )
        return text
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.S)
    return pattern.sub(f"{start}\n{content}\n{end}", text)


def main() -> None:
    readme = ROOT / "README.md"
    if not readme.exists():
        print(f"找不到 {readme}，请先创建根 README。", file=sys.stderr)
        sys.exit(1)

    problems = find_problems()
    tag_map = build_tag_map(problems)
    write_tag_pages(tag_map)

    text = readme.read_text(encoding="utf-8")
    text = replace_block(text, "PROBLEM_INDEX", render_problem_index(problems))
    text = replace_block(text, "TAG_INDEX", render_tag_index(tag_map))
    readme.write_text(text, encoding="utf-8")

    print(f"已索引 {len(problems)} 道题、{len(tag_map)} 个标签。")
    print("已更新 README.md 和 index/*.md。")


if __name__ == "__main__":
    main()
