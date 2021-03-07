# -*- coding: utf-8 -*-

"""
@File  : minimum-path-sum.py
@Author: swift
@Date  : 2021/02/10 23:23
@Link  : https://leetcode-cn.com/problems/minimum-path-sum/
@Desc  : 64. 最小路径和
@Method: 
"""


class Solution:
    def minPathSum(self, grid) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if i == 1:
                    dp[i][j] = dp[i][j-1] + grid[i-1][j-1]
                elif j == 1:
                    dp[i][j] = dp[i-1][j] + grid[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i - 1][j - 1]
        return dp[rows][cols]


if __name__ == '__main__':
    grid = [[1,2,3],[4,5,6]]
    solution = Solution()
    res = solution.minPathSum(grid)
    print(res)