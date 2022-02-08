# -*- coding: utf-8 -*-

"""
@Time    : 2022/2/8 2:29 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""

"""
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。
"""

# 进阶：你能不将整数转为字符串来解决这个问题吗？
# 通过取整和取余操作获取整数中对应的数字进行比较。
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        for i in range(len(x_str)):
            if x_str[i] != x_str[len(x_str) - i - 1]:
                return False
        return True

# 将数翻转
class Solution1:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        revertedNumber = 0
        num = x
        while num != 0:
            revertedNumber = revertedNumber * 10 + num % 10
            num //= 10
        return x == revertedNumber

if __name__ == '__main__':
    s = Solution1()
    res = s.isPalindrome(x=121)
    print(res)
    assert res == True