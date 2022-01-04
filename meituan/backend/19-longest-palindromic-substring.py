# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/4 6:05 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
"""给你一个字符串 s，找到 s 中最长的回文子串。"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 遍历，以某个字符为中心的回文子串，从中间向两边扩散来判断回文串。
        res = ''
        for i in range(len(s)):
            # 如果是奇数
            str_odd = self.find_palindrome(s, i, i)
            # 如果是偶数
            str_even = self.find_palindrome(s, i, i + 1)
            if len(str_odd) > len(str_even):
                res = str_odd if len(str_odd) > len(res) else res
            else:
                res = str_even if len(str_even) > len(res) else res
        return res

    def find_palindrome(self, stra, i, j):
        while i >= 0 and j < len(stra):
            if stra[i] != stra[j]:
                break
            else:
                i -= 1
                j += 1
        return stra[i + 1:j]

if __name__ == '__main__':
    s = Solution()
    res = s.longestPalindrome("babad")
    print(res)
    assert res == 'bab'