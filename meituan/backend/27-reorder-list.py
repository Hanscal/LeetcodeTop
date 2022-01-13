# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/9 5:32 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from basic_structure import NodeHandle

"""
给定一个单链表 L 的头节点 head ，单链表 L 表示为：

L0 → L1 → … → Ln - 1 → Ln
请将其重新排列后变为：

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""

# 可以存到列表中，然后再组合
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 双指针，将列表平分成两个，将第二个表逆序，拼接
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        mid = self.middleNode(head)
        l1 = head
        l2 = mid.next
        mid.next = None
        l2 = self.reverseList(l2)
        self.mergeList(l1, l2)
        return head

    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp
        return prev

    def mergeList(self, l1: ListNode, l2: ListNode):
        while l1 and l2:
            l1_tmp = l1.next
            l2_tmp = l2.next

            l1.next = l2
            l1 = l1_tmp

            l2.next = l1
            l2 = l2_tmp


if __name__ == '__main__':
    nh = NodeHandle()
    for i in [1,2,3,4][::-1]:
        head = nh.add(i)
    s = Solution()
    res = s.reorderList(head)
    res_list = nh.printNode(res)
    print(res_list)
    assert res_list == [1,4,2,3]