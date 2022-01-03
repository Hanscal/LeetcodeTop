# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/3 10:47 上午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from typing import Optional, List
from basic_structure import TreeHandle

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.res = []

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            self.res.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
        return self.res

if __name__ == '__main__':
    th = TreeHandle()
    root = th.createTree([1, None, 2,3])
    s = Solution()
    res = s.preorderTraversal(root)
    print(res)
    assert res == [1,2,3]

