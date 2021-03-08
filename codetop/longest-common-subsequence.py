# -*- coding: utf-8 -*-

"""
@File  : longest-common-subsequence.py
@Author: swift
@Date  : 2021/02/26 1:59
@Link  : https://leetcode-cn.com/problems/longest-common-subsequence/
@Desc  : 1143. 最长公共子序列
@Method: 
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        length1 = len(text1)
        length2 = len(text2)
        dp = [ [0]*(length2+1) for _ in range(length1+1) ]
        for i in range(1, length1+1):
            for j in range(1, length2+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[length1][length2]


if __name__ == '__main__':
    solution = Solution()
    text1 = "abcde"
    text2 = "ace"
    res = solution.longestCommonSubsequence(text1, text2)
    print(res)