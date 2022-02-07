# -*- coding: utf-8 -*-

"""
@Time    : 2022/2/7 11:40 上午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
"""
0,1,···,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字（删除后从下一个数字开始计数）。求出这个圆圈里剩下的最后一个数字。

例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。
"""

# 动态规划
# 根据状态转移方程的递推特性，无需建立状态列表 dp，而使用一个变量 x 执行状态转移即可。
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        ans = 0
        for i in range(2, n+1):
            ans = (ans + m) % i
        return ans

if __name__ == '__main__':
    s = Solution()
    res = s.lastRemaining(5, 3)
    print(res)
    assert res == 3
