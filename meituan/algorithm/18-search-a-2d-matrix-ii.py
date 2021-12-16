# -*- coding: utf-8 -*-

"""
@Time    : 2021/12/16 6:42 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from typing import List


"""
编写一个高效的算法来搜索mxn矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。

"""

# 二分查找， 分治
# 右上角开始遍历
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix[0])
        col = len(matrix)
        # 右上角开始
        r, c = 0, col - 1
        while c >= 0 and r < row:
            if matrix[r][c] < target:
                r += 1
            elif matrix[r][c] > target:
                c -= 1
            else:
                return True
        return False



if __name__ == '__main__':
    s = Solution()
    res = s.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5)
    print(res)
    assert res == True