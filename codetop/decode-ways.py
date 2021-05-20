'''
@File  : decode-ways.py
@Author: Swift
@Date  : 2021/5/20 16:29
@Link  : https://leetcode-cn.com/problems/decode-ways/
@Desc  : 91. 解码方法
@Method: 
'''

class Solution:
    def __init__(self):
        self.count = 0

    def isleagal(self, s):
        if len(s) >= 2 and s[0] == '0':
            return False
        if int(s) > 26 or int(s) == 0:
            return False
        return True

    def numDecodings(self, s: str) -> int:
        length = len(s)
        dp = [0]*(length+1)
        dp[0] = 1
        if s[0] != "0":
            dp[1] = 1
        for i in range(2, length+1):
            ones = s[i-1:i]
            twos = s[i-2:i]
            if self.isleagal(ones):
                dp[i] += dp[i-1]
            if self.isleagal(twos):
                dp[i] += dp[i-2]
        return dp[length]