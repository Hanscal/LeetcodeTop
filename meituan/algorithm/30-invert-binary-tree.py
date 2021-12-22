# -*- coding: utf-8 -*-

"""
@Time    : 2021/12/22 11:55 上午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""

"""翻转一棵二叉树。"""
# 树 + 遍历

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # 递归函数的终止条件，节点为空时返回
        if not root:
            return None
        # 将当前节点的左右子树交换
        root.left, root.right = root.right, root.left
        # 递归交换当前节点的 左子树和右子树
        self.invertTree(root.left)
        self.invertTree(root.right)
        # 函数返回时就表示当前这个节点，以及它的左右子树
        # 都已经交换完了
        return root

class CreateTree(object):
    def __init__(self):
        self.resp = []

    def createTree(self, root):
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

    def printTree(self, root):
        if root:
            print(root.val)
            self.resp.append(root.val)
            self.printTree(root.left)
            self.printTree(root.right)

if __name__ == '__main__':
    ct = CreateTree()
    t = ct.createTree([4,2,7,1,3,6,9]) # 中序遍历
    ct.printTree(t)  # [4,2,1,3,7,6,9]
    s = Solution()
    res = s.invertTree(t) # [4,7,9,6,2,3,1]
    ct.printTree(res)
