#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/26 12:20 AM
# @Author  : Swift
# @File    : interleaving-string.py
# @Brief   : 97. 交错字符串
# @Method  : https://leetcode-cn.com/problems/interleaving-string/solution/lei-si-lu-jing-wen-ti-zhao-zhun-zhuang-tai-fang-ch/

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        if l1 + l2 != l3:
            return False
        dp = [[False] * (l2 + 1) for _ in range(l1 + 1)]
        dp[0][0] = True
        for j in range(1, l2 + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, l1 + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                up = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                left = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                dp[i][j] = up or left
        return dp[-1][-1]