# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/4 6:04 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from typing import List

"""给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()

        rows, columns = len(matrix), len(matrix[0])
        order = list()
        left, right, top, bottom = 0, columns - 1, 0, rows - 1
        while left <= right and top <= bottom:
            for column in range(left, right + 1):
                order.append(matrix[top][column])
            for row in range(top + 1, bottom + 1):
                order.append(matrix[row][right])
            # 为了判断最后一个边界走向
            if left < right and top < bottom:
                for column in range(right - 1, left, -1):
                    order.append(matrix[bottom][column])
                for row in range(bottom, top, -1):
                    order.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return order

if __name__ == '__main__':
    s = Solution()
    res = s.spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]])
    print(res)
    assert res == [1,2,3,6,9,8,7,4,5]