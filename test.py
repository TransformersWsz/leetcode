#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/5 3:42 PM
# @Author  : Swift
# @File    : 123.py
# @Brief   :
# @Method  :


#
# Note: 类名、方法名、参数名已经指定，请勿修改
#
#
#
# @param rooms int整型二维数组 房间
# @param startPoint int整型一维数组 起始点
# @param endPoint int整型一维数组 终点
# @return int整型
#
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low+high) // 2
            pivot = nums[mid]
            if pivot == target:
                return mid
            elif pivot < target:
                if nums[high] >= target:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if nums[low] <= target:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1


if __name__ == "__main__":

    solution = Solution()
    nums = [4, 5, 6, 7, 8, 1, 2, 3]
    target = 8
    res = solution.search(nums, target)
    print(res)