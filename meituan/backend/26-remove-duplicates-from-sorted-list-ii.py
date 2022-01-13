# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/9 5:31 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
"""
存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除链表中所有存在数字重复情况的节点，只保留原始链表中没有重复出现的数字。

返回同样按升序排列的结果链表。
"""
from basic_structure import NodeHandle

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 升序，双指针
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = slow = ListNode()
        dummy.next = head
        fast = head
        while fast:
            while fast.next and fast.val == fast.next.val:
                fast = fast.next
            # 没有重复节点
            if slow.next == fast:
                slow = slow.next
            else:
                slow.next = fast.next
            fast = fast.next
        return dummy.next

if __name__ == '__main__':
    nh = NodeHandle()
    for i in [1,2,3,4,4,5,5,6][::-1]:
        head = nh.add(i)
    s = Solution()
    res = s.deleteDuplicates(head)
    res_list = nh.printNode(res)
    print(res_list)
    assert res_list == [1,2,3,6]