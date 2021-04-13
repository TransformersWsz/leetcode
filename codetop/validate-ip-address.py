'''
@File  : validate-ip-address.py
@Author: Swift
@Date  : 2021/4/13 17:07
@Link  : https://leetcode-cn.com/problems/validate-ip-address/
@Desc  : 468. 验证IP地址
@Method: https://leetcode-cn.com/problems/validate-ip-address/solution/yan-zheng-ip-di-zhi-by-leetcode/
'''


class Solution:
    def ipv4(self, IP):
        numbers = IP.split(".")
        for item in numbers:
            if len(item) == 0 or len(item) >= 4:
                return "Neither"
            if (item[0] == '0' and len(item) != 1) or not item.isdigit() or int(item) > 255:
                return "Neither"
        return "IPv4"

    def ipv6(self, IP):
        numbers = IP.split(":")
        s = "0123456789abcdefABCDEF"
        for item in numbers:
            if len(item) == 0 or len(item) >= 5:
                return "Neither"
            for c in item:
                if c not in s:
                    return "Neither"
        return "IPv6"

    def validIPAddress(self, IP: str) -> str:
        if IP.count(".") == 3:
            return self.ipv4(IP)
        elif IP.count(":") == 7:
            return self.ipv6(IP)
        else:
            return "Neither"