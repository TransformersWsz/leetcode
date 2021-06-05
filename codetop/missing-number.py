#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/6 12:32 AM
# @Author  : Swift
# @File    : missing-number.py
# @Brief   : 268. 丢失的数字
# @Method  : https://leetcode-cn.com/problems/missing-number/solution/que-shi-shu-zi-by-leetcode/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        accum = length*(length+1)//2
        for item in nums:
            accum -= item
        return accum