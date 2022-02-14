# -*- coding: utf-8 -*-

"""
@Time    : 2022/2/14 12:26 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from typing import List
"""
给定一个三角形 triangle ，找出自顶向下的最小路径和。
每一步只能移动到下一行中相邻的结点上。
相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。

可以将空间复杂度优化至 O(n)
# 我们使用两个长度为 n的一维数组进行转移，将 i根据奇偶性映射到其中一个一维数组，那么 i-1就映射到了另一个一维数组
"""

# 动态规划
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        f = [[0] * n for _ in range(n)]
        f[0][0] = triangle[0][0]

        for i in range(1, n):
            f[i][0] = f[i - 1][0] + triangle[i][0]
            for j in range(1, i):
                f[i][j] = min(f[i - 1][j - 1], f[i - 1][j]) + triangle[i][j]
            f[i][i] = f[i - 1][i - 1] + triangle[i][i]

        return min(f[n - 1])


if __name__ == '__main__':
    s = Solution()
    res = s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
    print(res)
    assert res == 11