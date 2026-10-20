创建一个能长期维护的算法仓库，核心矛盾通常不在“怎么写代码”，而在 **“如何让未来 500 道题之后的你，仍然能快速找到、复习和理解某一道题”** 。下面从目录策略、文件命名、单题元数据、索引自动化四个层面给出建议。

---

## 先做一个关键选择：按题号，还是按主题？

刷题仓库的顶层组织方式，主流有三条路：

**① 按题号范围**（如 `0000-0099/`, `0100-0199/`）
doocs/leetcode 采用的就是这种方式。优点是绝对稳定——力扣题号永不变，文件永远知道该放哪里；缺点是跨题号的同类题在物理目录上是分散的，想集中练“二分查找”需要依赖标签或索引来聚合。

**② 按算法主题**（如 `arrays/`, `dp/`, `graph/`）
NeetCode 路线和 Interview_DS_Algo 这类仓库采用的方式，每个主题下再放题目。优点是学习路径清晰，适合“按类型集中突破”；缺点是同一道题可能涉及多个标签，归类时容易纠结，而且随着题库增长，主题边界会变得模糊。

**③ 按难度**（`easy/`, `medium/`, `hard/`）
对“随便刷几道简单的”这种场景有即时帮助，但对知识沉淀几乎没有长期价值——你未来复习时不会想“我要复习 medium”，而是想“我要复习树形 DP”。

**推荐：以题号为主干，用元数据标签做主题索引。** 物理目录只按题号组织（稳定、无歧义、永不需要移动文件），同时每道题在 README 或元数据文件中打上 `tags`（如 `binary-search`, `two-pointers`），再用一个自动生成的索引脚本按标签聚合。这样既保住了文件位置的确定性，又获得了主题检索能力。


## 目录结构：单题单目录，内部按语言分文件

最推荐的结构是 **每道题一个独立目录，目录内放题解文档和该题所有语言的实现**。这样做的好处是：题目相关的代码、思路、复杂度、踩坑记录都在同一个地方，复习时不需要跨目录跳转。

```
your-algo-repo/
├── README.md                  # 总索引（自动生成）+ 使用说明
├── CONTRIBUTING.md            # 你自己的写作/提交规范（可选但推荐）
├── templates/
│   ├── problem-template.md    # 单题 README 模板
│   └── solution.py            # Python 题解骨架（可选）
├── scripts/
│   ├── new_problem.py         # 根据题号/标题生成新题目目录和文件
│   └── generate_index.py      # 扫描所有题目，重新生成根 README 和标签索引
├── 0000-0099/
│   ├── 0001.two-sum/
│   │   ├── README.md          # 题目信息 + 思路 + 复杂度 + 踩坑
│   │   ├── solution.py
│   │   └── solution.cpp       # 如果也写 C++，就放在同一目录
│   └── 0042.trapping-rain-water/
│       ├── README.md
│       └── solution.py
├── 0100-0199/
└── ...
```

如果你坚持只用 Python，可以省去多语言文件，目录会更轻。但如果未来打算加语言，**单题单目录 + 语言后缀文件名** 比“顶层按语言分目录”更利于知识聚合。后者（如 `python/`, `java/` 各自放所有题）适合做多语言对照的大型公共仓库，但个人刷题仓库中，同一道题的 Python 和 C++ 实现分居两个目录，复习时需要来回跳，并不方便。


## 文件与目录命名规范

推荐两种命名风格，选一种并**全程不破例**：

**风格 A：4 位零填充 + 点号 + slug**（贴近 doocs/leetcode）
```
0001.two-sum/
0042.trapping-rain-water/
```

**风格 B：4 位零填充 + 下划线 + slug**（更偏 Python 社区习惯）
```
0001_two_sum/
0042_trapping_rain_water/
```

slub 一律小写、用连字符或下划线，与力扣 URL 的 slug 保持一致。4 位零填充的意义不只是“好看”——它保证目录在文件管理器中始终按数值顺序排列，不会出现 `10` 排在 `2` 前面的情况。

单题目录内部，多语言文件统一命名：
```
solution.py
solution.cpp
solution.java
```

如果某道题写了多种解法（暴力 / 哈希 / 双指针），**不建议**用 `solution1.py`, `solution2.py`——文件名本身没有信息量。更清晰的做法是放在同一个 `solution.py` 中用不同函数/类区分，并在 README 中说明；或者用带思路后缀的文件名：`solution_hash.py`, `solution_two_pointer.py`。


## 单题 README：你未来复习时真正会读的东西

代码只是“答案”，README 才是“知识”。建议每道题的 README 至少包含以下字段（可以做成模板，生成新题时自动拷入）：

```markdown
# 0001. Two Sum

- **难度**：Easy
- **标签**：array, hash-table
- **链接**：https://leetcode.cn/problems/two-sum/
- **日期**：2026-10-20

## 思路

（用自己的话写，不要复制题解。重点记录“为什么想到这个方法”，而不是“方法是什么”。）

## 复杂度

- 时间：O(n)
- 空间：O(n)

## 踩坑 / 关键点

- 需要返回下标，所以不能用排序+双指针
- 边遍历边建哈希表，避免先完整建表再查找

## 相关题目

- 0015. 三数之和
- 0167. 两数之和 II
```

