# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/20 12:39 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from basic_structure import TreeHandle
"""
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。
"""

# 深度优先搜索， 二叉树
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        flag = True if abs(self.dfs(root.right) - self.dfs(root.left)) <= 1 \
                       and self.isBalanced(root.right) \
                       and self.isBalanced(root.left) else False
        return flag

    def dfs(self, node):
        if not node:
            return 0
        return max(self.dfs(node.left), self.dfs(node.right)) + 1

if __name__ == '__main__':
    th = TreeHandle()
    root = th.createTree([3,9,20,None,None,15,7])
    s = Solution()
    res = s.isBalanced(root)
    print(res)
    assert res == True