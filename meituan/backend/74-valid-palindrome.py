# -*- coding: utf-8 -*-

"""
@Time    : 2022/2/10 4:51 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
import string

"""给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        return sgood == sgood[::-1]

if __name__ == '__main__':
    s = Solution()
    res = s.isPalindrome("A man, a plan, a canal: Panama")
    print(res)
    assert res == True