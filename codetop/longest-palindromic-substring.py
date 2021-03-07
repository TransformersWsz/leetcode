# -*- coding: utf-8 -*-

"""
@File  : longest-palindromic-substring.py
@Author: swift
@Date  : 2021/02/19 13:17
@Link  : https://leetcode-cn.com/problems/longest-palindromic-substring/
@Desc  : 5. 最长回文子串
@Method: 
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        dp = [[0] * length for _ in range(length)]
        for i in range(length):
            dp[i][i] = 1

        res = s[0]
        for i in range(1, length):
            for j in range(i - 1, -1, -1):
                if j == i - 1:
                    if s[i] == s[j]:
                        dp[j][i] = 1
                        if len(s[j:i + 1]) > len(res):
                            res = s[j:i + 1]
                else:
                    if s[i] == s[j]:
                        dp[j][i] = dp[j + 1][i - 1]
                        if dp[j][i]:
                            if len(s[j:i + 1]) > len(res):
                                res = s[j:i + 1]
        return res