'''
@File  : jian-sheng-zi-ii-lcof.py
@Author: Swift
@Date  : 2020/12/10 11:36
@Link  : https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof/
@Desc  : 剪绳子 II
@Method: https://leetcode-cn.com/problems/integer-break/solution/zheng-shu-chai-fen-by-leetcode-solution/
'''

class Solution:
    def cuttingRope(self, n):
        dp = [0] * n
        for i in range(1, n):
            for j in range(i-1, -1, -1):
                dp[i] = max(dp[i], (i-j)*dp[j], (i-j)*(j+1))
        return dp[n-1] % 1000000007


if __name__ == '__main__':
    obj = Solution()
    n = 54
    res = obj.cuttingRope(n)
    print(res)