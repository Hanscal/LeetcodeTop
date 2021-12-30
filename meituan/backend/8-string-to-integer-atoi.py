# -*- coding: utf-8 -*-

"""
@Time    : 2021/12/30 10:06 上午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
"""Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:
1. Read in and ignore any leading whitespace.
2. Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
3. Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
5. If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
6. Return the integer as the final result.
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        res = '0'
        # s = s.replace(' ','') 违反第二条，在中间遇到空格就返回前面的数字
        while len(s) > 0:
            if s[0] == ' ' and res == '0':
                s = s[1:]
            elif s[0] == '-' and res == '0':
                res = '-'
                s = s[1:]
            elif s[0] == '+' and res == '0':
                res = '+'
                s = s[1:]
            elif 48 <= ord(s[0]) <= 57:  # 数字的范围
                res = res + s[0]
                s = s[1:]
            else:
                s = ''
        if res == '-' or res == "+":
            res = 0
        res = int(res)
        if res >= 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif res <= -2 ** 31:
            return -2 ** 31
        else:
            return res

if __name__ == '__main__':
    s = Solution()
    res = s.myAtoi(' -4 2 ')
    print(res)
    assert res == -4