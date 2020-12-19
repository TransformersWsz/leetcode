'''
@File  : cheapest-flights-within-k-stops.py
@Author: Swift
@Date  : 2020/12/16 11:32
@Link  : https://leetcode-cn.com/problems/cheapest-flights-within-k-stops/
@Desc  : 787. K 站中转内最便宜的航班
@Method: 
'''

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        dp = [[0]*(K+1) for _ in range(n)]
        for k in range(K+1):
            for item in flights:
                if item[0] == src:
                    dp[item[1]][k] = min(dp)


if __name__ == '__main__':
    obj = Solution()
    n = 3
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 1
    res = obj.findCheapestPrice(3, flights, src, dst, k)
    print(res)