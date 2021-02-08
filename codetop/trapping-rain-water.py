# -*- coding: utf-8 -*-

"""
@File  : trapping-rain-water.py
@Author: swift
@Date  : 2021/02/08 19:33
@Link  : https://leetcode-cn.com/problems/trapping-rain-water/
@Desc  : 42. 接雨水
@Method: https://leetcode-cn.com/problems/trapping-rain-water/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-w-8/ (按列求)
"""

class Solution:
    def trap(self, height) -> int:
        res = 0
        length = len(height)
        i = 1
        while i < length-1:
            left_max_h = max(height[:i])
            right_max_h = max(height[i+1:])
            min_h = min(left_max_h, right_max_h)
            if min_h > height[i]:
                res += min_h-height[i]
            i += 1
        return res


if __name__ == '__main__':
   solution = Solution()
   height = [4,2,0,3,2,5]
   res = solution.trap(height)
   print(res)