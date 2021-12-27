# -*- coding: utf-8 -*-

"""
@Time    : 2021/12/27 5:55 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from typing import List

"""
给定一个正整数、负整数和 0 组成的 N × M矩阵，编写代码找出元素总和最大的子矩阵。
返回一个数组 [r1, c1, r2, c2]，其中 r1, c1 分别代表子矩阵左上角的行号和列号，r2, c2 分别代表右下角的行号和列号。若有多个满足条件的子矩阵，返回任意一个均可。
"""

# 动态规划， 前缀和
class Solution:
    def getMaxMatrix(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        maxx = matrix[0][0] # 记录最大值
        pos = [0, 0, 0, 0]
        for i in range(m):
            b = matrix[i]  # 记录当前i~j行组成大矩阵的每一列的和，将二维转化为一维
            for j in range(i, m):
                if j > i:
                    for k in range(n):
                        b[k] += matrix[j][k]  # 求解i+1行到m行的值
                dp = 0
                begin = 0
                for t in range(n): # 转换为一维dp
                    if dp < 0:
                        dp = b[t]
                        begin = t # 自立门户
                    else:
                        dp += b[t]

                    if dp > maxx:
                        maxx = dp
                        pos[0] = i
                        pos[1] = begin
                        pos[2] = j
                        pos[3] = t
        return pos

if __name__ == '__main__':
    matrix = [[-1,0],
              [0,-1]]
    s = Solution()
    res = s.getMaxMatrix(matrix)
    print(res)
    assert res == [0,1,0,1]
