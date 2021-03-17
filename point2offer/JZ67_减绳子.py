'''
@File  : JZ67_减绳子.py
@Author: Swift
@Date  : 2021/3/17 16:12
@Link  : https://www.nowcoder.com/practice/57d85990ba5b440ab888fc72b0751bf8?tpId=13&tqId=33257&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1，m<=n），每段绳子的长度记为k[1],...,k[m]。请问k[1]x...xk[m]可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
@Method: 
'''

# -*- coding:utf-8 -*-
class Solution:
    def cutRope(self, number):
        # write code here
        dp = [1] * (number)
        res = 1
        for i in range(1, number):
            for j in range(i-1, 0, -1):
                dp[i] = max(dp[i], dp[j]*(i-j)*(number-i))
                res = max(res, dp[i])
        return res


if __name__ == '__main__':
    solution = Solution()
    res = solution.cutRope(8)
    print(res)