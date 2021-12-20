# -*- coding: utf-8 -*-

"""
@Time    : 2021/12/20 12:21 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""

"""给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。"""

# 滑动窗口
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic, res, i = {}, 0, -1  # i是左指针
        for j,c in enumerate(s):  # j是右指针
            if c in dic:  # 若当前元素在之前出现过，更新左指针
                # 当之前出现的元素在左右指针中间，左指针更新为之前元素下标，若不在中间，左指针不变
                i = max(i, dic[c])
            dic[c] = j  # 将当前元素加入哈希表中
            res = max(res, j - i)
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.lengthOfLongestSubstring("abcabcbb")
    print(res)
    assert res == 3