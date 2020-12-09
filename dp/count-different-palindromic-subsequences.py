'''
@File  : count-different-palindromic-subsequences.py
@Author: Swift
@Date  : 2020/12/9 17:26
@Link  : https://leetcode-cn.com/problems/count-different-palindromic-subsequences/
@Desc  : 730.统计不同回文子序列
@Method: https://blog.csdn.net/qq_41855420/article/details/89710028
'''


class Solution:

    def init_dp(self, length):
        dp = [[0]*length for _ in range(length)]
        for i in range(length):
            dp[i][i] = 1
        return dp

    def countPalindromicSubsequences(self, S):
        length = len(S)
        dp = self.init_dp(length)
        for i in range(1, length):
            for j in range(i-1, -1, -1):
                if S[j] == S[i]:  # 三种情况
                    left_idx = j+1
                    right_idx = i-1
                    while left_idx <= i and S[left_idx] != S[j]:
                        left_idx += 1

                    while right_idx >= j and S[right_idx] != S[i]:
                        right_idx -= 1

                    if left_idx > right_idx:
                        dp[j][i] = dp[j+1][i-1]*2 + 2
                    elif left_idx == right_idx:
                        dp[j][i] = dp[j+1][i-1]*2 + 1
                    else:
                        dp[j][i] = dp[j+1][i-1]*2 - dp[left_idx+1][right_idx-1]
                else:
                    dp[j][i] = dp[j][i-1] + dp[j+1][i] - dp[j+1][i-1]
        return dp[0][length-1] % 1000000007


if __name__ == '__main__':
    obj = Solution()
    S = 'bccb'
    num = obj.countPalindromicSubsequences(S)
    print(num)
