# -*- coding: utf-8 -*-

"""
@Time    : 2021/12/17 1:29 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""

"""
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

注意：
对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
如果 s 中存在这样的子串，我们保证它是唯一的答案。
"""

# 滑窗

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, window = {}, {}
        for c in t:
            need[c] = need.setdefault(c, 0) + 1

        left, right = 0, 0
        valid = 0
        start, length = 0, len(s) + 1
        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                window[c] = window.setdefault(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            while valid == len(need):
                if right - left < length:
                    start = left
                    length = right - left
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return s[start:start + length] if length != len(s) + 1 else ''



if __name__ == '__main__':
    s = Solution()
    res = s.minWindow("ADOBECODEBANC", "ABC")
    print(res)
    assert res == "BANC"