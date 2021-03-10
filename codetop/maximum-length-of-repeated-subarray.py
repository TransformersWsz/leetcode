'''
@File  : maximum-length-of-repeated-subarray.py
@Author: Swift
@Date  : 2021/3/10 13:57
@Link  : https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/
@Desc  : 718. 最长重复子数组
@Method: 
'''

class Solution:
    def findLength(self, A, B) -> int:
        if not A or not B:
            return 0
        lenA = len(A)
        lenB = len(B)
        dp = [ [0]*(lenB+1) for _ in range(lenA+1) ]
        res = 0
        for i in range(1, lenA+1):
            for j in range(1, lenB+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    res = max(res, dp[i][j])
        return res


if __name__ == '__main__':
    solution = Solution()
    A = [1,2,3,2,1]
    B = [3,2,1,4,7]
    res = solution.findLength(A, B)
    print(res)