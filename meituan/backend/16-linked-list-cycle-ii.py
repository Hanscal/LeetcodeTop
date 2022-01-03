# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/3 11:04 上午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""

from basic_structure import NodeHandle

"""
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
"""
# 双指针，一个快，一个慢
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head):
        fast, slow = head, head
        while True:
            if not (fast and fast.next): return None  # 如果没有环存在，则return None
            fast, slow = fast.next.next, slow.next
            if fast == slow: break # 有环存在，在相遇处跳出循环
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast

if __name__ == '__main__':
    nh = NodeHandle()
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(-4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    # n4.next = n2
    s = Solution()
    res = s.detectCycle(n1)
    print(res)
    assert res == None

