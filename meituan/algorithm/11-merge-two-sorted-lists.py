# -*- coding: utf-8 -*-

"""
@Time    : 2021/12/13 11:59 上午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""

"""将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。"""
from typing import Optional

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
    s = Solution()
    list1 = ListNode(4)
    for a in [2,1]:
        list1 = ListNode(a, list1)
    list2 = ListNode(4)
    for a in [3,1]:
        list2 = ListNode(a, list2)
    res = s.mergeTwoLists(list1, list2)
    res_out = []
    while res:
        res_out.append(res.val)
        res = res.next
    print(res_out)
    assert res_out == [1,1,2,3,4,4]