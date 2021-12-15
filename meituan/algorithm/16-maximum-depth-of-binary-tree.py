# -*- coding: utf-8 -*-

"""
@Time    : 2021/12/15 5:59 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

def createTree(root):
    if not root:
        return root

    Root = TreeNode(root[0])
    nodeQueue = [Root]
    index = 1  # 两个指针，其中一个
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
    res = s.maxDepth(t)
    print(res)
    assert res == 3