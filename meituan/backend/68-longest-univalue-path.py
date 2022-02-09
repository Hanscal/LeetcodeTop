# -*- coding: utf-8 -*-

"""
@Time    : 2022/2/9 4:06 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from basic_structure import TreeHandle

"""
给定一个二叉树的root，返回最长的路径的长度 ，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。

两个节点之间的路径长度由它们之间的边数表示。
"""
# 深度优先搜索
# Definition for a binary tree node.
# 对于每个节点，我们想知道向左延伸的最长箭头和向右延伸的最长箭头是什么？我们可以用递归来解决这个问题。
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ans = 0

        def arrow_length(node):
            if not node: return 0
            # 左子树遍历
            left_length = arrow_length(node.left)
            # 右子树遍历
            right_length = arrow_length(node.right)

            left_arrow = right_arrow = 0 # 中间变量比较巧妙
            if node.left and node.left.val == node.val:
                left_arrow = left_length + 1
            if node.right and node.right.val == node.val:
                right_arrow = right_length + 1
            self.ans = max(self.ans, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)

        arrow_length(root)
        return self.ans


if __name__ == '__main__':
    th = TreeHandle()
    root = th.createTree([5,4,5,1,1,5])
    s = Solution()
    res = s.longestUnivaluePath(root)
    print(res)
    assert res == 2