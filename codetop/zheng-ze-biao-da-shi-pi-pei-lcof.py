'''
@File  : zheng-ze-biao-da-shi-pi-pei-lcof.py
@Author: Swift
@Date  : 2021/3/14 22:49
@Link  : https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof/
@Desc  : 剑指 Offer 19. 正则表达式匹配
@Method: https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof/solution/zheng-ze-biao-da-shi-pi-pei-by-leetcode-s3jgn/
'''


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        def match(i, j):
            if i == 0:
                return False
            if p[j - 1] == ".":
                return True
            return s[i - 1] == p[j - 1]

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    dp[i][j] |= dp[i][j - 2]
                    if match(i, j - 1):
                        dp[i][j] |= dp[i - 1][j]
                else:
                    if match(i, j):
                        dp[i][j] |= dp[i - 1][j - 1]
        return dp[m][n]


if __name__ == '__main__':
    solution = Solution()
    s = "aa"
    p = "a*"
    res = solution.isMatch(s, p)
    print(res)