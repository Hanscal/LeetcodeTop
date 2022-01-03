# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/3 10:45 上午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from typing import Optional
from basic_structure import TreeHandle
"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. 
A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any non-empty path.
"""

# 二叉树中最大路径和
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxsum = float('-inf')

        def dfs(root):
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.maxsum = max(self.maxsum, left + right + root.val)
            return max(0, max(left, right) + root.val)

        dfs(root)
        return self.maxsum

if __name__ == '__main__':
    th = TreeHandle()
    root = th.createTree([-10,9,20,None,None,15,7])
    s = Solution()
    res = s.maxPathSum(root)
    print(res)
    assert res == 42