# -*- coding: utf-8 -*-

"""
@File  : minimum-size-subarray-sum.py
@Author: swift
@Date  : 2021/02/26 1:24
@Link  : https://leetcode-cn.com/problems/minimum-size-subarray-sum/
@Desc  : 209. 长度最小的子数组
@Method: 
"""

class Solution:
    def minSubArrayLen(self, s: int, nums) -> int:
        accum = 0
        length = len(nums)
        i = 0
        j = 0
        res = length+1
        while i < length:
            accum += nums[i]
            while accum >= s:
                res = min(res, i-j+1)
                accum -= nums[j]
                j += 1
            i += 1

        return 0 if res==length+1 else res


if __name__ == '__main__':
    target = 15
    nums = [1, 2, 4, 3, 5]
    solution = Solution()
    res = solution.minSubArrayLen(target, nums)
    print(res)