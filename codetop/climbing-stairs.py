# -*- coding: utf-8 -*-

"""
@File  : climbing-stairs.py
@Author: swift
@Date  : 2021/02/22 13:52
@Link  : https://leetcode-cn.com/problems/climbing-stairs/
@Desc  : 70. 爬楼梯
@Method: 
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a = 1
        b = 2
        for _ in range(3, n+1):
            c = a + b
            a = b
            b = c
        return c


if __name__ == '__main__':
    solution = Solution()
    res = solution.climbStairs(3)
    print(res)