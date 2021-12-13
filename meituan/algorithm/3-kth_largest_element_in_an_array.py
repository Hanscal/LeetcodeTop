# -*- coding: utf-8 -*-

"""
@Time    : 2021/12/9 2:29 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""

"""给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。"""
from typing import List

# 基于快排的思想实现,也可以用大根堆实现
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        while True:
            idx = self.partition(nums, l, r)
            if idx == k - 1:
                return nums[idx]
            elif idx < k - 1:
                l = idx + 1
            else:
                r = idx - 1

    # ----单向遍历
    def partition(self, nums: List[int], l: int, r: int) -> int:
        pivot = nums[l]
        idx = l
        for i in range(l + 1, r + 1):
            if nums[i] >= pivot:
                idx += 1
                nums[idx], nums[i] = nums[i], nums[idx]  # 自身的值发生变化
        nums[idx], nums[l] = nums[l], nums[idx]  # 自身的值发生变化，将最后idx的值放在第一位
        return idx


if __name__ == '__main__':
    s = Solution()
    prices = [-1, -2]
    res = s.findKthLargest(prices, k=2)
    assert res == -2
    prices = [3,2,3,1,2,4,5,5,6]
    res = s.findKthLargest(prices, k=4)
    assert res == 4
    prices = [3, 2, 3, 1, 2, 4, 5, 5, 6, 7, 7, 8, 2, 3, 1, 1, 1, 10, 11, 5, 6, 2, 4, 7, 8, 5, 6]
    res = s.findKthLargest(prices, k=20)
    assert res == 2
