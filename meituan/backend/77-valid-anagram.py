# -*- coding: utf-8 -*-

"""
@Time    : 2022/2/14 12:00 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""

"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
注意：若s 和 t中每个字符出现的次数都相同，则称s 和 t互为字母异位词。
进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
"""
# 最初想法是hashmap，可以排序后比较
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_map = {}
        for i in s:
            hash_map[i] = hash_map.get(i, 0) + 1

        for i in t:
            hash_map[i] = hash_map.get(i, 0) - 1
            if hash_map[i] < 0:  # 在长度相等的情况下肯定会出现小于0的情况
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    res = s.isAnagram(s = "rat", t = "cat")
    print(res)
    assert res == False