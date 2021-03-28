'''
@File  : last-stone-weight-ii.py
@Author: Swift
@Date  : 2021/3/28 14:59
@Link  : https://leetcode-cn.com/problems/last-stone-weight-ii/
@Desc  : 1049. 最后一块石头的重量 II
@Method: https://leetcode-cn.com/problems/last-stone-weight-ii/solution/qing-xi-jian-dan-de-ti-jie-by-ji-qi-ren-h8mpv/
'''
import math

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        capacity = int(math.floor(total/2))
        dp = [ [0]*(capacity+1) for _ in range(len(stones)+1) ]
        for i in range(1, len(stones)+1):
            for j in range(capacity+1):
                if j < stones[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-stones[i-1]]+stones[i-1])
        return total - 2*dp[len(stones)][capacity]