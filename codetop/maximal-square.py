#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/15 12:57 AM
# @Author  : Swift
# @File    : maximal-square.py
# @Brief   : 221. 最大正方形
# @Method  : https://leetcode-cn.com/problems/maximal-square/solution/zui-da-zheng-fang-xing-by-leetcode-solution/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        area = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                    area = max(area, dp[i][j] * dp[i][j])
        return area