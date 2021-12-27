# -*- coding: utf-8 -*-

"""
@Time    : 2021/12/27 7:28 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""

"""
输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。
例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 双指针，一个比另外一个超前k步
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        former, latter = head, head
        for _ in range(k):
            former = former.next
        while former:
            former, latter = former.next, latter.next
        return latter

class NodeHandle(object):
    def __init__(self):
        self.cur_node = None

    # 查找
    def find(self,node,num,a = 0):
        while node:
            if a == num:
                return node
            a += 1
            node = node.next

    # 反向增加
    def add(self,data):
        node = ListNode(0)
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

if __name__ == '__main__':
    nh = NodeHandle()
    node = [1,2,3,4,5]
    node.reverse()
    for i in node:
        head = nh.add(i)
    nh.printNode(head)

    s = Solution()
    res = s.getKthFromEnd(head, 2)
    nh.printNode(res)


