# -*- coding: utf-8 -*-

"""
@Time    : 2021/12/23 4:25 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from typing import List

"""输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。"""
# 类似于快排的思想，不同的地方是在于每一趟

# 这个方法的时间复杂度比较高
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k >= len(arr): return arr

        # 需要原地进行交换
        def quick_sort(l, r):
            i, j = l, r
            while i < j:
                while i < j and arr[j] >= arr[l]: j -= 1
                while i < j and arr[i] <= arr[l]: i += 1
                arr[i], arr[j] = arr[j], arr[i]
            arr[l], arr[i] = arr[i], arr[l]
            if k < i: return quick_sort(l, i - 1)
            if k > i: return quick_sort(i + 1, r)
            return arr[:k]

        return quick_sort(0, len(arr) - 1)

class Solution1:
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
    s = Solution1()
    res = s.getLeastNumbers([3,2,1], k=2)
    print(res)
    assert set(res) == {1,2}