# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/19 1:27 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from typing import List

"""输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。"""

# quick-sort先排序
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if not arr or k <= 0: return []
        if len(arr) <= k: return arr

        self.quick_sort(arr, 0, len(arr) - 1)
        return arr[:k]

    @staticmethod
    def swap(nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def partition(self, nums, left, right):
        pivot = left
        i = j = pivot + 1

        while j <= right:
            if nums[j] <= nums[pivot]:
                self.swap(nums, i, j)
                i += 1
            j += 1
        self.swap(nums, pivot, i - 1)
        return i - 1

    def quick_sort(self, nums, left, right):
        if left < right:
            pivot = self.partition(nums, left, right)
            self.quick_sort(nums, left, pivot - 1)
            self.quick_sort(nums, pivot + 1, right)

if __name__ == '__main__':
    s = Solution()
    res = s.getLeastNumbers(arr = [3,2,1], k = 2)
    print(res)
    assert res == [1,2]