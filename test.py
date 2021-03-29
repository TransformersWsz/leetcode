'''
@File  : word-search.py
@Author: Swift
@Date  : 2021/3/8 22:57
@Link  : https://leetcode-cn.com/problems/word-search/
@Desc  : 79. 单词搜索
@Method: https://leetcode-cn.com/problems/word-search/solution/dan-ci-sou-suo-by-leetcode-solution/
'''

# -*- coding:utf-8 -*-
class Solution:
    def nolessthan(self, nums, target):
        low = 0
        high = len(nums) - 1
        res = -1
        while low <= high:
            mid = (low+high) // 2
            if target <= nums[mid]:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res

    def nogreaterthan(self, nums, target):
        low = 0
        high = len(nums) - 1

        res = len(nums)
        while low <= high:
            mid = (low+high) // 2
            if target < nums[mid]:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res-1

    def search(self, nums: [int], target: int) -> int:
        def helper(tar):
            low, high = 0, len(nums) - 1
            while low <= high:
                m = (low + high) // 2
                if nums[m] <= tar:
                    low = m + 1
                else:
                    high = m - 1
            return low
        right = helper(target)

        left = helper(target-1)
        print(right, left)
        return right-left

    def cpp(self, nums, target, lower):
        left = 0
        right = len(nums)-1
        ans = len(nums)
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] > target or (lower and nums[mid] >= target):
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
        return ans



if __name__ == '__main__':
    solution = Solution()
    data = [1, 3,3,3,4,5]
    k = -1
    # lidx = solution.cpp(data, k, True)
    # ridx = solution.cpp(data, k, False)-1


    res = solution.nolessthan(data, k)
    print(res)