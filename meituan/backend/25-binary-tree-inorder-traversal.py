# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/7 6:42 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from typing import Optional
from typing import List
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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        if root != None:
            self.inorderTraversal(root.left)
            self.res.append(root.val)
            self.inorderTraversal(root.right)
        return self.res

if __name__ == '__main__':
    th = TreeHandle()
    root = th.createTree([1,None,2,3])
    s = Solution()
    res = s.inorderTraversal(root)
    print(res)
    assert res == [1,3,2]