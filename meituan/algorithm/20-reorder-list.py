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

class Node_handle():
    def __init__(self):
        self.cur_node = None

    # 查找
    def find(self,node,num,a = 0):
        while node:
            if a == num:
                return node
            a += 1
            node = node.next

    # 增加
    def add(self,data):
        node = ListNode()
        node.val = data
        node.next = self.cur_node
        self.cur_node = node
        return node

    # 打印
    def printNode(self,node):
        out = []
        while node:
            print('value: ', node.val)
            out.append(node.val)
            node = node.next
        return out

    # 删除
    def delete(self,node,num,b = 1):
        if num == 0:
            node = node.next
            return node
        while node and node.next:
            if num == b:
                node.next = node.next.next
            b += 1
            node = node.next
        return node

    # 翻转
    def reverse(self,nodelist):
        list = []
        while nodelist:
            list.append(nodelist.val)
            nodelist = nodelist.next
        result = ListNode()
        result_handle =Node_handle()
        for i in list:
            result = result_handle.add(i)
        return result


if __name__ == '__main__':
    nh = Node_handle()
    a = [1,2,3,4]
    a.reverse()
    for i in a:
        root = nh.add(i)
    nh.printNode(root)
    s = Solution()
    res = s.reorderList(root)
    out = nh.printNode(res)
    assert out == [1,4,2,3]

