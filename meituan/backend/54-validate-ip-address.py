# -*- coding: utf-8 -*-

"""
@Time    : 2022/2/7 12:54 下午
@Author  : hcai
@Email   : hua.cai@unidt.com
"""

"""
编写一个函数来验证输入的字符串是否是有效的 IPv4 或IPv6 地址。

如果是有效的 IPv4 地址，返回 "IPv4" ；
如果是有效的 IPv6 地址，返回 "IPv6" ；
如果不是上述类型的 IP 地址，返回 "Neither" 。
IPv4地址由十进制数和点来表示，每个地址包含 4 个十进制数，其范围为0 -255，用(".")分割。比如，172.16.254.1；

同时，IPv4 地址内的数不会以 0 开头。比如，地址172.16.254.01 是不合法的。

IPv6地址由 8 组 16 进制的数字来表示，每组表示16 比特。这些组数字通过 (":")分割。比如,2001:0db8:85a3:0000:0000:8a2e:0370:7334 是一个有效的地址。
而且，我们可以加入一些以 0 开头的数字，字母可以使用大写，也可以是小写。所以，2001:db8:85a3:0:0:8A2E:0370:7334 也是一个有效的 IPv6 address地址(即，忽略 0 开头，忽略大小写)。

然而，我们不能因为某个组的值为 0，而使用一个空的组，以至于出现 (::) 的情况。比如，2001:0db8:85a3::8A2E:0370:7334 是无效的 IPv6 地址。

同时，在 IPv6 地址中，多余的 0 也是不被允许的。比如，02001:0db8:85a3:0000:0000:8a2e:0370:7334 是无效的。
"""

# 分治法
class Solution:
    def validate_IPv4(self, IP: str) -> str:
        nums = IP.split('.')
        for x in nums:
            # Validate integer in range (0, 255):
            # 1. length of chunk is between 1 and 3
            if len(x) == 0 or len(x) > 3:
                return "Neither"
            # 2. no extra leading zeros
            # 3. only digits are allowed
            # 4. less than 255
            if x[0] == '0' and len(x) != 1 or not x.isdigit() or int(x) > 255:
                return "Neither"
        return "IPv4"

    def validate_IPv6(self, IP: str) -> str:
        nums = IP.split(':')
        hexdigits = '0123456789abcdefABCDEF'
        for x in nums:
            # Validate hexadecimal in range (0, 2**16):
            # 1. at least one and not more than 4 hexdigits in one chunk
            # 2. only hexdigits are allowed: 0-9, a-f, A-F
            if len(x) == 0 or len(x) > 4 or not all(c in hexdigits for c in x):
                return "Neither"
        return "IPv6"

    def validIPAddress(self, queryIP: str) -> str:
        if queryIP.count('.') == 3:
            return self.validate_IPv4(queryIP)
        elif queryIP.count(':') == 7:
            return self.validate_IPv6(queryIP)
        else:
            return "Neither"


if __name__ == '__main__':
    s = Solution()
    res = s.validIPAddress("172.16.254.1")
    print(res)
    assert res == 'IPv4'