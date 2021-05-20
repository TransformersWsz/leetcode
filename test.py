
from typing import List


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



if __name__ == '__main__':
    solution = Solution()
    triangle = [[-10]]
    res = solution.minimumTotal(triangle)
    print(res)