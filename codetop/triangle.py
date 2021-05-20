'''
@File  : triangle.py
@Author: Swift
@Date  : 2021/5/20 17:08
@Link  : https://leetcode-cn.com/problems/triangle/
@Desc  : 120. 三角形最小路径和
@Method: 
'''

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)
        cols = len(triangle[-1])
        dp = [ [float('inf')]*(cols+1) for _ in range(rows+1) ]
        dp[1][1] = triangle[0][0]
        for i in range(2, rows+1):
            for j in range(1, cols+1):
                if j <= len(triangle[i-1]):
                    if i-2 >= 0 and j-1 < len(triangle[i-2]):
                        dp[i][j] = dp[i-1][j] + triangle[i-1][j-1]
                    if i-2 >= 0 and j-2 >= 0:
                        dp[i][j] = min(dp[i][j], dp[i-1][j-1]+triangle[i-1][j-1])
        return min(dp[rows])