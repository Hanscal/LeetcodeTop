# -*- coding: utf-8 -*-

"""
@Time    : 2022/2/14 12:00 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from basic_structure import TreeHandle
"""给你一个二叉树的根节点 root ， 检查它是否轴对称。"""
# 它们的两个根结点具有相同的值
# 每个树的右子树都与另一个树的左子树镜像对称

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        else:
            return self.check(root.left, root.right)

    def check(self, node1, node2):
        if (node1 == node2):
            return True
        if (node1 is None or node2 is None):
            return False
        return (node1.val == node2.val) and (self.check(node1.left, node2.right)) and (self.check(node1.right, node2.left))


if __name__ == '__main__':
    th = TreeHandle()
    root = th.createTree([1,2,2,3,4,4,3])
    s = Solution()
    res = s.isSymmetric(root)
    print(res)
    assert res == True