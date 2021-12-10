# -*- coding: utf-8 -*-

"""
@Time    : 2021/12/10 2:26 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""

from typing import List

"""
给你一个大小为 m x n 的矩阵 mat ，请以对角线遍历的顺序，用一个数组返回这个矩阵中的所有元素。
"""

"""
找出向上行走对角线头部需要遵循两个规则：
如果当前尾部不在矩阵最后一行，则下一个对角线的头部是当前尾部的正下方元素；否则，下一条对角线首部是当前尾部的右边元素。

找出向下行走对角线头部需要遵循两个规则：
如果当前尾部不在矩阵最后一行，下一条对角线的首部是当前尾部正下方元素；否则，下一条对角线首部是当前尾部的右边元素。
"""

"""
假设n行m列，当前的点为(i,j)，每次遍历在直线i+j=z上，z从0到m+n-2
利用i进行遍历，有两个不等式
0<=i<n
0<=j<m，也就是0<=z-i<m
可以得到
0<=i<n和z-m<i<=z
然后把小于号后面的-1或前面的+1变成小于等于，得到
0<=i<=n-1和z-m+1<=i<=z
因此下界为
max(0,z-m+1)
上界为
min(n-1,z)
然后依次按照从上界到下界，从下届到上界的顺序遍历，记得上下界都要能取到

"""

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # 分不同的方向，右上方向，左下方向，越界处理
        n = len(mat)
        m = len(mat[0])
        flag = 0
        ans = []

        for z in range(0, m + n - 2 + 1):
            if flag:
                # print(max(0, z - m + 1), min(z, n - 1) + 1)
                for i in range(max(0, z - m + 1), min(z, n - 1) + 1):
                    ans.append(mat[i][z - i])
                flag = 0
            else:
                # print(min(z, n - 1), max(0, z - m + 1) - 1)
                for i in range(min(z, n - 1), max(0, z - m + 1) - 1, -1):
                    ans.append(mat[i][z - i])
                flag = 1

        return ans


if __name__ == '__main__':
    s = Solution()
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    res = s.findDiagonalOrder(mat)
    print(res)
    assert res == [1,2,4,7,5,3,6,8,9]