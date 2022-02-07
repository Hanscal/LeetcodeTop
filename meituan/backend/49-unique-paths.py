# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/24 6:49 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
"""一个机器人位于一个 m x n网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？
"""

# 动态规划
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        # print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

if __name__ == '__main__':
    s = Solution()
    res = s.uniquePaths(3, 7)
    print(res)
    assert res == 28