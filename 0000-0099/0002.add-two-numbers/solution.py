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
        """根据我第一版想法问的：
        
        def base_solve(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
            # 开始标记
            start_index: int = 0
            # 进位
            carry: int = 0
            cur_node = ListNode()
            while True:
                val_1 = l1.val if l1 else None
                val_2 = l2.val if l2 else None
                if val_1 and val_2:
                    res = val_1 + val_2
                    val = res // 10 if res % 10 else res
                elif val_1:
                    val = val_1
                elif val_2:
                    val = val_2
                else:
                    break
    
                if start_index == 0:
                    cur_node = ListNode(val + carry)
                else:
                    next_node = ListNode(val + carry)
    
                    cur_node.next = next_node
                    cur_node = next_node
    
                if val_1 and val_2:
                    res = val_1 + val_2
                    carry = res % 10 if res % 10 else res
                else:
                    carry = 0
    
                l1 = l1.next if l1 else None
                l2 = l2.next if l2 else None
    
                start_index += 1
    
            return cur_node

        """
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

    def recursive(self, l1: ListNode | None, l2: ListNode | None, carry: int = 0) -> ListNode | None:
        """递归解法"""
        # 递归终止条件：两个链表都空了，且没有进位了
        if not l1 and not l2 and carry == 0:
            return None

        # 统一取值
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        # 计算总和与新的进位
        total = val1 + val2 + carry
        carry = total // 10

        # 当前节点
        node = ListNode(total % 10)

        # 递归构建下一个节点
        node.next = self.recursive(
            l1.next if l1 else None,
            l2.next if l2 else None,
            carry
        )

        return node

    def build_in_solve(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        """python 内置函数解法"""
        dummy = curr = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # divmod 返回 (商, 余数)，对应 (进位, 当前位数字)
            carry, val = divmod(v1 + v2 + carry, 10)

            curr.next = ListNode(val)
            curr = curr.next

            # 极简的指针移动，利用 or 的短路特性
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

    def local_update(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        """原地修改法"""
        head = l1  # 最终返回的头
        prev = None
        carry = 0

        # 只要两个链表没遍历完，或者还有进位
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry
            carry = total // 10
            val = total % 10

            if l1:
                l1.val = val  # 直接修改 l1 的值
                prev = l1
                l1 = l1.next
            else:
                # 如果 l1 短了，把新建的节点挂载到后面
                prev.next = ListNode(val)
                prev = prev.next

            # l2 正常往后走
            if l2:
                l2 = l2.next

        return head


if __name__ == "__main__":
    l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    l2 = ListNode(5, ListNode(6, ListNode(7)))
    res = Solution().deepseek_solve(l1, l2)
    while res:
        print(res.val)
        res = res.next
