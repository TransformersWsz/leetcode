# -*- coding: utf-8 -*-

"""
@File  : rotate-array.py
@Author: swift
@Date  : 2021/02/22 14:31
@Link  : https://leetcode-cn.com/problems/rotate-array/
@Desc  : 189. 旋转数组
@Method: https://leetcode-cn.com/problems/rotate-array/solution/xuan-zhuan-shu-zu-by-leetcode-solution-nipk/ (数组翻转）
"""


class Solution:

    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]



if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    k=3
    solution = Solution()
    solution.rotate(nums, k)
    print(nums)