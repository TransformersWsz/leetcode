# -*- coding: utf-8 -*-

"""
@File  : find-first-and-last-position-of-element-in-sorted-array.py
@Author: swift
@Date  : 2021/02/21 14:58
@Link  : https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
@Desc  : 34. 在排序数组中查找元素的第一个和最后一个位置
@Method: 
"""

class Solution:
    def searchRange(self, nums, target: int):
        length = len(nums)
        low = 0
        high = length-1
        res = []
        while low <= high:
            mid = (low+high) // 2
            if nums[mid] == target:
                left = mid-1
                while left >= low and nums[left] == target:
                    left -= 1
                res.append(left+1)

                right = mid+1
                while right <= high and nums[right] == target:
                    right += 1
                res.append(right-1)
                break
            else:
                if nums[mid] < target:
                    low = mid+1
                else:
                    high = mid-1
        if not res:
            res = [-1, -1]
        return res


if __name__ == '__main__':
    solution = Solution()
    nums = [1]
    target = 1
    res = solution.searchRange(nums, target)
    print(res)