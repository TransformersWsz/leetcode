'''
@File  : best-time-to-buy-and-sell-stock-ii.py
@Author: Swift
@Date  : 2021/4/11 23:08
@Link  : https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
@Desc  : 122. 买卖股票的最佳时机 II
@Method: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/solution/mai-mai-gu-piao-de-zui-jia-shi-ji-ii-by-leetcode-s/
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        dp = [[0]*2 for _ in range(length)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, length):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
        return dp[length-1][0]