'''
@File  : ones-and-zeroes.py
@Author: Swift
@Date  : 2020/12/4 23:43
@Link  : https://leetcode-cn.com/problems/ones-and-zeroes/
@Desc  : 一和零
@Method: 
'''

import collections

class Solution:

    def init_arr(self, length, m, n):
        arr = []
        for i in range(length):
            tmp_i = []
            for j in range(m):
                tmp_j = [0] * n
                tmp_i.append(tmp_j)
            arr.append(tmp_i)
        return arr

    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = self.init_arr(len(strs)+1, m+1, n+1)
        for i in range(1, len(strs)+1):
            for j in range(m+1):
                for k in range(n+1):
                    count = collections.Counter(strs[i-1])
                    if count['0'] > j or count['1'] > k:
                        dp[i][j][k] = dp[i-1][j][k]
                    else:
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-count['0']][k-count['1']]+1)
        return dp[len(strs)][m][n]


if __name__ == '__main__':
    obj = Solution()
    strs = ["10", "1", "0"]
    m = 1
    n = 1
    res = obj.findMaxForm(strs, m, n)
    print(res)
