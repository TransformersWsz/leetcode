# -*- coding: utf-8 -*-

"""
@File  : fibonacci-number.py
@Author: swift
@Date  : 2021/02/23 13:53
@Link  : https://leetcode-cn.com/problems/fibonacci-number/
@Desc  : 509. 斐波那契数
@Method: 
"""

class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1
        if n <= 1:
            return n
        for _ in range(2, n+1):
            cur = b + a
            a = b
            b = cur
        return cur