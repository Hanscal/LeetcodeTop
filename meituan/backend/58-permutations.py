# -*- coding: utf-8 -*-

"""
@Time    : 2022/2/8 11:39 上午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from typing import List
"""
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
1 <= nums.length <= 6
-10 <= nums[i] <= 10
nums 中的所有整数 互不相同
"""

# 回溯
# 深度优先遍历、递归、栈之间的关系，
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, size, depth, path, used, res):
            if depth == size:  # 当树的深度与size一致时终止
                res.append(path[:]) # 对路径的copy
                return

            for i in range(size):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])

                    dfs(nums, size, depth + 1, path, used, res)

                    used[i] = False
                    path.pop()  # 撤销操作，状态重置，退回到上一层

        size = len(nums)
        if len(nums) == 0:
            return []

        used = [False for _ in range(size)] # 用空间换时间（一般操作，记录状态）
        res = []
        dfs(nums, size, 0, [], used, res)
        return res

if __name__ == '__main__':
    s = Solution()
    res = s.permute([1,2,3])
    print(res)
    assert res == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]