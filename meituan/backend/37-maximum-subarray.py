# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/17 1:12 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from typing import List

"""
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组 是数组中的一个连续部分。
"""

# 动态规划
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        sum = 0
        for num in nums:
            if sum > 0:
                sum += num
            else:
                sum = num
            ans = max(ans, sum)
        return ans

if __name__ == '__main__':
    s = Solution()
    res = s.maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4])
    print(res)
    assert res == 6