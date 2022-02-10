# -*- coding: utf-8 -*-

"""
@Time    : 2022/2/10 4:15 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from typing import List

"""输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数在数组的前半部分，所有偶数在数组的后半部分。"""

class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        res = []
        cnt = 0
        for num in nums:
            if num % 2 == 1:
                res.insert(cnt, num)
                cnt += 1
            else:
                res.append(num)
        return res

if __name__ == '__main__':
    s = Solution()
    res = s.exchange([1,2,3,4])
    print(res)
    assert res == [1,3,2,4]