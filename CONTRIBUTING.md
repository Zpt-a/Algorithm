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