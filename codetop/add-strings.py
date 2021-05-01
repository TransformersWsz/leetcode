# -*- coding: utf-8 -*-

"""
@File  : add-strings.py
@Author: swift
@Date  : 2021/02/13 23:20
@Link  : https://leetcode-cn.com/problems/add-strings/
@Desc  : 415. 字符串相加
@Method: 
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j, add = len(num1)-1, len(num2)-1, 0
        res = []
        while i >= 0 or j >= 0 or add != 0:
            x = int(num1[i]) if i >= 0 else 0
            y = int(num2[j]) if j >= 0 else 0
            total = x + y + add
            res.append(str(total%10))
            add = total//10
            i -= 1
            j -= 1
        return "".join(res[::-1])


if __name__ == '__main__':
    solution = Solution()
    num1 = "9"
    num2 = "99"
    res = solution.addStrings(num1, num2)
    print(res)
    print(int(num1) + int(num2))