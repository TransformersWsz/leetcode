'''
@File  : distinct-subsequences-ii.py
@Author: Swift
@Date  : 2020/12/14 11:02
@Link  : https://leetcode-cn.com/problems/distinct-subsequences-ii/
@Desc  : 940. 不同的子序列 II
@Method: https://leetcode-cn.com/problems/distinct-subsequences-ii/comments/
'''


class Solution:
    def distinctSubseqII(self, S: str) -> int:
        length = len(S)
        dp = [0] * (length)
        dp[0] = 1
        d = {}
        d[S[0]] = 0
        for i in range(1, length):
            if S[i] not in d:
                dp[i] = 2*dp[i-1] + 1
            else:
                dp[i] = 2*dp[i-1] - dp[d[S[i]]-1]
            d[S[i]] = i
        return dp[length-1]%1000000007


if __name__ == '__main__':
    obj = Solution()
    S = "abc"
    res = obj.distinctSubseqII(S)
    print(res)