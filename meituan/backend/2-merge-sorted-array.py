# -*- coding: utf-8 -*-

"""
@Time    : 2021/12/27 8:03 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from typing import List

"""
给你两个按 非递减顺序 排列的整数数组nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead. 如果不要求原地排序，可以利用额外m+n空间，并归排序中有设计
        """
        # 逆向双指针
        p1, p2 = m-1, n-1
        tail = m+n-1
        while p1>=0 or p2>=0:
            if p1 == -1:
                nums1[tail] = nums2[p2]
                p2 -= 1
            elif p2 == -1:
                nums1[tail] = nums1[p1]
                p1 -= 1
            elif nums1[p1] > nums2[p2]:
                nums1[tail] = nums1[p1]
                p1 -= 1
            else:
                nums1[tail] = nums2[p2]
                p2 -= 1
            tail -= 1
        return nums1

if __name__ == '__main__':
    s = Solution()
    res = s.merge(nums1 = [1,2,3, 0, 0, 0], m = 3, nums2 = [2,5,6], n = 3)
    print(res)
    assert res == [1,2,2,3,5,6]
