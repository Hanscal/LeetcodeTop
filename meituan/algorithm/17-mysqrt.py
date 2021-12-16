# -*- coding: utf-8 -*-

"""
@Time    : 2021/12/16 5:59 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
"""给你一个非负整数 x ，计算并返回x的 算术平方根 。

由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。

注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。

"""
# 二分查找
class Solution:
    def mySqrt(self, x: int) -> int:
        # 可以用迭代法去解决，x**2 - a = 0, 其实是a的正实根，在s点的斜率为2*s，所以s - f(s)/2*s 更接近的近似值
        if x == 0:
            return 0
        x0 = x # 迭代的起点
        while True: # 迭代条件
            x1 = 0.5 * (x0 + x/x0)
            if abs(x1 - x0) < 1e-7:
                return int(x1)
            x0 = x1


if __name__ == '__main__':
    s = Solution()
    res = s.mySqrt(8)
    print(res)
    assert res == 2
