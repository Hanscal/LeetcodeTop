# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/17 1:03 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from basic_structure import NodeHandle

"""
给你两个非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0开头。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 从后往前加，题目中已经是逆序了
        pre = ListNode(0)
        cur = pre
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum = x + y + carry

            carry = sum // 10
            sum = sum % 10
            cur.next = ListNode(sum)

            cur = cur.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry == 1:
            cur.next = ListNode(carry)
        return pre.next

if __name__ == '__main__':
    nh1 = NodeHandle()
    for i in [2,3,4][::-1]:
        l1 = nh1.add(i)
    nh2 = NodeHandle()
    for i in [5,6,4][::-1]:
        l2 = nh2.add(i)
    s = Solution()
    res = s.addTwoNumbers(l1, l2)
    res_list = nh2.printNode(res)
    print(res_list)
    assert res_list == [7,9,8]