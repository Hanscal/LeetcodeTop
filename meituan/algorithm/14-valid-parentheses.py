# -*- coding: utf-8 -*-

"""
@Time    : 2021/12/14 6:27 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""
"""给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串 s ，判断字符串是否有效。

有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。

"""

# 栈处理
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        str_map = {"{":"}","(":")", "[":"]"}
        for i in s:
            if i in ['{','(','[']:
                stack.append(i)
            elif i in ['}',')',']']:
                if not stack:
                    return False
                last = stack[-1]
                if str_map[last] == i:
                    stack = stack[:-1]
                else:
                    return False
        if len(stack)>0:
            return False
        else:
            return True

if __name__ == '__main__':
    s = Solution()
    res = s.isValid("(])")
    print(res)
    assert res == False