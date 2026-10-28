# 算法练习

个人力扣刷题仓库。每道题一个目录，目录内包含题解说明和该题所有语言的实现。

## 快速开始

新建一道题：

```bash
python scripts/new_problem.py 1 "Two Sum" --difficulty Easy --tags array,hash-table
```

开始一次复习：

```bash
python scripts/new_review.py 1
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
    reviews/          # 复习记录，每次一个 YYYY-MM-DD.md
      2026-10-21.md
index/                # 按标签聚合的索引（脚本生成，勿手改）
scripts/              # 辅助脚本
templates/            # 新建题目/复习时使用的模板
```

## 复习流程

1. `python scripts/new_review.py <题号>` 生成当天的复习记录。
2. 不翻原解法，先在“重写思路”里写思路，再在“代码”里重新实现。
3. 写完对照 `solution.py`，填“与上次解法对比”“本次卡点”“下次复习重点”。
4. 运行 `python scripts/generate_index.py`，索引表会显示复习次数和最近复习日期。

## 题目索引

<!-- PROBLEM_INDEX_START -->
| 题号 | 题目 | 难度 | 标签 | 语言 | 复习 |
| --- | --- | --- | --- | --- | --- |
| [0001](./0000-0099/0001.two-sum/) | Two Sum | Easy | array, hash-table | Python | 1 次（最近 2026-10-21） |
| [0002](./0000-0099/0002.add-two-numbers/) | add Two Numbers | Medium | recursive, linked-list, math | Python | - |
| [0003](./0000-0099/0003.longest-substring-without-repeating-characters/) | Longest Substring Without Repeating Characters | Medium | hash-table, string, sliding-window | Python | - |
| [0004](./0000-0099/0004.median-of-two-sorted-arrays/) | Median Of Two Sorted Arrays | Hard | array, binary-search, divide-and-conquer | Python | - |
<!-- PROBLEM_INDEX_END -->

## 按标签浏览

<!-- TAG_INDEX_START -->
- [array](./index/array.md)（2 题）
- [binary-search](./index/binary-search.md)（1 题）
- [divide-and-conquer](./index/divide-and-conquer.md)（1 题）
- [hash-table](./index/hash-table.md)（2 题）
- [linked-list](./index/linked-list.md)（1 题）
- [math](./index/math.md)（1 题）
- [recursive](./index/recursive.md)（1 题）
- [sliding-window](./index/sliding-window.md)（1 题）
- [string](./index/string.md)（1 题）
<!-- TAG_INDEX_END -->
