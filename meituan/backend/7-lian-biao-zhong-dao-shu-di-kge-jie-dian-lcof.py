# -*- coding: utf-8 -*-

"""
@Time    : 2021/12/29 3:16 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from basic_structure import NodeHandle

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        former, latter = head, head
        for _ in range(k):
            former = former.next
        while former:
            former, latter = former.next, latter.next
        return latter

if __name__ == '__main__':
    nh = NodeHandle()
    for i in [1,2,3,4,5][::-1]:
        head = nh.add(i)
    nh.printNode(head)
    s = Solution()
    res = s.getKthFromEnd(head, 2)
    res_list = nh.printNode(res)
    assert res_list == [4, 5]