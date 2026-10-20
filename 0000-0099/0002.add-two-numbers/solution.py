# -*- coding: utf-8 -*-
# @Time    : 2026/10/20 11:06
# @Author  : Zpt
# @Email   : zpta_super@163.com
# @File    : solution.py
# @Project : Algorithm
# @Software: PyCharm
"""
0002. add Two Numbers

https://leetcode.cn/problems/add-two-numbers/
"""

from __future__ import annotations


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


class Solution:
    def solve(self) -> None:
        raise NotImplementedError

    def base_solve(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        """基础解决方法"""
        # 进位
        carry: int = 0
        dummy = ListNode(0)
        cur_node = dummy

        while l1 or l2 or carry:
            val_1 = l1.val if l1 else 0
            val_2 = l2.val if l2 else 0

            val_sum = val_1 + val_2 + carry

            cur_node.next = ListNode(val_sum % 10)

            cur_node = cur_node.next

            carry = val_sum // 10

            # l1 和 l2 也要往后走（注意判空）
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return cur_node.next

    def deepseek_solve(self, l1: ListNode | None, l2: ListNode | None) -> ListNode:
        """"""
        # 1. 创建哑节点和游标
        dummy = ListNode(0)
        curr = dummy

        # 2. 进位变量
        carry = 0

        # 3. 只要 l1 还有、l2 还有、或者进位还有，就继续算
        while l1 or l2 or carry:
            # 统一取值，没有节点就当作 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # 计算总和（把进位加进来）
            total = val1 + val2 + carry

            # 算出新的进位（比如 15 // 10 = 1）
            carry = total // 10

            # 当前位应该存的数字（比如 15 % 10 = 5）
            curr.next = ListNode(total % 10)

            # 游标往后走一位，准备接下一个节点
            curr = curr.next

            # l1 和 l2 也要往后走（注意判空）
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        # 返回哑节点的下一个节点，也就是真正的头节点
        return dummy.next


if __name__ == "__main__":
    l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    l2 = ListNode(5, ListNode(6, ListNode(7)))
    res = Solution().deepseek_solve(l1, l2)
    while res:
        print(res.val)
        res = res.next
