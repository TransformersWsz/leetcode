'''
@File  : target_sum.py
@Author: Swift
@Date  : 2021/5/5 20:45
@Link  : https://leetcode-cn.com/problems/target-sum/
@Desc  : 494. 目标和
@Method: https://leetcode-cn.com/problems/target-sum/solution/yi-tao-kuang-jia-jie-jue-bei-bao-wen-ti-58wvk/
'''

from typing import List


class Solution:

    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        total = sum(nums)
        if total < abs(S) or (total+S)%2==1:
            return 0
        target = (total+S) // 2
        dp = [0]*(target+1)
        dp[0] = 1
        for item in nums:
            for i in range(target, item-1, -1):
                dp[i] += dp[i-item]
        return dp[target]


if __name__ == '__main__':
    solution = Solution()
    nums = [100]
    S = -200
    res = solution.findTargetSumWays(nums, S)
    print(res)
