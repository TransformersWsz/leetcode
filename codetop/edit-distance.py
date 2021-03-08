'''
@File  : edit-distance.py
@Author: Swift
@Date  : 2021/3/8 16:13
@Link  : https://leetcode-cn.com/problems/edit-distance/
@Desc  : 72. 编辑距离
@Method: https://leetcode-cn.com/problems/edit-distance/solution/edit-distance-by-ikaruga/
'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        dp = [ [0]*(l2+1) for _ in range(l1+1) ]
        for col in range(1, l2+1):
            dp[0][col] = col
        for row in range(1, l1+1):
            dp[row][0] = row

        for row in range(1, l1+1):
            for col in range(1, l2+1):
                dp[row][col] = min(dp[row][col-1]+1,
                                   dp[row-1][col]+1,
                                   dp[row-1][col-1]+1)
                if word1[row-1] == word2[col-1]:
                    dp[row][col] = min(dp[row][col - 1] + 1,
                                       dp[row - 1][col] + 1,
                                       dp[row - 1][col - 1])
        return dp[l1][l2]




if __name__ == '__main__':
    solution = Solution()
    word1 = "intention"
    word2 = "execution"
    res = solution.minDistance(word1, word2)
    print(res)