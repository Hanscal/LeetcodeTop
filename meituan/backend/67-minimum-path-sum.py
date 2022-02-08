# -*- coding: utf-8 -*-

"""
@Time    : 2022/2/8 2:54 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from typing import List

"""
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。
"""
# 动态规划
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, columns = len(grid), len(grid[0])
        # 初始化dp
        dp = [[0] * columns for _ in range(rows)]
        dp[0][0] = grid[0][0]
        for i in range(1, rows):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, columns):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        # 状态更新
        for i in range(1, rows):
            for j in range(1, columns):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[rows - 1][columns - 1]


if __name__ == '__main__':
    s = Solution()
    res = s.minPathSum(grid = [[1,3,1],[1,5,1],[4,2,1]])
    print(res)
    assert res == 7