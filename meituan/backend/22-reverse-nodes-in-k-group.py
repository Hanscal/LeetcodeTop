# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/7 6:10 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from basic_structure import NodeHandle
from typing import Optional

"""
给你一个链表，每k个节点一组进行翻转，请你返回翻转后的链表。
k是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是k的整数倍，那么请将最后剩余的节点保持原有顺序。

进阶：
你可以设计一个只使用常数额外空间的算法来解决此问题吗？
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cnt = 0
        cur = head
        while cur and cnt != k:
            cnt += 1
            cur = cur.next

        if cnt == k:
            cur = self.reverseKGroup(cur, k)
            # 翻转链表
            while cnt:
                tmp = head.next
                head.next = cur
                # 指针都发生移动
                cur = head
                head = tmp
                cnt -= 1
            head = cur
        return head

if __name__ == '__main__':
    nh = NodeHandle()
    for i in [1,2,3,4,5][::-1]:
        head = nh.add(i)
    s = Solution()
    res = s.reverseKGroup(head, 3)
    res_list = nh.printNode(res)
    assert res_list == [3,2,1,4,5]