# -*- coding: utf-8 -*-

"""
@Time    : 2022/2/8 12:59 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
import random
from typing import List
"""
给你一个整数数组 nums ，设计算法来打乱一个没有重复元素的数组。打乱后，数组的所有排列应该是 等可能 的。

实现 Solution class:
Solution(int[] nums) 使用整数数组 nums 初始化对象
int[] reset() 重设数组到它的初始状态并返回
int[] shuffle() 返回数组随机打乱后的结果

nums 中的所有元素都是 唯一的
"""

class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = nums.copy()

    def reset(self) -> List[int]:
        self.nums = self.original.copy()
        return self.nums

    def shuffle(self) -> List[int]:
        shuffled = [0] * len(self.nums)
        for i in range(len(self.nums)):
            j = random.randrange(len(self.nums))
            shuffled[i] = self.nums.pop(j)
        self.nums = shuffled
        return self.nums


if __name__ == '__main__':
    # Your Solution object will be instantiated and called as such:
    obj = Solution(nums=[1,2,3])
    param_1 = obj.shuffle()
    print(param_1)
    param_2 = obj.reset()
    print(param_2)
    assert param_2 == [1,2,3]
