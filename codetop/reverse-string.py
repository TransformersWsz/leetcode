# -*- coding: utf-8 -*-

"""
@File  : reverse-string.py
@Author: swift
@Date  : 2021/02/24 22:22
@Link  : https://leetcode-cn.com/problems/reverse-string/
@Desc  : 344. 反转字符串
@Method: 
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        low = 0
        high = len(s)-1
        while low < high:
            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1