'''
@File  : maximum-product-subarray.py
@Author: Swift
@Date  : 2021/5/10 22:58
@Link  : https://leetcode-cn.com/problems/maximum-product-subarray/
@Desc  : 152. 乘积最大子数组
@Method: 
'''
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [[1] * 2 for _ in range(length)]
        dp[0][0] = nums[0]
        dp[0][1] = nums[0]
        res = max(dp[0])
        for i in range(1, length):
            dp[i][0] = max(nums[i], dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i])
            dp[i][1] = min(nums[i], dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i])
            res = max(res, max(dp[i]))
        return res


if __name__ == '__main__':
    solution = Solution()
    nums = [-2, 0, -1]
    res = solution.maxProduct(nums)
    print(res)
