# -*- coding: utf-8 -*-

"""
@Time    : 2021/12/10 11:23 上午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from typing import List

"""
给定一个未排序的整数数组 nums ，找出数字连续的最长序列的长度,

&&（不要求序列元素在原数组中连续）&&

请你设计并实现时间复杂度为O(n) 的算法解决此问题。
"""

# 数组，哈希表
"""用哈希表存储每个端点值对应连续区间的长度
若数已在哈希表中：跳过不做处理
若是新数加入：
取出其左右相邻数已有的连续区间长度 left 和 right
计算当前数的区间长度为：cur_length = left + right + 1
根据 cur_length 更新最大长度 max_length 的值
更新区间两端点的长度值
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        hash_dict = dict()
        for num in nums:
            # 新进来哈希表一个数
            if num not in hash_dict:
                # 获取当前数的最左边连续长度,没有的话就更新为0
                left = hash_dict.get(num-1,0)
                # 同理获取右边的数
                right = hash_dict.get(num+1,0)
                """不用担心左边和右边没有的情况
                因为没有的话就是left或者right0
                并不改变什么
                """
                # 把当前数加入哈希表，代表当前数字出现过
                hash_dict[num] = 1
                # 更新长度
                length = left+1+right
                res = max(res,length)
                # 更新最左端点的值，如果left=n存在，那么证明当前数的前n个都存在哈希表中
                hash_dict[num-left] = length
                # 更新最右端点的值，如果right=n存在，那么证明当前数的后n个都存在哈希表中
                hash_dict[num+right] = length
                # 此时 【num-left，num-right】范围的值都连续存在哈希表中了
                # 即使left或者right=0都不影响结果
        return res

class Solution1:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            # 只有当这个数是连续序列的第一个数才会进入循环，分连续区域找最大
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak


if __name__ == '__main__':
    s = Solution()
    nums = [0,3,7,2,5,8,4,6,0,1]
    res = s.longestConsecutive(nums)
    print(res)
    assert res == 9