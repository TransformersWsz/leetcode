#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/20 12:19 AM
# @Author  : Swift
# @File    : remove-k-digits.py
# @Brief   : 402. 移掉K位数字
# @Method  : https://leetcode-cn.com/problems/remove-k-digits/solution/yi-diao-kwei-shu-zi-by-leetcode-solution/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for item in num:
            while k and stack and stack[-1] > item:
                stack.pop()
                k -= 1
            stack.append(item)
        if k:
            stack = stack[:-k]
        stack = "".join(stack).lstrip("0")
        return stack if stack else "0"
