# -*- coding: utf-8 -*-

"""
@Time    : 2021/12/27 8:03 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from typing import List
import random

"""
给你一个整数数组 nums，请你将该数组升序排列。
"""

# 超出时间限制
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        else:
            pivot = nums[0]  # pivot
            less_a = [i for i in nums[1:] if i <= pivot]
            big_a = [i for i in nums[1:] if i > pivot]
        return self.sortArray(less_a) + [pivot] + self.sortArray(big_a)

class Solution1:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        def QuickSort(left, right):
            if left >= right: return nums
            index = random.randint(left, right) # 有个随机选择过程
            pivot = nums[index]
            nums[index], nums[left] = nums[left], nums[index]
            i, j = left, right
            while i < j:
                while i < j and nums[j] > pivot:
                    j -= 1
                nums[i] = nums[j]
                while i < j and nums[i] <= pivot:
                    i += 1
                nums[j] = nums[i]
            nums[i] = pivot
            QuickSort(left, i - 1)
            QuickSort(i + 1, right)
            return nums

        return QuickSort(0, n - 1)


if __name__ == '__main__':
    s = Solution1()
    res = s.sortArray([5,2,3,1])
    print(res)
    assert res == [1,2,3,5]
