'''
@File  : coin-change.py
@Author: Swift
@Date  : 2021/4/28 0:05
@Link  : https://leetcode-cn.com/problems/coin-change/
@Desc  : 322. 零钱兑换
@Method: 
'''


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [0] + [float('inf')]*amount
        for val in coins:
            for i in range(val, amount+1):
                dp[i] = min(dp[i], dp[i-val]+1)
        return -1 if dp[amount] == float('inf') else dp[amount]