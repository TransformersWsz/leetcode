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
        length1 = len(num1)
        length2 = len(num2)
        min_length = min(length1, length2)
        tmp = 0
        res = []
        for i in range(1, min_length + 1):
            s = int(num1[-i]) + int(num2[-i]) + tmp
            if s >= 10:
                res.insert(0, s % 10)
                tmp = s // 10
            else:
                res.insert(0, s)
                tmp = 0

        if length1 == length2:
            res.insert(0, tmp)
        else:
            if length1 > min_length:
                for i in range(-min_length - 1, -length1 - 1, -1):
                    s = int(num1[i]) + tmp
                    if s >= 10:
                        res.insert(0, s % 10)
                        tmp = s // 10
                    else:
                        res.insert(0, s)
                        tmp = 0
            else:
                for i in range(-min_length - 1, -length2 - 1, -1):
                    s = int(num2[i]) + tmp
                    if s >= 10:
                        res.insert(0, s % 10)
                        tmp = s // 10
                    else:
                        res.insert(0, s)
                        tmp = 0
            if tmp != 0:
                res.insert(0, tmp)

        cal = 0
        for item in res:
            cal = cal * 10 + item
        return str(cal)


if __name__ == '__main__':
    solution = Solution()
    num1 = "9"
    num2 = "99"
    res = solution.addStrings(num1, num2)
    print(res)
    print(int(num1) + int(num2))