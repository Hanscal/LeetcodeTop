# -*- coding: utf-8 -*-

"""
@Time    : 2022/2/9 4:06 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
"""
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：

F(0) = 0, F(1)= 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
"""

class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        f0 = 0
        f1 = 1
        for i in range(2, n + 1):
            f0, f1 = f1, f0 + f1
        return f1 % 1000000007 if f1 / 1000000007 > 1 else f1

if __name__ == '__main__':
    s = Solution()
    res = s.fib(5)
    print(res)
    assert res == 5
