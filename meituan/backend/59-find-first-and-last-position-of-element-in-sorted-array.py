# -*- coding: utf-8 -*-

"""
@Time    : 2022/2/8 11:40 上午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from typing import List

"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回[-1, -1]。

进阶：
你可以设计并实现时间复杂度为O(log n)的算法解决此问题吗？
"""

# 改进的二分查找
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def left_func(nums,target):
            n = len(nums)-1
            left = 0
            right = n
            while left <= right:
                mid = (left+right)//2
                if nums[mid] >= target:
                    right = mid-1
                if nums[mid] < target:
                    left = mid+1
            return left
        a = left_func(nums,target)
        b = left_func(nums,target+1)
        if a == len(nums) or nums[a] != target:
            return [-1,-1]
        else:
            return [a,b-1]

if __name__ == '__main__':
    s = Solution()
    res = s.searchRange([5,7,7,8,8,10], 8)
    print(res)
    assert res == [3,4]