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
    def __init__(self):
        self.res = []

    def dfs(self, data, start):
        if start == len(data):
            self.res.append(data[:])
        else:
            for i in range(start, len(data)):
                data[i], data[start] = data[start], data[i]
                self.dfs(data, start+1)
                data[i], data[start] = data[start], data[i]

    def combine(self, n: int, k: int) -> List[List[int]]:
        data = [i + 1 for i in range(n)]
        self.dfs(data, 0)
        return self.res


if __name__ == "__main__":

    solution = Solution()
    n = 4
    k = 2

    res = solution.combine(4, 2)
    print(res)