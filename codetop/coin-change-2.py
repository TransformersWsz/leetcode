'''
@File  : coin-change-2.py
@Author: Swift
@Date  : 2021/4/29 17:52
@Link  : https://leetcode-cn.com/problems/coin-change-2/
@Desc  : 518. 零钱兑换 II
@Method: 
'''


class Solution:

    def change(self, amount: int, coins):
        dp = [0]*(amount+1)
        dp[0] = 1
        for val in coins:
            for i in range(val, amount+1):
                dp[i] += dp[i-val]
        return dp[amount]



if __name__ == '__main__':
    solution = Solution()
    coins = [1,5,2]
    amount = 5
    count = solution.change(amount, coins)
    print(count)