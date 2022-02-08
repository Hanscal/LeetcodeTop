# -*- coding: utf-8 -*-

"""
@Time    : 2022/2/8 1:16 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [] # 定义 dp[i] 为考虑前 i 个元素，以第 i 个数字结尾的最长上升子序列的长度
        if not nums:
            return 0
        for i in range(len(nums)):
            dp.append(1) # 可以看做为初始化
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)  # 状态转移过程，前面的最长长度+1
        return max(dp)

if __name__ == '__main__':
    s = Solution()
    res = s.lengthOfLIS([10,9,2,5,3,7,101,18])
    print(res)
    assert res == 4