# -*- coding: utf-8 -*-

"""
@Time    : 2021/12/20 2:32 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from typing import List

"""
给定一个非负整数数组 nums 和一个整数 m ，你需要将这个数组分成 m 个非空的连续子数组。
设计一个算法使得这 m 个子数组各自和的最大值最小。
"""

# 贪心， 二分查找，动态规划（该方法未用）
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left, right = max(nums), sum(nums)
        while left < right: #当left == right的时候就终止查找，返回任意一个
            mid = (left + right) // 2
            # 找到施以查找的变量，测试中点是大还是小
            sums, cnt = 0, 1 # sums表示当前数组的和, cnt表示使用该mid我们会得到几个数组
            for i in nums:
                if sums + i > mid: # 如果当前数组已经超过mid，要停止这个数组
                    cnt += 1 # 一经达到就重新分组,得到的数组数量+1
                    sums = i # 这个数变为下个数组的开头
                else:
                    sums += i

            # 这里有一个注意点，如果cnt已经等于m了, 但此时如果left不等于right，范围还是会继续收敛的，
            # 且取的是左半边，目的是让我们能最终找到一个确切的值，这个值恰好就是取得了最大值的那个数组的和
            # (因为小于这个和的话，就不能通过cnt=m的测试；而大于这个m的话，即使通过了cnt=m的测试，直到我们找到的就是这个和)。

            if cnt <= m: # 数组总数是否<=m, 小于等于的话说明mid太大，二分查找取左边
                right = mid
            else:
                left = mid + 1
        return left

"""
left, right = max(nums),sum(nums)
while left < right:
    mid = (left + right) // 2
    if #排除右侧的条件:
        right = mid
    else:
        left = mid + 1
return left
"""

if __name__ == '__main__':
    s = Solution()
    res = s.splitArray([7,2,5,10,8], 2)
    print(res)
    assert res == 18