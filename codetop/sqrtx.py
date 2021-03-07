# -*- coding: utf-8 -*-

"""
@File  : sqrtx.py
@Author: swift
@Date  : 2021/02/16 0:00
@Link  : https://leetcode-cn.com/problems/sqrtx/
@Desc  : 69. x 的平方根
@Method: https://leetcode-cn.com/problems/sqrtx/solution/x-de-ping-fang-gen-by-leetcode-solution/ (二分查找)
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        res = -1
        while l <= r:
            mid = (l+r) // 2
            if mid*mid <= x:
                res = mid
                l = mid+1
            else:
                r = mid-1
        return res


if __name__ == '__main__':
    solution = Solution()
    res = solution.mySqrt(2)
    print(res)