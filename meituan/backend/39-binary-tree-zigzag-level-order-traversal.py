# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/19 1:28 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from typing import List
from basic_structure import TreeHandle

"""给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []

        ans = []
        stack = []
        stack.append(root)
        Layer = 0

        # 广度优先遍历
        while stack:
            cur_ans = []
            Layer += 1
            lenThisLayer = len(stack)
            for _ in range(lenThisLayer):
                cur_node = stack.pop(0)
                cur_ans.append(cur_node.val)
                if cur_node.left:
                    stack.append(cur_node.left)
                if cur_node.right:
                    stack.append(cur_node.right)
            if Layer % 2 == 0:  # 奇数层时倒序数组
                cur_ans.reverse()
            ans.append(cur_ans)

        return ans

if __name__ == '__main__':
    root = TreeHandle().createTree([3,9,20,None,None,15,7])
    s = Solution()
    res = s.zigzagLevelOrder(root)
    print(res)
    assert res == [[3],[20,9],[15,7]]