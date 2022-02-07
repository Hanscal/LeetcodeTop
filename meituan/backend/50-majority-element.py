# -*- coding: utf-8 -*-

"""
@Time    : 2022/2/7 11:40 上午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from typing import List

"""
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于n/2的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。
"""

# 先排序，取出n/2的元素
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        Qsort().quick_sort(nums, 0, len(nums)-1)
        # nums.sort(key=lambda x: x)
        return nums[len(nums)//2]

class Qsort(object):
    # 分解，递归，合并
    def quick_sort(self, lists, i, j):
        if i >= j:
            return lists
        pivot = lists[i]
        low = i
        high = j
        while i < j:
            while i < j and lists[j] >= pivot:
                j -= 1
            lists[i] = lists[j]
            while i < j and lists[i] <= pivot:
                i += 1
            lists[j] = lists[i]
        lists[j] = pivot
        self.quick_sort(lists, low, i - 1)
        self.quick_sort(lists, i + 1, high)
        return lists

if __name__ == '__main__':
    s = Solution()
    res = s.majorityElement([3,2,3])
    print(res)
    assert res == 3