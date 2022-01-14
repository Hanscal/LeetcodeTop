# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/14 6:41 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
"""
给定两个字符串形式的非负整数num1和num2，计算它们的和并同样以字符串形式返回。
你不能使用任何內建的用于处理大整数的库（比如 BigInteger），也不能直接将输入的字符串转换为整数形式。
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j, carry, res = len(num1) - 1, len(num2) - 1, 0, 0
        ans = ''

        while i >= 0 or j >= 0 or carry != 0:
            val = carry

            if i >= 0:
                val += ord(num1[i]) - ord('0')
                i -= 1
            if j >= 0:
                val += ord(num2[j]) - ord('0')
                j -= 1

            carry, res = divmod(val, 10)
            ans = str(res) + ans

        return ans

if __name__ == '__main__':
    s = Solution()
    res = s.addStrings("11","123")
    print(res)
    assert res == "134"