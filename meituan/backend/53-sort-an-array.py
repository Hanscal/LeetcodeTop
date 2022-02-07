# -*- coding: utf-8 -*-

"""
@Time    : 2022/2/7 12:44 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from typing import List
import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        def QuickSort(left, right):
            if left >= right: return nums
            # 加入随机性，更快
            index = random.randint(left, right)
            pivot = nums[index]
            nums[index], nums[left] = nums[left], nums[index]
            i, j = left, right
            # 交换列表中的元素
            while i < j:
                while i < j and nums[j] > pivot:
                    j -= 1
                nums[i] = nums[j]
                while i < j and nums[i] <= pivot:
                    i += 1
                nums[j] = nums[i]
            nums[i] = pivot
            QuickSort(left, i-1)
            QuickSort(i+1, right)
            return nums
        return QuickSort(0, n-1)

if __name__ == '__main__':
    s = Solution()
    res = s.sortArray([5,2,3,1])
    print(res)
    assert res == [1,2,3,5]