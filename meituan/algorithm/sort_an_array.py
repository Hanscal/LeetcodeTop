# -*- coding: utf-8 -*-

"""
@Time    : 2021/12/9 12:49 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""

"""给你一个整数数组 nums，请你将该数组升序排列。"""

from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        else:
            pivot = nums[0]  # pivot
            less_a = [i for i in nums[1:] if i <= pivot]
            big_a = [i for i in nums[1:] if i > pivot]
        return self.sortArray(less_a) + [pivot] + self.sortArray(big_a)

if __name__ == '__main__':
    s = Solution()
    nums = [5, 2, 3, 1]
    res = s.sortArray(nums)
    assert res == [1,2,3,5]
    nums = [5, 1, 1, 2, 0, 0]
    res = s.sortArray(nums)
    assert res == [0,0,1,1,2,5]