# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/7 6:02 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from basic_structure import NodeHandle
from typing import Optional

"""将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 """

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode(-1) # 双指针初始化+建立伪头
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next  # 更新 cur往前进一步
        cur.next = list1 if list1 else list2
        return dummy.next

if __name__ == '__main__':
    nh1 = NodeHandle()
    for i in [1,2,4][::-1]:
        l1 = nh1.add(i)
    nh2 = NodeHandle()
    for i in [1,3,4][::-1]:
        l2 = nh2.add(i)
    s = Solution()
    res = s.mergeTwoLists(l1, l2)
    res_list = nh1.printNode(res)
    assert res_list == [1,1,2,3,4,4]