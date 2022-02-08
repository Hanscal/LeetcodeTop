# -*- coding: utf-8 -*-

"""
@Time    : 2022/2/8 1:11 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
"""
给你一个非负整数 x ，计算并返回x的算术平方根 。
由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。

注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。
"""

# 需要用到数学知识，二分查找和牛顿迭代，牛顿迭代比二分查找算法更快
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        C, x0 = float(x), float(x)
        while True:
            xi = 0.5 * (x0 + C / x0)
            if abs(x0 - xi) < 1e-7:
                break
            x0 = xi

        return int(x0)

"""
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans
"""

if __name__ == '__main__':
    s = Solution()
    res = s.mySqrt(4)
    print(res)
    assert res == 2