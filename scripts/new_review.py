# -*- coding: utf-8 -*-
# @Time    : 2026/10/21 13:25
# @Author  : Zpt
# @Email   : zpta_super@163.com
# @File    : new_review.py.py
# @Project : Algorithm
# @Software: PyCharm
#!/usr/bin/env python3
"""为某道题创建一次复习记录：reviews/YYYY-MM-DD.md"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = ROOT / "templates"
RANGE_DIR_RE = re.compile(r"^\d{4}-\d{4}$")
PROBLEM_DIR_RE = re.compile(r"^(\d{4})\.(.+)$")


def find_problem_dir(number: int) -> Path | None:
    for d in sorted(ROOT.iterdir()):
        if not d.is_dir() or not RANGE_DIR_RE.match(d.name):
            continue
        for sub in sorted(d.iterdir()):
            if not sub.is_dir():
                continue
            m = PROBLEM_DIR_RE.match(sub.name)
            if m and int(m.group(1)) == number:
                return sub
    return None


def read_title(problem_dir: Path) -> str:
    readme = problem_dir / "README.md"
    if readme.exists():
        text = readme.read_text(encoding="utf-8")
        first = text.splitlines()[0] if text else ""
        m = re.match(r"^#\s*\d+\.\s*(.+?)\s*$", first)
        if m:
            return m.group(1)
    return problem_dir.name


def main() -> None:
    parser = argparse.ArgumentParser(description="为某道题创建一次复习记录")
    parser.add_argument("number", type=int, help="题号，如 1")
    parser.add_argument("--date", help="复习日期 YYYY-MM-DD，默认今天")
    args = parser.parse_args()

    problem_dir = find_problem_dir(args.number)
    if problem_dir is None:
        print(
            f"找不到题号 {args.number} 对应的目录。先运行 new_problem.py 创建题目。",
            file=sys.stderr,
        )
        sys.exit(1)

    reviews_dir = problem_dir / "reviews"
    reviews_dir.mkdir(exist_ok=True)

    review_date = args.date or date.today().isoformat()
    existing = sorted(reviews_dir.glob("*.md"))
    review_no = len(existing) + 1

    last_date = ""
    days_since = ""
    if existing:
        dates = sorted(f.stem[:10] for f in existing)
        last_date = dates[-1]
        try:
            delta = datetime.fromisoformat(review_date) - datetime.fromisoformat(last_date)
            days_since = str(delta.days)
        except ValueError:
            pass

    target = reviews_dir / f"{review_date}.md"
    suffix = 2
    while target.exists():
        target = reviews_dir / f"{review_date}-{suffix}.md"
        suffix += 1

    tpl = TEMPLATES / "review-template.md"
    if not tpl.exists():
        print(f"模板缺失：{tpl}", file=sys.stderr)
        sys.exit(1)

    content = tpl.read_text(encoding="utf-8")
    replacements = {
        "{number}": f"{args.number:04d}",
        "{title}": read_title(problem_dir),
        "{date}": review_date,
        "{review_no}": str(review_no),
        "{last_review_date}": last_date or "—",
        "{days_since}": days_since or "—",
    }
    for key, value in replacements.items():
        content = content.replace(key, value)
    target.write_text(content, encoding="utf-8")

    rel = target.relative_to(ROOT)
    print(f"已创建复习记录：{rel}")
    print("填完后运行 python scripts/generate_index.py 更新索引。")


if __name__ == "__main__":
    main()
