# -*- coding: utf-8 -*-

"""
@Time    : 2021/12/11 10:17 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from typing import List

"""
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
子数组 是数组中的一个连续部分。
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # base case
        dp = [0 for _ in range(len(nums))]
        ans = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            if dp[i] > ans:
                ans = dp[i]
        return ans

class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        # base case
        ans = nums[0]
        # 只与前一个状态有关，减少DPtable数量，节省空间
        current_sum = 0
        for i in range(len(nums)):
            current_sum = max(0, current_sum) + nums[i]
            ans = max(ans, current_sum)
        return ans

if __name__ == '__main__':
    s = Solution()
    res = s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print(res)
    assert res == 6