'''
@File  : longest-increasing-subsequence.py
@Author: Swift
@Date  : 2020/12/6 21:24
@Link  : https://leetcode-cn.com/problems/longest-increasing-subsequence/
@Desc  : 最长上升子序列
@Method: 
'''


class Solution:
    def lengthOfLIS(self, nums):
        res = 0
        if len(nums) <= 1:
            res = len(nums)
        else:
            dp = [1] * len(nums)
            for i in range(1, len(nums)):
                for j in range(i):
                    if nums[i] > nums[j]:
                        dp[i] = max(dp[i], dp[j]+1)
                res = max(res, dp[i])
        return res


if __name__ == '__main__':
    obj = Solution()
    nums = [10,9,2,5,3,7,101,18]
    res = obj.lengthOfLIS(nums)
    print(res)