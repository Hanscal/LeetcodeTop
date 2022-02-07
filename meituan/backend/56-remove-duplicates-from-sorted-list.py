# -*- coding: utf-8 -*-

"""
@Time    : 2022/2/7 2:28 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from basic_structure import NodeHandle

"""给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head

        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head

if __name__ == '__main__':
    nh = NodeHandle()
    for i in [1,1,2,3,3][::-1]:
        head = nh.add(i)
    s = Solution()
    res = s.deleteDuplicates(head)
    res_list = nh.printNode(res)
    print(res_list)
    assert res_list == [1,2,3]
