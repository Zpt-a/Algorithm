# -*- coding: utf-8 -*-
# @Time    : 2026/10/20 11:07
# @Author  : Zpt
# @Email   : zpta_super@163.com
# @File    : new_problem.py
# @Project : Algorithm
# @Software: PyCharm
#!/usr/bin/env python3
"""新建一道算法题：生成题号目录、README 和 Python 题解骨架。"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = ROOT / "templates"


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def range_dir(number: int) -> str:
    start = (number // 100) * 100
    return f"{start:04d}-{start + 99:04d}"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="新建一道算法题（生成目录、README、题解骨架）",
    )
    parser.add_argument("number", type=int, help="力扣题号，如 1")
    parser.add_argument("title", help="题目标题，如 'Two Sum'")
    parser.add_argument("--slug", help="目录 slug，默认由英文标题生成")
    parser.add_argument(
        "--difficulty",
        default="Medium",
        help="难度：Easy / Medium / Hard，默认 Medium",
    )
    parser.add_argument(
        "--tags",
        default="",
        help="标签，逗号分隔，如 'array,hash-table'",
    )
    parser.add_argument("--url", help="题目链接，默认按 slug 生成力扣链接")
    args = parser.parse_args()

    slug = args.slug or slugify(args.title)
    if not slug:
        print(
            "无法从标题生成 slug（标题可能含中文）。请用 --slug 指定英文 slug。",
            file=sys.stderr,
        )
        sys.exit(1)

    parent = ROOT / range_dir(args.number)
    parent.mkdir(parents=True, exist_ok=True)
    problem_dir = parent / f"{args.number:04d}.{slug}"

    if problem_dir.exists():
        print(f"目录已存在，未做任何修改：{problem_dir}", file=sys.stderr)
        sys.exit(1)

    problem_dir.mkdir()

    replacements = {
        "{number}": f"{args.number:04d}",
        "{title}": args.title,
        "{difficulty}": args.difficulty,
        "{tags}": args.tags,
        "{url}": args.url or f"https://leetcode.cn/problems/{slug}/",
        "{date}": date.today().isoformat(),
    }

    pairs = [
        ("problem-template.md", "README.md"),
        ("solution.py", "solution.py"),
    ]
    for tpl_name, out_name in pairs:
        tpl = TEMPLATES / tpl_name
        if not tpl.exists():
            print(f"模板缺失：{tpl}", file=sys.stderr)
            sys.exit(1)
        content = tpl.read_text(encoding="utf-8")
        for key, value in replacements.items():
            content = content.replace(key, value)
        (problem_dir / out_name).write_text(content, encoding="utf-8")

    rel = problem_dir.relative_to(ROOT)
    print(f"已创建：{rel}")
    print("下一步：")
    print(f"  1. 编辑 {rel}/README.md")
    print(f"  2. 编辑 {rel}/solution.py")
    print(f"  3. 运行 python scripts/generate_index.py 更新索引")
    print(f"  4. 复习时运行 python scripts/new_review.py {args.number}")


if __name__ == "__main__":
    main()
