# -*- coding: utf-8 -*-

"""
@Time    : 2021/12/12 10:20 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from typing import List


"""给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。"""
# 动态规划

"""
状态定义：dp[i][j] 以nums1[i-1]结尾的nums1和以nums2[j-1]结尾的nums2
状态转移 若nums1[i-1] == nums2[j-1] 则 dp[i][j] = dp[i-1][j-1] + 1
遍历过程中记录最大值
"""

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        len1, len2 = len(nums1) + 1, len(nums2) + 1
        dp = [[0] * (len1) for _ in range(len2)]
        ans = 0
        for i in range(1, len2):
            for j in range(1, len1):
                if nums2[i - 1] == nums1[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    ans = max(ans, dp[i][j])
        return ans

if __name__ == '__main__':
    s = Solution()
    res = s.findLength([1,2,3,2,1],[3,2,1,4,7])
    print(res)
    assert res == 3