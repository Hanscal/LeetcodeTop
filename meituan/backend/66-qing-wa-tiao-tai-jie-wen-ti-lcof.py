# -*- coding: utf-8 -*-

"""
@Time    : 2022/2/8 2:54 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""

"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n级的台阶总共有多少种跳法。
答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
"""

# 动态规划, 斐波拉契数列
class Solution:
    def numWays(self, n: int) -> int:
        dp0 = 1
        dp1 = 1
        for i in range(2, n+1):
            dp0, dp1 = dp1, dp0 + dp1
        return dp1 % 1000000007

if __name__ == '__main__':
    s = Solution()
    res = s.numWays(7)
    print(res)
    assert res == 21