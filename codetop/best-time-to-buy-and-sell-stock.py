'''
@File  : best-time-to-buy-and-sell-stock.py
@Author: Swift
@Date  : 2020/12/22 14:51
@Link  : https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
@Desc  : 121. 买卖股票的最佳时机
@Method: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/121-mai-mai-gu-piao-de-zui-jia-shi-ji-by-leetcode-/
'''


class Solution:
    def maxProfit(self, prices):
        min_price = sum(prices)
        max_profit = 0
        for item in prices:
            if item < min_price:
                min_price = item
            else:
                max_profit = max(max_profit, item-min_price)
        return max_profit


if __name__ == '__main__':
    obj = Solution()
    prices = [7,6,4,3,1]
    res = obj.maxProfit(prices)
    print(res)