# -*- coding: utf-8 -*-
# @Time    : 2026/10/20 11:06
# @Author  : Zpt
# @Email   : zpta_super@163.com
# @File    : solution.py
# @Project : Algorithm
# @Software: PyCharm
"""
0004. Median Of Two Sorted Arrays

https://leetcode.cn/problems/median-of-two-sorted-arrays/
"""

from __future__ import annotations


class Solution:
    def solve(self, nums1: list[int], nums2: list[int]) -> float:
        length = len(nums1) + len(nums2)

        if length % 2 == 0:
            # 能整除，说明是偶数序列组合，那么中位数必定是两数相除
            mid_right = length // 2
            mid_left = mid_right - 1
        else:
            # 不能整除，说明是奇数序列组合，组合序列长度除以2必定是中位数在序列的下表
            mid_left = mid_right = length // 2

        print(mid_left, mid_right)

        # 当前指针
        cur_ind: int = 0
        # 标志位，决定哪个序列是否走完: 0：都在，1：num1 没了，2：num2 么了，3：都没了
        end_flag = 0
        if nums1 and nums2:
            ind_1: int = 0
            ind_2: int = 0
        elif nums1:
            ind_1 = 0
            end_flag = 2
        elif nums2:
            ind_2 = 0
            end_flag = 1
        else:
            end_flag = 3

        if nums1 and nums2:
            while cur_ind <= mid_left:

                if end_flag == 0:
                    max_val = max(nums1[ind_1], nums2[ind_2])
                    if cur_ind == mid_left:
                        if mid_left == mid_right:
                            return nums2[ind_2] if max_val == nums1[ind_1] else nums1[ind_1]
                        else:
                            left_val = nums2[ind_2] if max_val == nums1[ind_1] else nums1[ind_1]
                            if max_val == nums1[ind_1]:
                                # num1 序列大，那么序列2的下标往前移，存了 序列2 的一个值
                                if ind_2 < len(nums2) - 1:
                                    right_val = min(nums2[ind_2 + 1], max_val)
                                else:
                                    right_val = max_val
                            else:
                                # num2 序列大，那么序列1的下标往前移，存了 序列1 的一个值
                                if ind_1 < len(nums1) - 1:
                                    right_val = min(nums1[ind_1 + 1], max_val)
                                else:
                                    right_val = max_val
                            return (left_val + right_val) / 2

                    # max_val = max(nums1[ind_1], nums2[ind_2])

                    if max_val == nums1[ind_1]:
                        # num1 序列大，那么序列2的下标往前移，存了 序列2 的一个值
                        if ind_2 < len(nums2) - 1:
                            ind_2 += 1
                        else:
                            end_flag = 2 if end_flag == 0 else 3
                    else:
                        # num2 序列大，那么序列1的下标往前移，存了 序列1 的一个值
                        if ind_1 < len(nums1) - 1:
                            ind_1 += 1
                        else:
                            end_flag = 1 if end_flag == 0 else 3
                    cur_ind += 1
                elif end_flag == 1:
                    if cur_ind == mid_left:
                        if mid_left == mid_right:
                            return nums2[ind_2]
                        else:
                            if nums1 and len(nums2) > 1:
                                if nums1[-1] <= nums2[ind_2 - 1]:
                                    return (nums2[ind_2 - 1] + nums2[ind_2]) / 2
                                else:
                                    return (nums1[-1] + nums2[ind_2]) / 2
                            elif nums1 and len(nums2) == 1:
                                return nums2[ind_2]
                            else:
                                return None

                    if ind_2 < len(nums2) - 1:
                        ind_2 += 1
                    else:
                        end_flag = 3
                    cur_ind += 1
                elif end_flag == 2:
                    if cur_ind == mid_left:
                        if mid_left == mid_right:
                            return nums1[ind_1]
                        else:
                            if nums2 and len(nums1) > 1:
                                if nums2[-1] <= nums1[ind_1 - 1]:
                                    return (nums1[ind_1 - 1] + nums1[ind_1]) / 2
                                else:
                                    return (nums2[-1] + nums1[ind_1]) / 2
                            elif nums2 and len(nums1) == 1:
                                return nums1[ind_1]
                            else:
                                return None

                    if ind_1 < len(nums1) - 1:
                        ind_1 += 1
                    else:
                        end_flag = 3
                    cur_ind += 1
                else:
                    break
        elif nums1:
            return (nums1[mid_left] + nums1[mid_right]) / 2
        elif nums2:
            return (nums2[mid_left] + nums2[mid_right]) / 2
        else:
            return None

        return None

    def new_solve(self, nums1: list[int], nums2: list[int]) -> float:
        """整理双指针"""
        length = len(nums1) + len(nums2)
        if length % 2 == 0:
            # 能整除，说明是偶数序列组合，那么中位数必定是两数相除
            mid_right = length // 2
            mid_left = mid_right - 1
        else:
            # 不能整除，说明是奇数序列组合，组合序列长度除以2必定是中位数在序列的下表
            mid_left = mid_right = length // 2

        print(mid_left, mid_right)

        if nums1 and nums2:
            # 当前两列表排序值下表
            cur_ind: int = 0
            # num1 指针
            left_ind: int = 0
            # num2 指针
            right_ind: int = 0
            # 标志位，决定哪个序列是否走完: 0：都在，1：num1 没了，2：num2 没了，3：都没了
            end_flag = 0
            # 上一个元素属于哪个序列：0：没开始，1：序列一，2：序列二
            last_ind_flag = 0

            if end_flag == 0:
                cur_val = min(nums1[left_ind], nums2[right_ind])

                if cur_ind == mid_left:
                    if mid_left == mid_right:
                        return cur_val
                    else:
                        left_val = cur_val
                        if cur_val == nums1[left_ind]:
                            if left_ind < len(nums1) - 1:
                                left_ind += 1
                                right_val = min(nums1[left_ind], nums2[right_ind])
                            else:
                                right_val = nums2[right_ind]
                        else:
                            if right_ind < len(nums2) - 1:
                                right_ind += 1
                                right_val = min(nums1[left_ind], nums2[right_ind])
                            else:
                                right_val = nums1[left_ind]
                        return (left_val + right_val) / 2

                if cur_val == nums1[left_ind]:
                    last_ind_flag = 1
                    if left_ind < len(nums1) - 1:
                        left_ind += 1
                    else:
                        end_flag = 1
                else:
                    last_ind_flag = 2
                    if right_ind < len(nums2) - 1:
                        right_ind += 1
                    else:
                        end_flag = 2

                cur_ind += 1
            elif end_flag == 1:
                if last_ind_flag == 1:
                    cur_val = nums2[right_ind]
                    if cur_ind == mid_left:
                        pass
                elif last_ind_flag == 2:
                    pass
                else:
                    pass
            elif end_flag == 2:
                pass
            else:
                return None
        elif nums1:
            return (nums1[mid_left] + nums1[mid_right]) / 2
        elif nums2:
            return (nums2[mid_left] + nums2[mid_right]) / 2
        else:
            return None

    def build_in_solve(self, nums1: list[int], nums2: list[int]) -> float:
        length = len(nums1) + len(nums2)

        new_num = sorted(nums1 + nums2)

        if length % 2 == 0:
            # 能整除，说明是偶数序列组合，那么中位数必定是两数相除
            mid_right = length // 2
            mid_left = mid_right - 1
            return (new_num[mid_left] + new_num[mid_right]) / 2
        else:
            # 不能整除，说明是奇数序列组合，组合序列长度除以2必定是中位数在序列的下表
            mid_left = mid_right = length // 2
            return (new_num[mid_left] + new_num[mid_right]) / 2

    def deepseek_solve(self, nums1: list[int], nums2: list[int]) -> float:
        """deepseek 双指针"""
        m, n = len(nums1), len(nums2)
        total_len = m + n

        # 我们只需要遍历到 (total_len // 2) 这个位置就可以停了
        # 因为对于偶数长度，中位数由倒数第二个和最后一个数决定
        target_idx = total_len // 2

        i, j = 0, 0
        curr, prev = 0, 0  # 记录当前数字和前一个数字

        for _ in range(target_idx + 1):
            prev = curr  # 每次循环前，把当前的变成前一个

            # 核心逻辑：如果 nums1 没走完，且（nums2 走完了 或者 nums1 当前数更小）
            if i < m and (j >= n or nums1[i] <= nums2[j]):
                curr = nums1[i]
                i += 1
            else:
                curr = nums2[j]
                j += 1

        # 如果是奇数，直接返回最后一个遍历到的数
        if total_len % 2 != 0:
            return float(curr)
        # 如果是偶数，返回前一个数和当前数的平均值
        else:
            return (curr + prev) / 2.0

    def divide_and_conquer(self, nums1: list[int], nums2: list[int]) -> float:
        """二分法"""
        m, n = len(nums1), len(nums2)

        total_len = m + n

        target_idx = total_len // 2

        if m == 0:
            if total_len % 2 != 0:
                return float(nums2[target_idx])
            # 如果是偶数，返回前一个数和当前数的平均值
            else:
                return (nums2[target_idx - 1] + nums2[target_idx]) / 2.0
        elif n == 0:
            if total_len % 2 != 0:
                return float(nums1[target_idx])
            # 如果是偶数，返回前一个数和当前数的平均值
            else:
                return (nums1[target_idx - 1] + nums1[target_idx]) / 2.0
        else:
            m_mid = m // 2
            n_mid = n // 2
            if nums1[m_mid] > nums2[n_mid] and nums1[m_mid] < nums2[-1]:
                #
                pass

    def deepseek_divide_and_conquer(self, nums1: list[int], nums2: list[int]) -> float:
        """deepseek 二分法实现"""

        m, n = len(nums1), len(nums2)
        total_len = m + n

        # 封装一个辅助函数，用来找第 k 小的数 (k 从 1 开始)
        def find_kth(k: int) -> int:
            # 内部维护两个指针，指向当前数组的起始位置
            idx1, idx2 = 0, 0

            while True:
                # 边界情况 1：如果 nums1 已经空了，直接返回 nums2 的第 k 个
                if idx1 == m:
                    return nums2[idx2 + k - 1]
                # 边界情况 2：如果 nums2 已经空了，直接返回 nums1 的第 k 个
                if idx2 == n:
                    return nums1[idx1 + k - 1]
                # 边界情况 3：如果 k 变成了 1，直接比较当前两个指针指向的值
                if k == 1:
                    return min(nums1[idx1], nums2[idx2])

                # 正常情况：取 k 的一半进行二分排除
                half_k = k // 2

                # 获取两个数组当前要比较的索引位置（注意不要越界）
                new_idx1 = min(idx1 + half_k, m) - 1
                new_idx2 = min(idx2 + half_k, n) - 1

                # 比较两个位置的值
                if nums1[new_idx1] <= nums2[new_idx2]:
                    # nums1 这一半被淘汰了
                    # k 需要减去实际被淘汰的长度
                    k -= (new_idx1 - idx1 + 1)
                    idx1 = new_idx1 + 1
                else:
                    # nums2 这一半被淘汰了
                    k -= (new_idx2 - idx2 + 1)
                    idx2 = new_idx2 + 1

        # 主逻辑计算中位数
        if total_len % 2 == 1:
            # 奇数，直接找第 total_len // 2 + 1 小
            return float(find_kth(total_len // 2 + 1))
        else:
            # 偶数，找中间两个数，求平均
            left = find_kth(total_len // 2)
            right = find_kth(total_len // 2 + 1)
            return (left + right) / 2.0


if __name__ == "__main__":
    # res = Solution().solve([1, 3], [2])
    # res = Solution().solve([1, 2], [3, 4])
    # res = Solution().solve([1], [1])
    # res = Solution().solve([], [2, 3])
    # res = Solution().solve([1, 2], [-1, 3])
    # res = Solution().solve([1], [2, 3, 4])
    res = Solution().solve([1,2,3,4,5], [6,7,8,9,10,11,12,13,14,15,16,17])
    print(res)
