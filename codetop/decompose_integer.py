#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/15 10:48 PM
# @Author  : Swift
# @File    : decompose_integer.py
# @Brief   : 百度的一道面试题：整数分解，4 -> [[1,1,1,1], [1,2,1], [1,3]]
# @Method  :

class Solution(object):
    def __init__(self):
        self._res = []

    def dfs(self, start, target, tmp):
        if start == target:
            if tmp not in self._res:
                self._res.append(tmp)
        else:
            rest = target - start
            for i in range(1, rest+1):
                self.dfs(start+i, target, tmp + [i])

    def decompose(self, target):
        self.dfs(0, target, [])
        return self._res


if __name__ == "__main__":

    solution = Solution()
    target = 4
    res = solution.decompose(target)
    print(res)