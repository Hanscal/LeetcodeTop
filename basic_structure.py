# -*- coding: utf-8 -*-

"""
@Time    : 2021/12/29 12:09 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

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


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TreeHandle:
    def __init__(self):
        self.res_list = []

    def createTree(self, root:List):
        if not root:
            return root

        Root = TreeNode(root[0])
        nodeQueue = [Root]
        index = 1
        front = 0
        while index < len(root):
            node = nodeQueue[front]

            item = root[index]
            index += 1
            if item is not None:
                leftNumber = item
                node.left = TreeNode(leftNumber)
                nodeQueue.append(node.left)

            if index >= len(root):
                break

            item = root[index]
            index += 1
            if item is not None:
                rightNumber = item
                node.right = TreeNode(rightNumber)
                nodeQueue.append(node.right)

            front += 1

        return Root

    # def printTree(self, root):
    #     if root:
    #         self.printTree(root.left)
    #         print(root.val)
    #
    #         self.printTree(root.right)

    def printTree(self, root):
        # 使用列表作为队列
        queue = []
        # 将首个根节点添加到队列中
        queue.append(root)
        # 当队列不为空时进行遍历
        while queue:
            # 从队列头部取出一个节点并判断其是否有左右节点
            # 若有子节点则把对应子节点添加到队列中，且优先判断左节点
            temp = queue.pop(0)
            left = temp.left
            right = temp.right
            if left:
                queue.append(left)
            if right:
                queue.append(right)
            print(temp.val)
            self.res_list.append(temp.val)
        return self.res_list


