'''
@File  : unique-paths-ii.py
@Author: Swift
@Date  : 2021/5/21 13:02
@Link  : https://leetcode-cn.com/problems/unique-paths-ii/
@Desc  : 63. 不同路径 II
@Method: 
'''


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        dp = [[0] * cols for _ in range(rows)]
        if obstacleGrid[0][0] == 1:
            dp[0][0] = 0
        else:
            dp[0][0] = 1
        for j in range(1, cols):
            if obstacleGrid[0][j] == 0:
                if obstacleGrid[0][j - 1] == 0:
                    dp[0][j] = dp[0][j - 1]

        for i in range(1, rows):
            if obstacleGrid[i][0] == 0:
                if obstacleGrid[i - 1][0] == 0:
                    dp[i][0] = dp[i - 1][0]

        for i in range(1, rows):
            for j in range(1, cols):
                if obstacleGrid[i][j] == 0:
                    if dp[i][j - 1] != 0 and dp[i - 1][j] != 0:
                        dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
                    else:
                        dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return dp[rows - 1][cols - 1]