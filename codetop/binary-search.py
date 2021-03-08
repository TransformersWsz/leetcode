# -*- coding: utf-8 -*-

"""
@File  : binary-search.py
@Author: swift
@Date  : 2021/02/10 23:04
@Link  : https://leetcode-cn.com/problems/binary-search/
@Desc  : 704. 二分查找
@Method: 
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        low = 0
        high = length-1
        while low <= high:
            mid = (low+high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid+1
            else:
                high = mid-1
        return -1