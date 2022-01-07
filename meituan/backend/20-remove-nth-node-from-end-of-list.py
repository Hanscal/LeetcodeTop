# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/5 5:38 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from basic_structure import NodeHandle

"""给你一个链表，删除链表的倒数第n个结点，并且返回链表的头结点。"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 双指针
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        first = head
        second = dummy
        for i in range(n):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next

if __name__ == '__main__':
    nh = NodeHandle()
    for i in [1,2,3,4,5][::-1]:
        head = nh.add(i)
    s = Solution()
    res = s.removeNthFromEnd(head, 2)
    res_list = nh.printNode(res)
    assert res_list == [1,2,3,5]

