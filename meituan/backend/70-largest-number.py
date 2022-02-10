# -*- coding: utf-8 -*-

"""
@Time    : 2022/2/10 3:31 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from typing import List
import functools

"""
给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。

注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。"""

# 贪心解法
# 对于 numsnums 中的任意两个值 a和 b，我们无法直接从常规角度上确定其大小/先后关系。
# 但我们可以根据「结果」来决定 a 和 b 的排序关系：
# 如果拼接结果 ab 要比 ba 好，那么我们会认为 a 应该放在 b 前面。
# 另外，注意我们需要处理前导零（最多保留一位）。

# 利用Python3自定义cmp_to_key函数，传入两个参数(x,y)对应于(self,other),这里的self表示当前的数，而other是前面已经出现比较过的对象。
# 比如arr=[3,32]，此时self为32，other为3，即x=32,y=3,这里与惯性思维是相反的.
# 示例：x=32,y=3,或者说y为数组前面的数，x为数组后面的数。要使得构造的数更大，需要满足条件：前面的数+后面的数>后面的数+前面的数，即y+x>x+y返回1成立，
# 即332>323成立，此时3出现在32前面


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = map(str, nums)

        def cmp(a, b):
            if a + b == b + a:
                return 0
            elif a + b > b + a:
                return 1
            else:
                return -1

        strs = sorted(strs, key=functools.cmp_to_key(cmp), reverse=True)
        return ''.join(strs) if strs[0] != '0' else '0' # 排序后处于第一个位置的值为0，说明后面的数都是0

if __name__ == '__main__':
    s = Solution()
    res = s.largestNumber([3,30,34,5,9])
    print(res)
    assert res == "9534330"