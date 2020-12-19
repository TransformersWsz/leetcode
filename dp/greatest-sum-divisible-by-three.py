'''
@File  : greatest-sum-divisible-by-three.py
@Author: Swift
@Date  : 2020/12/16 10:47
@Link  : https://leetcode-cn.com/problems/greatest-sum-divisible-by-three/
@Desc  : 1262. 可被三整除的最大和
@Method: https://leetcode-cn.com/problems/greatest-sum-divisible-by-three/solution/dong-tai-gui-hua-yu-zhuang-tai-zhuan-yi-by-christm/
'''

class Solution:
    def maxSumDivThree(self, nums):
        length = len(nums)
        dp = [[0]*3 for _ in range(length+1)]
        dp[0][0] = 0
        dp[0][1] = -sum(nums)
        dp[0][2] = -sum(nums)

        for i in range(1, length+1):
            if nums[i-1] % 3 == 0:
                dp[i][0] = max(dp[i-1][0], dp[i-1][0] + nums[i-1])
                dp[i][1] = max(dp[i-1][1], dp[i-1][1] + nums[i-1])
                dp[i][2] = max(dp[i-1][2], dp[i-1][2] + nums[i-1])
            elif nums[i-1] % 3 == 1:
                dp[i][0] = max(dp[i-1][0], dp[i-1][2] + nums[i-1])
                dp[i][1] = max(dp[i-1][1], dp[i-1][0] + nums[i-1])
                dp[i][2] = max(dp[i-1][2], dp[i-1][1] + nums[i-1])
            else:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + nums[i-1])
                dp[i][1] = max(dp[i-1][1], dp[i-1][2] + nums[i-1])
                dp[i][2] = max(dp[i-1][2], dp[i-1][0] + nums[i-1])

        return dp[length][0]



if __name__ == '__main__':
    obj = Solution()
    nums = [2,6,2,2,7]
    res = obj.maxSumDivThree(nums)
    print(res)