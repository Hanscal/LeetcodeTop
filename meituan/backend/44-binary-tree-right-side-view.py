# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/20 1:07 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from typing import List
from basic_structure import TreeHandle

"""给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 树的宽度优先遍历，当stack中为最后一个元素的时候append, 每一层只能看见一个值
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        rightmost_value_at_depth = dict()  # 深度为索引，存放节点的值
        max_depth = -1

        queue = [(root, 0)]
        while queue:
            node, depth = queue.pop(0)

            if node is not None:
                # 维护二叉树的最大深度
                max_depth = max(max_depth, depth)

                # 由于每一层最后一个访问到的节点才是我们要的答案，因此不断更新对应深度的信息即可
                rightmost_value_at_depth[depth] = node.val

                queue.append((node.left, depth + 1))
                queue.append((node.right, depth + 1))

        return [rightmost_value_at_depth[depth] for depth in range(max_depth + 1)]

if __name__ == '__main__':
    th = TreeHandle()
    root = th.createTree([1,2,3,None,5,None,4])
    s = Solution()
    res = s.rightSideView(root)
    print(res)
    assert res == [1,3,4]
