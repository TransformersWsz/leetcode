'''
@File  : unique-paths.py
@Author: Swift
@Date  : 2020/1/5 17:43
@Link  : https://leetcode-cn.com/problems/unique-paths/
@Desc  : 62. 不同路径
@Method:
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [ [0]*m for _ in range(n) ]
        for col in range(0, m):
            dp[0][col] = 1
        for row in range(0, n):
            dp[row][0] = 1

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[n-1][m-1]
