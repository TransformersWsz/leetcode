# -*- coding: utf-8 -*-

"""
@File  : subarray-sum-equals-k.py
@Author: swift
@Date  : 2021/02/27 0:39
@Link  : https://leetcode-cn.com/problems/subarray-sum-equals-k/
@Desc  : 560. 和为K的子数组
@Method: https://leetcode-cn.com/problems/subarray-sum-equals-k/solution/he-wei-kde-zi-shu-zu-by-leetcode-solution/
"""


class Solution:
    def subarraySum(self, nums, k: int) -> int:
        count = 0
        d = {}
        d[0] = 1
        accum = 0
        for item in nums:
            accum +=item
            if d.get(accum-k):
                count += d[accum-k]
            d[accum] = d.get(accum, 0) + 1
        return count


if __name__ == '__main__':
    nums = [1,2,3]
    k = 3
    solution = Solution()
    res = solution.subarraySum(nums, k)
    print(res)