'''
@File  : target-sum.py
@Author: Swift
@Date  : 2020/12/14 16:44
@Link  : https://leetcode-cn.com/problems/target-sum/
@Desc  : 494. 目标和
@Method: 
'''


class Solution:

    def dfs(self, nums, idx, tgt):
        if idx == len(nums):
            if tgt == 0:
                return 1
            else:
                return 0
        else:
            return self.dfs(nums, idx+1, tgt+nums[idx]) + self.dfs(nums, idx+1, tgt-nums[idx])

    def findTargetSumWays(self, nums, S):
        res = self.dfs(nums, 0, S)
        return res


if __name__ == '__main__':
    obj = Solution()
    nums = [14,23,35,48,10,39,34,40,36,45,11,14,41,6,4,17,42,22,0,35]
    S = 44
    res = obj.findTargetSumWays(nums, S)
    print(res)
