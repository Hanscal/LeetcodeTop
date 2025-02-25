# -*- coding: utf-8 -*-

"""
@Time    : 2022/2/7 12:19 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""

"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
"""

# 动态规划
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1]+ dp[i-2]
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    res = s.climbStairs(2)
    print(res)
    assert res == 2