其中 **“踩坑 / 关键点”是最有价值的部分**。力扣题解已经足够多，你不需要再存一份标准答案；你真正需要的是记录自己当时卡在哪里、为什么选了这个方法、下次遇到类似题应该先想到什么。


## 把“主题索引”做起来，而不是靠翻目录

既然物理目录按题号走，主题聚合就必须靠**索引**。最轻量的做法是：在单题 README 的元数据区维护 `tags`，然后用一个脚本扫描所有题目的 README，自动生成根目录下的 `README.md` 索引表：

| 题号 | 题目 | 难度 | 标签 | 语言 |
|---|---|---|---|---|
| 0001 | Two Sum | Easy | array, hash-table | Python |
| 0042 | Trapping Rain Water | Hard | two-pointers, stack, dp | Python, C++ |

索引脚本还可以按标签生成子索引，比如在根 README 底部附上：

```
## 按标签浏览
- [binary-search](./index/binary-search.md) (12 题)
- [dynamic-programming](./index/dynamic-programming.md) (8 题)
- [two-pointers](./index/two-pointers.md) (15 题)
```

如果不想一开始就写脚本，**从手动维护一个根 README 表格开始也完全可以**。等到题目超过 50 道、觉得手动更新开始烦的时候，再写 `generate_index.py` 也不迟。核心原则是：**索引从第一天就开始积累，哪怕用手写；不要等到几百道题才想起来补。**


## 推荐加一个 `templates/` 目录，降低“开始一道新题”的摩擦

新建题目时最容易敷衍的地方就是 README——因为懒得从头写。放一个模板文件，配合一个轻量生成脚本（Python 即可）：

```
python scripts/new_problem.py 42 "Trapping Rain Water" --difficulty Hard --tags two-pointers,stack,dp
```

脚本自动创建 `0042.trapping-rain-water/`，拷入 `README.md` 模板和 `solution.py` 骨架，预填好题号、标题、链接、日期。摩擦越小，你越可能把每道题的元数据写完整；元数据越完整，索引和复习就越有用。


## 多语言怎么办：不要过早按语言分顶层目录

如果你现在主要用 Python，偶尔写 C++ 练手，**不要**为了“以后可能有很多语言”而把顶层做成 `python/` 和 `cpp/`。过早按语言拆分会让同一道题的思路文档和代码分离，破坏“单题单目录”的知识聚合优势。等到某天你确实开始系统性地用 3 种以上语言写同一批题，再考虑迁移——而且迁移也只是一个脚本按扩展名重新分目录的事，成本远低于长期在割裂的目录间跳转。


## 最终推荐的最小可行结构

```
algo-practice/
├── README.md                     # 自动/手动维护的总索引 + 学习路线
├── templates/
│   ├── problem-template.md
│   └── solution.py
├── scripts/
│   ├── new_problem.py
│   └── generate_index.py
├── 0000-0099/
│   ├── 0001.two-sum/
│   │   ├── README.md
│   │   └── solution.py
│   └── ...
├── 0100-0199/
└── index/
    ├── binary-search.md          # 按标签聚合的索引（由脚本生成）
    └── dynamic-programming.md
```

这套结构的核心取舍是：**物理存储用题号保稳定，知识检索用标签索引保灵活，单题目录用 README 保理解，生成脚本把“维护索引”的重复劳动自动化。** 先按这个骨架开始，前 20 道题手动维护索引也不会太累；等你感觉到瓶颈时，自动化已经水到渠成了。


---

下面把整套骨架直接给你，复制粘贴即可用。文件清单：

```
algo-practice/
├── README.md
├── CONTRIBUTING.md
├── .gitignore
├── templates/
│   ├── problem-template.md
│   └── solution.py
├── scripts/
│   ├── new_problem.py
│   └── generate_index.py
└── index/                  # 先建空目录，脚本会往里写
```

---

## `README.md`

````markdown
# 算法练习

个人力扣刷题仓库。每道题一个目录，目录内包含题解说明和该题所有语言的实现。

## 快速开始

新建一道题：

```bash
python scripts/new_problem.py 1 "Two Sum" --difficulty Easy --tags array,hash-table
```

更新索引：

```bash
python scripts/generate_index.py
```

## 目录约定

```
0000-0099/            # 按题号分段
  0001.two-sum/
    README.md         # 题目信息、思路、复杂度、踩坑
    solution.py       # Python 实现
index/                # 按标签聚合的索引（脚本生成，勿手改）
scripts/              # 辅助脚本
templates/            # 新建题目时使用的模板
```

## 题目索引

<!-- PROBLEM_INDEX_START -->
<!-- PROBLEM_INDEX_END -->

## 按标签浏览

