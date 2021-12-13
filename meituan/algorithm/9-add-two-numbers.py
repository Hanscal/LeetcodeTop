# -*- coding: utf-8 -*-

"""
@Time    : 2021/12/12 9:51 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""

"""
给你两个非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0开头。
"""

# 链表，递归
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        Res = p = ListNode(0)  # Res和p当前都指在表头,需要预留一个指针，同时一个指针去遍历
        carry = 0  # temp用于进位，初始为0，表示无进位，为1，则进一位
        while l1 or l2:  # 判断l1和l2是否为空，不为空，则继续
            # 将l1 和l2表长改成一样长，空的地方用0补充
            if not l1:  # 此时l1空，l2不空，则将l1增加一位，值为0
                l1 = ListNode(0)
            if not l2:  # 此时l2空，l1不空，则将l2增加一位，值为0
                l2 = ListNode(0)
            sum = l1.val + l2.val + carry  # sum表示当前节点下l1,l2,和进位值相加的结果 <10则不进位，temp置零，p链表下一节点值就是sum；>10则进位，temp置1，p链表下一节点值就是sum%10
            # print(sum)
            if (sum < 10):
                carry = 0
                p.next = ListNode(sum)
            else:
                carry = 1
                p.next = ListNode(sum % 10)
            # 当前节点运算结束，前往下一节点
            p = p.next
            l1 = l1.next
            l2 = l2.next
        if (carry):  # 判断最后一次运算有无进位，有进位，则p再加一位节点，置1
            p.next = ListNode(carry)
        return Res.next

if __name__ == '__main__':
    s = Solution()
    l1 = None
    for a in [2,4,3]:
        l1 = ListNode(val=a, next=l1)
    l2 = None
    for a in [5,6,4]:
        l2 = ListNode(val=a, next=l2)
    res = s.addTwoNumbers(l1,l2)
    res_list = []
    while res:
        res_list.append(res.val)
        res = res.next
    print(res_list)
    assert res_list == [7,0,8]

