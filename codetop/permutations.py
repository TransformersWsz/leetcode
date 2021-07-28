#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/29 1:20 AM
# @Author  : Swift
# @File    : permutations.py
# @Brief   : 46. 全排列
# @Method  :

class Solution:
    def __init__(self):
        self.res = []

    def recur(self, nums, start):
        if start == len(nums):
            self.res.append(nums[:])
        else:
            for i in range(start, len(nums)):
                nums[i], nums[start] = nums[start], nums[i]
                self.recur(nums, start+1)
                nums[i], nums[start] = nums[start], nums[i]

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.recur(nums, 0)
        return self.res