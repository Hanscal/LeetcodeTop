# -*- coding: utf-8 -*-

"""
@Time    : 2022/1/9 5:33 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from typing import List
"""
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

if __name__ == '__main__':
    s = Solution()
    res = s.merge([[1,3],[2,6],[8,10],[15,18]])
    print(res)
    assert res == [[1,6],[8,10],[15,18]]