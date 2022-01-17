# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/14 6:57 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
"""编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为汉明重量）。"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += 1
            n &= n - 1
        return res

if __name__ == '__main__':
    s = Solution()
    res = s.hammingWeight(0b00000000000000000000000000001011)
    print(res)
    assert res == 3
