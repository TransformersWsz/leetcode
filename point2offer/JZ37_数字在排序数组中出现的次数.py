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

    def test(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            m = (low + high) // 2
            if nums[m] <= target:
                low = m + 1
            else:
                high = m - 1
        return low



if __name__ == '__main__':
    solution = Solution()
    data = [1,1,1,1,1, 2,3,3,3,9]
    k = 3
    res = solution.search(data, 1)
    print(res)