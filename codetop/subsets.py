# -*- coding: utf-8 -*-

"""
@File  : subsets.py
@Author: swift
@Date  : 2021/02/27 0:09
@Link  : https://leetcode-cn.com/problems/subsets/
@Desc  : 78. 子集
@Method: https://leetcode-cn.com/problems/subsets/solution/hui-su-suan-fa-by-powcai-5/
"""

class Solution:
    def __init__(self):
        self.res = []

    def subsets(self, nums):
        res = []
        n = len(nums)
        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                helper(j + 1, tmp + [nums[j]])

        helper(0, [])
        return res

def test(self, nums):
        def back_trace(nums, start, tmp):
            self.res.append(tmp)
            for i in range(start, len(nums)):
                back_trace(nums, i + 1, tmp + [nums[i]])

        back_trace(nums, 0, [])
        return self.res


if __name__ == '__main__':
    nums = [1, 2, 3]
    solution = Solution()
    res = solution.subsets(nums)
    print(res)
