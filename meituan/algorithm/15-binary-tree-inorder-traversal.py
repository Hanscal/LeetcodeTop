# -*- coding: utf-8 -*-

"""
@Time    : 2021/12/15 4:46 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""

from typing import Optional, List

"""给定一个二叉树的根节点 root ，返回它的 中序 遍历。"""

# 递归
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = []
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        if root:
            self.inorderTraversal(root.left)
            self.res.append(root.val)
            self.inorderTraversal(root.right)
        return self.res



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


if __name__ == "__main__":
    root = [1, None, 2, 3]
    treeRoot = createTree(root)
    printTree(treeRoot)
    res = Solution().inorderTraversal(treeRoot)
    print(res)
    assert res == [1,3,2]

