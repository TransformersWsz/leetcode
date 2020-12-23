'''
@File  : maximum-subarray.py
@Author: Swift
@Date  : 2020/12/23 23:19
@Link  : https://leetcode-cn.com/problems/maximum-subarray/
@Desc  : 53. 最大子序和
@Method: https://leetcode-cn.com/problems/maximum-subarray/solution/zui-da-zi-xu-he-by-leetcode-solution/
'''

class Solution:
    def maxSubArray(self, nums):
        dp = [0] * len(nums)
        dp[0] = nums[0]
        res = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            res = max(res, dp[i])
        return res