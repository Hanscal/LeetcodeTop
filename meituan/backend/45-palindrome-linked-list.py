# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/20 1:07 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from basic_structure import NodeHandle

"""给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 双指针
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]


if __name__ == '__main__':
    nh = NodeHandle()
    for i in [1,2,2,1][::-1]:
        head = nh.add(i)
    s = Solution()
    res = s.isPalindrome(head)
    print(res)
    assert res == True