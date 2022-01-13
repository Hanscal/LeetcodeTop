# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/7 6:27 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from basic_structure import TreeHandle

"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：
对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。

说明:
所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉树中。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root.val == p.val or root.val == q.val: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left: return right
        if not right: return left
        return root

if __name__ == '__main__':
    th = TreeHandle()
    root = th.createTree([3,5,1,6,2,0,8,None,None,7,4])
    p = th.createTree([5, 6, 2, None,None,7,4])
    q = th.createTree([1,0,8])
    s = Solution()
    res = s.lowestCommonAncestor(root, p, q)
    res_list = th.printTree(res)
    assert res_list == [3,5,1,6,2,0,8,7,4]
