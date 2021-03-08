# -*- coding: utf-8 -*-

"""
@File  : longest-consecutive-sequence.py
@Author: swift
@Date  : 2021/02/03 22:34
@Link  : https://leetcode-cn.com/problems/longest-consecutive-sequence/
@Desc  : 128. 最长连续序列
@Method: https://leetcode-cn.com/problems/longest-consecutive-sequence/solution/zui-chang-lian-xu-xu-lie-by-leetcode-solution/
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums_set = set(nums)
        for item in nums_set:
            if item-1 not in nums_set:
                tmp_length = 1
                tmp_item = item
                while tmp_item+1 in nums_set:
                    tmp_length += 1
                    tmp_item += 1
                res = max(res, tmp_length)
        return res
