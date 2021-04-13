'''
@File  : restore_ip_addresses.py
@Author: Swift
@Date  : 2021/4/13 17:26
@Link  : https://leetcode-cn.com/problems/restore-ip-addresses/
@Desc  : 93. 复原 IP 地址
@Method: 
'''

class Solution:
    def __init__(self):
        self.res = []

    def isleagal(self, substr):
        if substr[0] == '0' and len(substr) != 1:
            return False
        if substr.isdigit() and int(substr) <= 255:
            return True
        return False

    def dfs(self, s, idx, temp):
        if len(temp) > 4:
            return
        if idx >= len(s):
            if len(temp) == 4:
                self.res.append(".".join(temp))
        else:
            for l in range(1, 4):
                substr = s[idx:idx+l]
                if self.isleagal(substr) and idx+l <= len(s):
                    self.dfs(s, idx+l, temp + [s[idx: idx+l]])

    def restoreIpAddresses(self, s: str):
        self.dfs(s, 0, [])
        return self.res


if __name__ == '__main__':
    solution = Solution()
    s = "010010"
    res = solution.restoreIpAddresses(s)
    print(res)