# -*- coding: utf-8 -*-

"""
@Time    : 2021/12/27 6:38 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from typing import List

"""
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
"""
# 动态规划，时间复杂度O(n*n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [] # 定义 dp[i] 为考虑前 i 个元素，以第 i 个数字结尾的最长上升子序列的长度
        if not nums:
            return 0
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)  # 状态转移过程，前面的最长长度+1
        return max(dp)

if __name__ == '__main__':
    s = Solution()
    res = s.lengthOfLIS([10,9,2,5,3,7,101,17,18,14])
    print(res)
    assert res == 5
