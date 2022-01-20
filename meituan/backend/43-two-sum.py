# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/20 12:39 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""

"""
给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出和为目标值 target的那两个整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。
"""
from typing import List

# hashmap
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        res = []
        for i,num in enumerate(nums):
            if target - num in hash_map:
                res = [hash_map[target - num], i]
            else:
                hash_map[num] = i
        return res

if __name__ == '__main__':
    s = Solution()
    res = s.twoSum(nums = [2,7,11,15], target = 9)
    print(res)
    assert res == [0,1]