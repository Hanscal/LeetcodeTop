# -*- coding: utf-8 -*-

"""
@Time    : 2021/12/23 4:28 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from typing import List

"""给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。"""

# 哈希，矩阵

class Solution:
    def setZeroes(self, matrix: List[List[int]]):
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        row, col = [False] * m, [False] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = col[j] = True

        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    matrix[i][j] = 0
        return matrix

if __name__ == '__main__':
    s = Solution()
    res = s.setZeroes([[1,1,1],[1,0,1],[1,1,1]])
    print(res)
    assert res == [[1,0,1],[0,0,0],[1,0,1]]