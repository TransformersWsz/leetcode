#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/6 9:05 PM
# @Author  : Swift
# @File    : number-of-provinces.py
# @Brief   : 547. 省份数量
# @Method  : https://leetcode-cn.com/problems/number-of-provinces/solution/sheng-fen-shu-liang-by-leetcode-solution-eyk0/


class Solution:
    def __init__(self):
        self.count = 0

    def dfs(self, isConnected, i, isVisited):
        for j in range(len(isConnected[i])):
            if not isVisited[j] and isConnected[i][j]:
                isVisited[j] = True
                self.dfs(isConnected, j, isVisited)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        num = len(isConnected)
        isVisited = [False] * num
        for i in range(num):
            if not isVisited[i]:
                self.dfs(isConnected, i, isVisited)
                self.count += 1
        return self.count