# -*- coding: utf-8 -*-

"""
@Time    : 2021/12/27 6:38 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from typing import List

"""
给你一个 无重复元素 的整数数组candidates 和一个目标整数target，找出candidates中可以使数字和为目标数target 的 所有不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。
candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。
对于给定的输入，保证和为target 的不同组合数少于 150 个。
"""

# 回溯
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, begin, size, path, res, target):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return

            for index in range(begin, size):
                dfs(candidates, index, size, path + [candidates[index]], res, target - candidates[index])

        size = len(candidates)
        if size == 0:
            return []
        path = []
        res = []
        dfs(candidates, 0, size, path, res, target)
        return res

if __name__ == '__main__':
    s = Solution()
    res = s.combinationSum(candidates=[2,3,6,7], target=7)
    print(res)
    assert res == [[2,2,3],[7]]