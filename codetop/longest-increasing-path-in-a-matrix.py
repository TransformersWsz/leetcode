'''
@File  : longest-increasing-path-in-a-matrix
@Author: Swift
@Date  : 2021/7/1 17:36
@Link  : https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix/
@Desc  : 329. 矩阵中的最长递增路径
@Method: https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix/solution/ji-yi-hua-de-di-gui-sou-suo-by-lzx1997-v49k/
'''


class Solution:
    def dfs(self, i, j, matrix, dp):
        if dp[i][j] != -1:
            return dp[i][j]
        d = 1
        direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for (ox, oy) in direction:
            newx, newy = i+ox, j+oy
            if 0 <= newx < len(matrix) and 0 <= newy < len(matrix[0]) and matrix[newx][newy] > matrix[i][j]:
                d = max(d, self.dfs(newx, newy, matrix, dp)+1)
        dp[i][j] = d
        return d


    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [ [-1]*cols for _ in range(rows) ]
        res = 0
        for i in range(rows):
            for j in range(cols):
                if dp[i][j] == -1:
                    res = max(res, self.dfs(i, j, matrix, dp))
        return res