<!-- TAG_INDEX_START -->
<!-- TAG_INDEX_END -->
````

---

## `.gitignore`

```
__pycache__/
*.py[cod]
.venv/
venv/
.idea/
.vscode/
.DS_Store
```

---

## `CONTRIBUTING.md`

````markdown
# 写作规范

## 目录与命名

- 每题一个目录：`NNNN.slug`，NNNN 为 4 位题号，slug 为小写英文、连字符分隔。
- 题目放在对应的题号范围目录下，如 `0000-0099/0001.two-sum/`。
- 多语言实现放在同一目录，文件名统一为 `solution.<ext>`。
- 同一题有多种思路时，优先在一个 `solution.py` 中用不同函数/类区分，并在 README 中说明；确需拆分时用 `solution_hash.py` 这类带思路后缀的文件名。

## README 必填字段

每道题的 `README.md` 必须包含以下元数据行，供索引脚本解析：

```markdown
- **难度**：Easy
- **标签**：array, hash-table
- **链接**：https://leetcode.cn/problems/two-sum/
- **日期**：2026-10-20
```

- 难度取值：Easy / Medium / Hard。
- 标签用逗号分隔，尽量复用已有标签，避免同义标签（如 `dp` 和 `dynamic-programming` 二选一）。
- 日期为首次完成或最近复习日期，格式 `YYYY-MM-DD`。

## 内容要求

- “思路”用自己的话写，重点记录“为什么想到这个方法”。
- “复杂度”写清时间和空间。
- “踩坑 / 关键点”记录自己卡住的地方，这是最值得复习的部分。
- 不要整段复制题解。

## 提交前

运行 `python scripts/generate_index.py`，确保索引已更新。
````

---

## `templates/problem-template.md`

````markdown
# {number}. {title}

- **难度**：{difficulty}
- **标签**：{tags}
- **链接**：{url}
- **日期**：{date}

## 思路

（用自己的话写：为什么想到这个方法，而不是方法本身。）

## 复杂度

- 时间：O(?)
- 空间：O(?)

## 踩坑 / 关键点

- 

## 相关题目

- 
````

---

## `templates/solution.py`

```python
"""
{number}. {title}

{url}
"""

from __future__ import annotations


class Solution:
    def solve(self) -> None:
        raise NotImplementedError


if __name__ == "__main__":
    Solution().solve()
```

---

## `scripts/new_problem.py`

```python
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
    print("  3. 运行 python scripts/generate_index.py 更新索引")


if __name__ == "__main__":
    main()
```

---

## `scripts/generate_index.py`

```python
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

    return {
        "number": number,
        "slug": slug,
        "title": title,
        "difficulty": difficulty,
        "tags": tags,
        "langs": langs,
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


def render_problem_index(problems: list[dict]) -> str:
    if not problems:
        return "_还没有题目。运行 `python scripts/new_problem.py ...` 创建第一道题。_"
    lines = [
        "| 题号 | 题目 | 难度 | 标签 | 语言 |",
        "| --- | --- | --- | --- | --- |",
    ]
    for p in problems:
        num = f"{p['number']:04d}"
        link = f"[{num}](./{p['rel'].as_posix()}/)"
        tags = ", ".join(p["tags"]) if p["tags"] else "-"
        langs = ", ".join(p["langs"]) if p["langs"] else "-"
        diff = p["difficulty"] or "-"
        lines.append(f"| {link} | {p['title']} | {diff} | {tags} | {langs} |")
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
            "| 题号 | 题目 | 难度 | 语言 |",
            "| --- | --- | --- | --- |",
        ]
        for p in entry["problems"]:
            num = f"{p['number']:04d}"
            link = f"[{num}](../{p['rel'].as_posix()}/)"
            langs = ", ".join(p["langs"]) if p["langs"] else "-"
            diff = p["difficulty"] or "-"
            lines.append(f"| {link} | {p['title']} | {diff} | {langs} |")
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
```

---

## 初始化与验证

创建完上述文件后，在仓库根目录执行：

```bash
mkdir -p index
git init
python scripts/generate_index.py
```

第一次运行应该输出 `已索引 0 道题、0 个标签。`，根 README 的索引区域会变成“还没有题目”的提示。

然后创建第一道题验证：

```bash
python scripts/new_problem.py 1 "Two Sum" --difficulty Easy --tags array,hash-table
python scripts/generate_index.py
```

应该看到 `0000-0099/0001.two-sum/` 被创建，根 README 出现索引表格，`index/array.md` 和 `index/hash-table.md` 也被生成。

之后每道题的固定流程就是三步：

1. `python scripts/new_problem.py <题号> "<英文标题>" --difficulty <难度> --tags <标签>`
2. 填 `README.md` 的思路/复杂度/踩坑，写 `solution.py`
3. `python scripts/generate_index.py`，提交

如果标题是中文，记得加 `--slug`，比如：

```bash
python scripts/new_problem.py 42 "接雨水" --slug trapping-rain-water --difficulty Hard --tags two-pointers,stack,dp
```