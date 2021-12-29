# -*- coding: utf-8 -*-

"""
@Time    : 2021/12/27 7:38 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from typing import List
import random

"""
给你一个整数数组 nums，请你将该数组升序排列。
"""
from basic_structure import NodeHandle

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev

if __name__ == '__main__':
    nh = NodeHandle()
    for i in [5,2,3,1][::-1]:
        head = nh.add(i)

    s = Solution()
    res = s.reverseList(head)
    res = nh.printNode(res)
    assert res == [1,3,2,5]
