# -*- coding: utf-8 -*-

"""
@Time    : 2021/12/29 3:12 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from typing import List

"""给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。"""
# 连续

# 动态规划，滑动窗口
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        dp = [0 for _ in range(n2+1)] # 降维优化，因为只依赖左上角的值
        res = 0
        for i in range(1, n1+1):
            for j in range(n2, 0, -1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[j] = dp[j - 1] + 1
                else:
                    dp[j] = 0
                res = max(res, dp[j])
        return res

if __name__ == '__main__':
    s = Solution()
    res = s.findLength([1,2,3,2,1], [3,2,1,4,7])
    print(res)
    assert res == 3