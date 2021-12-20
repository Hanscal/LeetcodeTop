# -*- coding: utf-8 -*-

"""
@Time    : 2021/12/17 1:36 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from typing import List
"""
给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        self.ans = []
        self.dfs(root, 0)
        return self.ans

    def dfs(self, root, l):
        if not root: return
        if len(self.ans) == l: self.ans.append([])  # 每一层开始

        # 通过元素的奇数和偶数交替存储
        if l % 2 == 0:
            self.ans[l].append(root.val)
        else:
            self.ans[l].insert(0, root.val)
        if root.left: self.dfs(root.left, l + 1)
        if root.right: self.dfs(root.right, l + 1)



def createTree(root):
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
        if item:
            leftNumber = item
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(root):
            break

        item = root[index]
        index += 1
        if item:
            rightNumber = item
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)

        front += 1

    return Root


def printTree(root):
    if root:
        printTree(root.left)
        print(root.val)
        printTree(root.right)

if __name__ == '__main__':
    t = createTree([3,9,20,None,None,15,7])
    printTree(t)
    s = Solution()
    res = s.zigzagLevelOrder(t)
    print(res)
    assert res == [[3], [20, 9], [15, 7]]
