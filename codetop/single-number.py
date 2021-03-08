# -*- coding: utf-8 -*-

"""
@File  : single-number.py
@Author: swift
@Date  : 2021/02/07 23:30
@Link  : https://leetcode-cn.com/problems/single-number/
@Desc  : 136. 只出现一次的数字
@Method: https://leetcode-cn.com/problems/single-number/solution/zhi-chu-xian-yi-ci-de-shu-zi-by-leetcode-solution/
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for item in nums:
            res = res ^ item
        return res