# -*- coding: utf-8 -*-

"""
@File  : combination-sum.py
@Author: swift
@Date  : 2021/02/27 0:32
@Link  : https://leetcode-cn.com/problems/combination-sum/
@Desc  : 39. 组合总和
@Method: 
"""


class Solution:
    def combinationSum(self, candidates, target: int):
        arr = sorted(candidates)
        res = []
        length = len(arr)
        def back_trace(start, tmp, rest):
            if rest == 0:
                res.append(tmp)
            if rest > 0:
                for i in range(start, length):
                    if i > start and arr[i] == arr[i-1]:
                        continue
                    back_trace(i, tmp+[arr[i]], rest-arr[i])
        back_trace(0, [], target)
        return res


if __name__ == '__main__':
    solution = Solution()
    candidates = [2,3,6,7]
    target = 7
    res = solution.combinationSum(candidates, target)
    print(res)