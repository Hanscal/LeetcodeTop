# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/14 6:53 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from typing import List

"""给定一个n个元素有序的（升序）整型数组nums 和一个目标值target ，
写一个函数搜索nums中的 target，如果目标值存在返回下标，否则返回 -1。
"""

# 二分查找
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (high - low) // 2 + low
            num = nums[mid]
            if num == target:
                return mid
            elif num > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1


if __name__ == '__main__':
    s = Solution()
    res = s.search(nums = [-1,0,3,5,9,12], target = 9)
    print(res)
    assert res == 4