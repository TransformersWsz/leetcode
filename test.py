#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/5 3:42 PM
# @Author  : Swift
# @File    : 123.py
# @Brief   :
# @Method  :


#
# Note: 类名、方法名、参数名已经指定，请勿修改
#
#
#
# @param rooms int整型二维数组 房间
# @param startPoint int整型一维数组 起始点
# @param endPoint int整型一维数组 终点
# @return int整型
#
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