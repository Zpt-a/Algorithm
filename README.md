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
| 题号 | 题目 | 难度 | 标签 | 语言 |
| --- | --- | --- | --- | --- |
| [0001](./0000-0099/0001.two-sum/) | Two Sum | Easy | array, hash-table | Python |
| [0002](./0000-0099/0002.add-two-numbers/) | add Two Numbers | Medium | recursive, linked-list, math | Python |
<!-- PROBLEM_INDEX_END -->

## 按标签浏览

<!-- TAG_INDEX_START -->
- [array](./index/array.md)（1 题）
- [hash-table](./index/hash-table.md)（1 题）
- [linked-list](./index/linked-list.md)（1 题）
- [math](./index/math.md)（1 题）
- [recursive](./index/recursive.md)（1 题）
<!-- TAG_INDEX_END -->
