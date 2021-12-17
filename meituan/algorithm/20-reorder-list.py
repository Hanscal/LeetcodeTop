# -*- coding: utf-8 -*-

"""
@Time    : 2021/12/17 1:33 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""

"""
先存，然后再二分合并：
时间：o(n)
空间：o(n)，需要额外的空间
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head

        n = 0
        node = head
        while node:
            n += 1
            node = node.next

        # find middle
        prev, curr = None, head
        for _ in range(n // 2 if n % 2 == 0 else (n // 2 + 1)):
            prev = curr
            curr = curr.next

        # reverse last half
        prev.next = None
        prev = None
        while curr.next:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        curr.next = prev

        # merge
        node = head
        while curr:
            nxt = node.next
            node.next = curr
            cnext = curr.next
            curr.next = nxt
            curr = cnext
            node = nxt

        return head

def createTree(nums=[1,2,3,4]):
    if nums:
        head = root = ListNode(nums[0])
        for n in nums[1:]:
            tmp = ListNode(n)
            root.next = tmp
            root = root.next
        return head
    else:
        return ListNode()

def printNode(node):
    while node:
        print(node.val)
        node = node.next

if __name__ == '__main__':
    root = createTree([1,2,3,4])
    printNode(root)
    s = Solution()
    res = s.reorderList(root)
    printNode(res)

