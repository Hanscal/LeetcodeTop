# -*- coding: utf-8 -*-

"""
@Time    : 2022/2/7 12:56 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""

"""
在一个数组中，每一个数左边比当前数小的数累加起来，叫做这个数组的小和。求一个数组的小和。

例子：
[1,3,4,2,5]
1左边比1小的数，没有；
3左边比3小的数，1；
4左边比4小的数，1、3；
2左边比2小的数，1；
5左边比5小的数，1、3、4、2；
所以小和为1+1+3+1+1+3+4+2=16
要求时间复杂度O(NlogN)，空间复杂度O(N)
"""

class Solution(object):
    def merge(self, nums, left, middle, right):
        i, j = left, middle + 1
        total = 0
        replace = []
        while i <= middle and j <= right:
            if nums[i] <= nums[j]:
                total += nums[i] * (right - j + 1)
                replace.append(nums[i])
                i += 1
            else:
                replace.append(nums[j])
                j += 1
        if i <= middle:
            replace.extend(nums[i:middle + 1])
        if j <= right:
            replace.extend(nums[j:right + 1])
        nums[left:right + 1] = replace
        return total

    def mergesort(self, nums, left, right):
        if left >= right:
            return 0
        middle = (left + right) // 2
        left_number = self.mergesort(nums, left, middle)
        right_number = self.mergesort(nums, middle + 1, right)
        number = self.merge(nums, left, middle, right)
        return number + left_number + right_number

    def min_sum(self, number_list):
        number = self.mergesort(number_list, 0, len(number_list) - 1)
        return number

if __name__ == '__main__':
    s = Solution()
    res = s.min_sum([1,3,4,2,5])
    print(res)
    assert res == 16