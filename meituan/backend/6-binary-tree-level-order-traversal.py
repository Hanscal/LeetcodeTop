# -*- coding: utf-8 -*-

"""
@Time    : 2021/12/29 3:13 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from typing import List
from basic_structure import TreeHandle

"""给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 广度优先遍历
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        # 队列实现
        res = []
        def dfs(index, r):
            # 假设res是[ [1],[2,3] ]， index是3，就再插入一个空list放到res中
            if len(res) == index:
                res.append([])
            #  将当前节点的值加入到res中，index代表当前层，假设index是3，节点值是99
            # res是[ [1],[2,3] [4] ]，加入后res就变为 [ [1],[2,3] [4,99] ]
            res[index].append(r.val)
            # 递归的处理左子树，右子树，同时将层数index+1
            if r.left:
                dfs(index + 1, r.left)
            if r.right:
                dfs(index + 1, r.right)
        dfs(0, root)
        return res


if __name__ == '__main__':
    th = TreeHandle()
    root = th.createTree([3,9,20,None,None,15,7])
    s = Solution()
    res = s.levelOrder(root)
    print(res)
    assert res == [[3], [9, 20], [15, 7]]
