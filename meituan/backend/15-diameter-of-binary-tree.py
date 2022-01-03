# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/3 10:52 上午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
"""
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.
"""
from basic_structure import TreeHandle

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1

        def depth(node):
            # 访问到空节点了，返回0
            if not node:
                return 0
            # 左儿子为根的子树的深度
            L = depth(node.left)
            # 右儿子为根的子树的深度
            R = depth(node.right)
            # 计算d_node即L+R+1 并更新ans
            self.ans = max(self.ans, L + R + 1)
            # 返回该节点为根的子树的深度
            return max(L, R) + 1

        depth(root)
        return self.ans - 1

if __name__ == '__main__':
    th = TreeHandle()
    root = th.createTree([1,2,3,4,5])
    s = Solution()
    res = s.diameterOfBinaryTree(root)
    print(res)
    assert res == 3