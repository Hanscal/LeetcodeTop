# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/20 12:15 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""

"""
给定两个字符串text1 和text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。

一个字符串的子序列是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。
"""

# 注意没有提到连续
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 初始化dp
        M, N = len(text1), len(text2)
        dp = [[0] * (N+1) for _ in range(M+1)]

        for i1, t1 in enumerate(text1, 1): # 从1开始计数
            for i2, t2 in enumerate(text2, 1):
                if t1 == t2:
                    dp[i1][i2] = dp[i1-1][i2-1] + 1
                else:
                    dp[i1][i2] = max(dp[i1-1][i2], dp[i1][i2-1])
        return dp[M][N]

if __name__ == '__main__':
    s = Solution()
    res = s.longestCommonSubsequence(text1 = "abcde", text2 = "ace" )
    print(res)
    assert res == 3