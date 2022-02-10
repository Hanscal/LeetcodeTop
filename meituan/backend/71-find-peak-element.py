# -*- coding: utf-8 -*-

"""
@Time    : 2022/2/10 3:31 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from typing import List
"""
峰值元素是指其值严格大于左右相邻值的元素。

给你一个整数数组nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。

你可以假设nums[-1] = nums[n] = -∞ 。

你必须实现时间复杂度为 O(log n) 的算法来解决此问题。
"""
# 最大值位置也是满足的，O(n)时间复杂度

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        idx = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[idx]:
                idx = i
        return idx

class Solution1:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        # 辅助函数，输入下标 i，返回 nums[i] 的值
        # 方便处理 nums[-1] 以及 nums[n] 的边界情况
        def get(i: int) -> int:
            if i == -1 or i == n:
                return float('-inf')
            return nums[i]

        left, right, ans = 0, n - 1, -1
        while left <= right:
            mid = (left + right) // 2
            if get(mid - 1) < get(mid) > get(mid + 1):
                ans = mid
                break
            if get(mid) < get(mid + 1):
                left = mid + 1
            else:
                right = mid - 1

        return ans


if __name__ == '__main__':
    s = Solution()
    res = s.findPeakElement(nums = [1,2,3,1])
    print(res)
    assert res == 2
