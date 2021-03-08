# -*- coding: utf-8 -*-

"""
@File  : search-in-rotated-sorted-array.py
@Author: swift
@Date  : 2021/02/19 13:44
@Link  : https://leetcode-cn.com/problems/search-in-rotated-sorted-array/
@Desc  : 33. 搜索旋转排序数组
@Method: https://leetcode-cn.com/problems/search-in-rotated-sorted-array/solution/sou-suo-xuan-zhuan-pai-xu-shu-zu-by-leetcode-solut/
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low+high) // 2
            if nums[mid]  == target:
                return mid
            else:
                if nums[low] <= nums[mid]:    # low->mid ordered
                    if nums[low] <= target and target <= nums[mid]:
                        high = mid-1
                    else:
                        low = mid + 1
                else:    # mid+1->high ordered
                    if nums[mid+1] <= target and target <= nums[high]:
                        low = mid+1
                    else:
                        high = mid-1
        return -1