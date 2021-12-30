# -*- coding: utf-8 -*-

"""
@Time    : 2021/12/30 10:09 上午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
"""Given the head of a singly linked list and two integers left and right where left <= right, 
reverse the nodes of the list from position left to position right, and return the reversed list.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # 设置 dummyNode 是这一类问题的一般做法
        dummy_node = ListNode(-1)
        dummy_node.next = head
        pre = dummy_node
        for _ in range(left - 1):
            pre = pre.next

        cur = pre.next
        for _ in range(right - left):
            next = cur.next
            cur.next = next.next
            next.next = pre.next
            pre.next = next
        return dummy_node.next


if __name__ == '__main__':
    s =Solution()
