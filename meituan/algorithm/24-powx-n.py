# -*- coding: utf-8 -*-

"""
@Time    : 2021/12/20 12:22 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""

"""实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。"""
"""当一个数 & 1若为1，即该数的最后一位为1，不能被2整除，否则代表可以被2整数。"""

"""比如我们要计算x的y次方。通常情况我们需要执行y次。但是如果我们将其转化为(x*x) ^ (y/2)就只需要执行一半的时间了，那么如果是()(x*x) * (x*x)) ^ (y/2/2)就只用四分之一的时间了，
类似O(logn) 的方式。但这里有一个问题，你怎么知道y能一直被二整除呢？于是可以转为二进制的移位表示"""

# 递归，二进制
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0: x, n = 1 / x, -n
        res = 1
        while n:
            if n & 1:
                res *= x
            x *= x
            n = n >> 1
        return res

class Solution1:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        ret = self.myPow(x, n // 2)
        return ret * ret if n % 2 == 0 else ret * ret * x

class Solution2:
    def myPow(self, x: float, n: int) -> float:
        if x == 0.0:
            return 0.0
        powx = 1
        # n 为正数
        if n < 0:
            x, n = 1 / x, -n
        for i in range(n):
            powx = x*powx
        return powx


if __name__ == '__main__':
    s = Solution()
    res = s.myPow(2.00000, 10)
    print(res)
    assert res == 1024.00000