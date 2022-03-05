#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/17 12:18 AM
# @Author  : Swift
# @File    : sort-colors.py
# @Brief   : 75. 颜色分类
# @Method  : https://leetcode-cn.com/problems/sort-colors/solution/yan-se-fen-lei-by-leetcode-solution/

class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = p1 = 0
        length = len(nums)
        for i in range(length):
            if nums[i] == 1:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1
            elif nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                if p0 < p1:
                    nums[i], nums[p1] = nums[p1], nums[i]
                p0 += 1
                p1 += 1


if __name__ == "__main__":
    solution = Solution()
    nums = [2, 1, 1, 0, 0]
    solution.sortColors(nums)
    print(nums)