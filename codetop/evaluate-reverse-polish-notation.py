#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/17 1:34 AM
# @Author  : Swift
# @File    : evaluate-reverse-polish-notation.py
# @Brief   : 150. 逆波兰表达式求值
# @Method  : https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/


from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = ["+", "-", "*", "/"]
        for item in tokens:
            if item not in op:
                stack.append(int(item))
            else:
                p = stack.pop()
                q = stack.pop()
                if item == "+":
                    res = q + p
                elif item == "-":
                    res = q - p
                elif item == "*":
                    res = q * p
                else:
                    flag = 1 if q*p >= 0 else -1
                    res = abs(q) // abs(p)
                    res = flag * res
                stack.append(res)
        return stack[0]


if __name__ == "__main__":

    solution = Solution()
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    res = solution.evalRPN(tokens)
    print(res)