# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/14 5:58 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from basic_structure import TreeHandle

"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。
特别地，我们希望可以就地完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中的第一个节点的指针。
"""

# Definition for a Node.
# 双向链表，循环链表
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 中序遍历，深度优先搜索，二叉搜索树的中序遍历为 递增序列
# 双指针
class Solution:
    def treeToDoublyList(self, root: Node) -> Node:
        if not root:
            return root
        self.pre = None
        self.dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head


    def dfs(self, cur):
        if not cur: return
        self.dfs(cur.left)  # 左
        # 构建链表
        # 当pre为空时，代表正在访问链表头结点，记为head
        # 当pre不为空时，修改双向节点引用，pre.right = cur, cur.left = pre
        # 保存cur, 更新pre=cur, 即节点cur是后继节点的pre;
        if self.pre:  # 修改节点引用
            self.pre.right, cur.left = cur, self.pre
        else:  # 记录头节点
            self.head = cur
        self.pre = cur  # 保存 cur

        # self.res.append(root.val)  # 根
        self.dfs(cur.right)  # 右


if __name__ == '__main__':
    th = TreeHandle()
    root = th.createTree([4,2,5,1,3])
    s = Solution()
    res = s.treeToDoublyList(root)
    # print(res_list)