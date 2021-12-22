# -*- coding: utf-8 -*-

"""
@Time    : 2021/12/22 11:55 上午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""

from typing import List

"""给你一个包含 n 个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，使得a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。
"""

# 排序 + 双指针
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 存储结果列表
        res_list = []
        # 对nums列表进行排序，无返回值，排序直接改变nums顺序
        nums.sort()
        for i in range(len(nums)):
            # 如果排序后第一个数都大于0，则跳出循环，不可能有为0的三数之和
            if nums[i] > 0:
                break
            # 排序后相邻两数如果相等，则跳出当前循环继续下一次循环，相同的数只需要计算一次
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 记录i的下一个位置
            j = i + 1
            # 最后一个元素的位置
            k = len(nums) - 1
            while j < k:
                # 判断三数之和是否为0
                if nums[j] + nums[k] == -nums[i]:
                    # 把结果加入数组中
                    res_list.append([nums[i], nums[j], nums[k]])
                    # 判断j相邻元素是否相等，有的话跳过这个
                    while j < k and nums[j] == nums[j + 1]: j += 1
                    # 判断后面k的相邻元素是否相等，是的话跳过
                    while j < k and nums[k] == nums[k - 1]: k -= 1
                    # 没有相等则j+1，k-1，缩小范围
                    j += 1
                    k -= 1
                # 小于-nums[i]的话还能往后取
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1
                else:
                    k -= 1

        return res_list

if __name__ == '__main__':
    s = Solution()
    res = s.threeSum([-1,0,1,2,-1,-4])
    print(res)
    assert res == [[-1,-1,2],[-1,0,1]]