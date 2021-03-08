# -*- coding: utf-8 -*-

"""
@File  : max-area-of-island.py
@Author: swift
@Date  : 2021/02/22 14:28
@Link  : https://leetcode-cn.com/problems/max-area-of-island/
@Desc  : 695. 岛屿的最大面积
@Method: dfs
"""


class Solution:
    def __init__(self):
        self.max_area = 0
        self.tmp = 0

    def dfs(self, grid, i, j):
        if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j] == 1:
            self.tmp += 1
            grid[i][j] = 0
            self.dfs(grid, i - 1, j)
            self.dfs(grid, i + 1, j)
            self.dfs(grid, i, j - 1)
            self.dfs(grid, i, j + 1)

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    self.dfs(grid, i, j)
                    self.max_area = max(self.max_area, self.tmp)
                    self.tmp = 0
        return self.max_area

