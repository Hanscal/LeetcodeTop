# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/3 10:44 上午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from typing import List

"""
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(nums, left, right):
            pivot = nums[left]  # 初始化一个待比较数据
            i, j = left, right
            while (i < j):
                while (i < j and nums[j] >= pivot):  # 从后往前查找，直到找到一个比pivot更小的数
                    j -= 1
                nums[i] = nums[j]  # 将更小的数放入左边
                while (i < j and nums[i] <= pivot):  # 从前往后找，直到找到一个比pivot更大的数
                    i += 1
                nums[j] = nums[i]  # 将更大的数放入右边
            # 循环结束，i与j相等
            nums[i] = pivot  # 待比较数据放入最终位置
            return i  # 返回待比较数据最终位置

        def topk_split(nums, k, left, right):
            # 寻找到第k个数停止递归，使得nums数组中index左边是前k个小的数，index右边是后面n-k个大的数
            if (left < right):
                index = partition(nums, left, right)
                if index == k:
                    return
                elif index < k:
                    topk_split(nums, k, index + 1, right)
                else:
                    topk_split(nums, k, left, index - 1)

        # parttion是按从小到大划分的，如果让index左边为前n-k个小的数，则index右边为前k个大的数
        topk_split(nums, len(nums) - k, 0, len(nums) - 1)  # 把k换成len(nums)-k
        return nums[len(nums) - k]

if __name__ == '__main__':
    s = Solution()
    res = s.findKthLargest(nums = [3,2,1,5,6,4], k = 2)
    print(res)
    assert res == 5