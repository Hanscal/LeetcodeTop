# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/3 11:05 上午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""

"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
If the two linked lists have no intersection at all, return null.
"""
from basic_structure import NodeHandle

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A

if __name__ == '__main__':
    nh = NodeHandle()
    na = ListNode(4)
    n2 = ListNode(1)
    n3 = ListNode(8)
    n4 = ListNode(4)
    n5 = ListNode(5)
    na.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    nb = ListNode(5)
    nb2 = ListNode(6)
    nb3 = ListNode(1)
    nb.next = nb2
    nb2.next = nb3
    nb3.next = n3
    s = Solution()
    res = s.getIntersectionNode(na, nb)
    res_list = nh.printNode(res)
    print(res_list)
    assert res_list == [8,4,5]