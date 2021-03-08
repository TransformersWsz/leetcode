# -*- coding: utf-8 -*-

"""
@File  : reverse-words-in-a-string.py
@Author: swift
@Date  : 2021/02/19 13:50
@Link  : https://leetcode-cn.com/problems/reverse-words-in-a-string/
@Desc  : 151. 翻转字符串里的单词
@Method: 
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.strip().split()[::-1])