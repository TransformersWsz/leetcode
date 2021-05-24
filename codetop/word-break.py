'''
@File  : word-break.py
@Author: Swift
@Date  : 2021/5/24 15:13
@Link  : https://leetcode-cn.com/problems/word-break/
@Desc  : 139. 单词拆分
@Method: 
'''

class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        dp = [False]*(length+1)
        dp[0] = True
        for i in range(1, length+1):
            for j in range(0, i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        return dp[length]