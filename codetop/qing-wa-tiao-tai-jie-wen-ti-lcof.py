# -*- coding: utf-8 -*-

"""
@File  : qing-wa-tiao-tai-jie-wen-ti-lcof.py
@Author: swift
@Date  : 2021/02/24 22:34
@Link  : https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/
@Desc  : 剑指 Offer 10- II. 青蛙跳台阶问题
@Method: 
"""

class Solution:
    def numWays(self, n: int) -> int:
        if n <= 1:
            return 1
        a = 1
        b = 1
        for _ in range(2, n+1):
            c = b + a
            a = b
            b = c
        return c%1000000007