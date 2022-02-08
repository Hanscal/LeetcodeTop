# -*- coding: utf-8 -*-

"""
@Time    : 2022/2/8 1:16 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from typing import List

"""
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
"""

# 实际上，对于一个长度为 N 的数组，其中没有出现的最小正整数只能在 [1, N+1]中。
# 这是因为如果 [1, N]都出现了，那么答案是 N+1，否则答案是 [1, N]中没有出现的最小正整数。
# 这样一来，我们将所有在 [1, N]范围内的数放入哈希表，也可以得到最终的答案。

# 步骤
# 对数组进行遍历，对于遍历到的数 x，如果它在 [1, N]的范围内，那么就将数组中的第 x-1个位置（注意：数组下标从0开始）打上「标记」（负号）。
# 在遍历结束之后，如果所有的位置都被打上了标记，那么答案是 N+1，否则答案是最小的没有打上标记的位置加 1。

# 哈希表，数组
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        # 这步理解比较困难
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1

if __name__ == '__main__':
    s = Solution()
    res = s.firstMissingPositive([1,2,0])
    print(res)
    assert res == 3