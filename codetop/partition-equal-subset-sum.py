'''
@File  : partition-equal-subset-sum.py
@Author: Swift
@Date  : 2021/4/28 19:02
@Link  : https://leetcode-cn.com/problems/partition-equal-subset-sum/
@Desc  : 416. 分割等和子集
@Method:
'''

class Solution:
    def canPartition(self, nums):
        total = sum(nums)
        half = total // 2
        length = len(nums)
        dp = [ [0]*(half+1) for _ in range(length) ]

        for i in range(length):
            for j in range(half+1):
                if i == 0:
                    if j >= nums[i]:
                        dp[0][j] = nums[i]
                else:
                    if j >= nums[i]:
                        dp[i][j] = max(dp[i-1][j], dp[i-1][j-nums[i]]+nums[i])
                    else:
                        dp[i][j] = dp[i-1][j]
        return dp[length-1][half] == half


if __name__ == '__main__':
    solution = Solution()
    nums = [1,5,11,5]
    res = solution.canPartition(nums)
    print(res)