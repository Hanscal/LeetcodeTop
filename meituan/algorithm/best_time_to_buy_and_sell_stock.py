# -*- coding: utf-8 -*-

"""
@Time    : 2021/12/9 1:57 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from typing import List

"""
给定一个数组 prices ，它的第i 个元素prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 用minProfit记录前面遍历的最小值，用maxProfit记录遍历到该位置的最大利润。（动态规划）
        maxprofit = 0
        minprofit = prices[0]
        for price in prices:
            maxprofit = max(price - minprofit, maxprofit)
            minprofit = min(price, minprofit)
        return maxprofit

if __name__ == '__main__':
    s = Solution()
    prices = [7, 6, 4, 3, 1]
    res = s.maxProfit(prices)
    assert res == 0
    prices = [7,1,5,3,6,4]
    res = s.maxProfit(prices)
    assert res == 5