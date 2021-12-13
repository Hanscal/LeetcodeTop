# -*- coding: utf-8 -*-

"""
@Time    : 2021/12/13 6:24 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""

from typing import List

"""给你一个整数数组 nums 和一个整数 k ，请你统计并返回该数组中和为 k 的连续子数组的个数。"""

# 暴力法
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum == k:
                    count += 1
        return count

# 前缀和+hashmap
class Solution1:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumi = 0
        presum_map = {0: 1}
        count = 0
        for i in range(len(nums)):
            sumi += nums[i]
            sumj = sumi - k
            if sumj in presum_map:
                count += presum_map[sumj]
            presum_map[sumi] = presum_map.get(sumi, 0) + 1
        return count

if __name__ == '__main__':
    s = Solution1()
    res = s.subarraySum([1,1,1], 2)
    print(res)
    assert res == 2