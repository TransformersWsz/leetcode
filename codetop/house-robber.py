'''
@File  : house-robber.py
@Author: Swift
@Date  : 2021/4/25 18:35
@Link  : https://leetcode-cn.com/problems/house-robber/
@Desc  : 198. 打家劫舍
@Method: 
'''


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        length = len(nums)
        dp = [ [0]*2 for _ in range(length+1) ]
        dp[1][0] = 0
        dp[1][1] = nums[0]
        for i in range(2, length+1):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            dp[i][1] = dp[i-1][0] + nums[i-1]
        return max(dp[length][0], dp[length][1])


if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,3,1]
    res = solution.rob(nums)
    print(res)
