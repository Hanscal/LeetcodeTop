# -*- coding: utf-8 -*-

"""
@Time    : 2022/2/10 4:51 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""

"""
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行Z 字形排列。

比如输入字符串为 "PAYPALISHIRING"行数为 3 时，排列如下：

P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"
"""

#
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        # 初始化
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1: # 到达边界
                flag = -flag # 控制方向
            i += flag
        return "".join(res)


if __name__ == '__main__':
    s = Solution()
    res = s.convert(s = "PAYPALISHIRING", numRows = 3)
    print(res)
    assert res == "PAHNAPLSIIGYIR"
