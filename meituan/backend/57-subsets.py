# -*- coding: utf-8 -*-

"""
@Time    : 2022/2/7 2:28 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from typing import List

"""
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
"""

# 回溯，DFS
# 因此回溯算法与 DFS 的区别就是有无状态重置
# 当问题需要 "回头"，以此来查找出所有的解的时候，使用回溯算法。即满足结束条件或者发现不是正确路径的时候(走不通)，要撤销选择，回退到上一个状态，继续尝试，直到找出所有解为止

# 回溯结题步骤
# ①画出递归树，找到状态变量(回溯函数的参数)，这一步非常重要※
# ②根据题意，确立结束条件
# ③找准选择列表(与函数参数相关),与第一步紧密关联※
# ④判断是否需要剪枝
# ⑤作出选择，递归调用，进入下一层
# ⑥撤销选择

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        q = [[]]
        n = len(nums)
        for i in range(n):
            for j in range(len(q)):
                q.append(q[j] + [nums[i]])
        return q


if __name__ == '__main__':
    s = Solution()
    res = s.subsets(nums = [1,2,3])
    print(res)
    assert res == [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]