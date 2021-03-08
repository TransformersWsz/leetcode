# -*- coding: utf-8 -*-

"""
@File  : implement-rand10-using-rand7.py
@Author: swift
@Date  : 2021/02/23 15:07
@Link  : https://leetcode-cn.com/problems/implement-rand10-using-rand7/
@Desc  : 470. 用 Rand7() 实现 Rand10()
@Method: https://leetcode-cn.com/problems/implement-rand10-using-rand7/solution/cong-zui-ji-chu-de-jiang-qi-ru-he-zuo-dao-jun-yun-/
"""


# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            a = rand7() - 1
            b = rand7()
            num = a * 7 + b
            if num <= 40:
                return num % 10 + 1

            a = num % 40 - 1
            b = rand7()
            num = a * 7 + b
            if num <= 60:
                return num % 10 + 1

            a = num % 60 - 1
            b = rand7()
            num = a * 7 + b
            if num <= 20:
                return num % 10 + 1