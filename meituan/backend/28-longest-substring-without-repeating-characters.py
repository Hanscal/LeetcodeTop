# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/9 5:33 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
"""给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。"""

# hash + 滑窗 + 左右指针
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        # i代表左指针
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans

if __name__ == '__main__':
    s = Solution()
    res = s.lengthOfLongestSubstring("abcabcbb")
    print(res)
    assert res == 3