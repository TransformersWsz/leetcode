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
class Solution:
    def shortestSubarray(self, A, K: int) -> int:
        prefix = [0]
        stack = []
        for v in A:
            prefix.append(prefix[-1] + v)

        res = length = len(prefix)
        for i in range(length):
            while stack and prefix[i] - prefix[stack[0]] >= K:
                res = min(res, i - stack[0])
                stack.pop(0)
            while stack and prefix[i] <= prefix[stack[-1]]:
                stack.pop()
            stack.append(i)
        return res if res != length else -1


if __name__ == "__main__":

    solution = Solution()
    nums = [2,-1,4]
    k = 3
    res = solution.shortestSubarray(nums, k)
    print(res)