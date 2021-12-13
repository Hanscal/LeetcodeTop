# -*- coding: utf-8 -*-

"""
@Time    : 2021/12/10 12:53 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
"""
给定两个字符串text1 和text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列，返回 0 。

一个字符串的子序列是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。

"""

"""
递归篇
->自顶向下(递归数)；->备忘录优化
动态规划篇
->自底向上，重叠子问题(最优子结构)；->DP-Table优化；
明确「状态」 -> 定义 dp 数组/函数的含义 -> 明确「选择」-> 明确 base case。
1、遍历的过程中，所需的状态必须是已经计算出来的。 
2、遍历的终点必须是存储结果的那个位置。

正向遍历
int[][] dp = new int[m][n];
for (int i = 0; i < m; i++)
for (int j = 0; j < n; j++)
// 计算 dp[i][j]

反向遍历
for (int i = m - 1; i >= 0; i--)
for (int j = n - 1; j >= 0; j--)
// 计算 dp[i][j]

斜向遍历
for (int l = 2; l <= n; l++) {
for (int i = 0; i <= n - l; i++) {
int j = l + i - 1;
// 计算 dp[i][j]

"""

# 动态规划
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 初始化dp
        M, N = len(text1), len(text2)
        dp = [[0] * (N+1) for _ in range(M+1)]

        for i1, t1 in enumerate(text1, 1):
            for i2, t2 in enumerate(text2, 1):
                if t1 == t2:
                    dp[i1][i2] = dp[i1-1][i2-1] + 1
                else:
                    dp[i1][i2] = max(dp[i1-1][i2], dp[i1][i2-1])
        return dp[M][N]


if __name__ == '__main__':
    s = Solution()
    text1 = "abcde"
    text2 = "ace"
    res = s.longestCommonSubsequence(text1, text2)
    print(res)
    assert res == 3