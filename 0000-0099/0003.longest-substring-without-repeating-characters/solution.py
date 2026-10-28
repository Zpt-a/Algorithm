# -*- coding: utf-8 -*-
# @Time    : 2026/10/20 11:06
# @Author  : Zpt
# @Email   : zpta_super@163.com
# @File    : solution.py
# @Project : Algorithm
# @Software: PyCharm
"""
0003. Longest Substring Without Repeating Characters

https://leetcode.cn/problems/longest-substring-without-repeating-characters/
"""

from __future__ import annotations


class Solution:
    def solve(self, s: str) -> int:
        """"""
        # 总
        hash_dict: dict = {}
        # 子串最长长度
        length: int = 0
        # 每个子串长度计数
        cur_length: int = 0
        # 左指针
        left_ind: int = 0
        # 右指针
        right_ind: int = 0

        while left_ind < len(s) or right_ind < len(s):

            if left_ind == len(s):
                # 左指针到达最大值（按理不存在）
                break
            elif right_ind == len(s):
                # 右指针到达最大值，左指针未到达，这种情况不会在有新的最长 子串 的情况
                length = max(length, cur_length)
                break
            else:
                if left_ind == right_ind:
                    right_ind += 1
                    cur_length = 1
                    hash_dict = {}
                    hash_dict[s[left_ind]] = left_ind
                else:
                    # 主逻辑（全在 left < right）
                    if s[right_ind] in hash_dict:
                        length = max(length, cur_length)
                        hash_dict.pop(s[left_ind])
                        cur_length -= 1
                        left_ind += 1
                    else:
                        hash_dict[s[right_ind]] = right_ind
                        cur_length += 1
                        right_ind += 1

        return length

    def better_way(self, s: str) -> int:
        """deepseek 进阶"""
        # 哈希表记录：字符 -> 该字符最近一次出现的索引 + 1
        # 例如 { 'a': 1 } 表示 'a' 上一次出现在索引 0，左边界至少要移动到 1
        last_pos: dict = {}

        max_length = 0
        left = 0

        # 经典套路：右指针用 for 循环无脑往前冲
        for right, char in enumerate(s):
            # 如果当前字符之前出现过，并且它的位置在当前窗口内
            if char in last_pos:
                # 左指针直接跳跃到该字符上次出现位置的右边
                # 使用 max 是为了防止 left 往回退（针对 "abba" 这种情况）
                left = max(left, last_pos[char])

            # 更新字符的最后位置（注意 +1，方便 left 直接赋值）
            last_pos[char] = right + 1

            # 更新最大长度（当前窗口长度 = right - left + 1）
            max_length = max(max_length, right - left + 1)

        return max_length


if __name__ == "__main__":
    s_len = Solution().solve("s")
    print(s_len)
