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

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        for i in range(len(x_str)):
            if x_str[i] != x_str[len(x_str) - i - 1]:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    res = s.isPalindrome(x=121)
    print(res)
    assert res == True