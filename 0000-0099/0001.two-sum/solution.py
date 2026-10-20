# -*- coding: utf-8 -*-
# @Time    : 2026/10/20 11:06
# @Author  : Zpt
# @Email   : zpta_super@163.com
# @File    : solution.py
# @Project : Algorithm
# @Software: PyCharm
"""
0001. Two Sum

https://leetcode.cn/problems/two-sum/
"""

from __future__ import annotations

from typing import List


class Solution:
    def solve(self) -> None:
        raise NotImplementedError

    def sorted_list_two_num(self, nums: list[int], target: int) -> list[int]:
        """有序列表的两数之和：双指针"""
        start_index: int = 0
        end_index: int = len(nums) - 1
        while start_index < end_index:
            if nums[start_index] + nums[end_index] == target:
                break
            elif nums[start_index] + nums[end_index] > target:
                end_index -= 1
            elif nums[start_index] + nums[end_index] < target:
                start_index += 1
            else:
                raise ValueError("未找到目标值！")
        return [start_index, end_index]

    @staticmethod
    def unsort_list_two_num(nums: list[int], target: int) -> list[int]:
        """无序列表的暴力破解"""
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    @staticmethod
    def the_optimal(nums: list[int], target: int) -> List[int]:
        """最优解"""
        hash_map: dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash_map:
                return [i, hash_map[complement]]
            hash_map[num] = i

        return []


if __name__ == "__main__":
    Solution().solve()
