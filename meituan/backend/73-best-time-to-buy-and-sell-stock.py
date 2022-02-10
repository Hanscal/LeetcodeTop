# -*- coding: utf-8 -*-

"""
@Time    : 2022/2/10 4:15 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
from typing import List

"""
给定一个数组 prices ，它的第i 个元素prices[i] 表示一支给定股票第 i 天的价格。
你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
"""

# 动态规划，第i的位置代表之前的最大利润
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        inf = int(1e9)
        minprice = inf
        maxprofit = 0
        for price in prices:
            maxprofit = max(price - minprice, maxprofit)
            minprice = min(price, minprice)
        return maxprofit




if __name__ == '__main__':
    s = Solution()
    res = s.maxProfit([7,1,5,3,6,4])
    print(res)
    assert res == 5