# -*- coding: utf-8 -*-

"""
@Time    : 2021/12/11 9:45 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""

"""写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。"""

"""
1）分析上面对二进制的计算过程
a.计算不进位的和，相当于对两个数进制异或：1101^1001=0100；
b.计算进位，第1位相当于对两个数求与：1101&1001=1001，然后再对其进行左移1位：
2）计算a+b，等价于(a^b)+((a&b)<<1)。
由于公式中又出现了+号，因此要再重复2）这个等价的计算过程。
结束条件是：没有进位了。
"""

# 位运算
class Solution:
    def add(self, a: int, b: int) -> int:
        while b:
            sum = a ^ b
            carry = a & b << 1
            a = sum
            b = carry
        return a

if __name__ == '__main__':
    s = Solution()
    res = s.add(1000000000000000,1)
    print(res)
    assert res == 1000000000000001

