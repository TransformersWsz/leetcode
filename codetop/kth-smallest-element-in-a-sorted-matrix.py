#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/18 1:51 AM
# @Author  : Swift
# @File    : kth-smallest-element-in-a-sorted-matrix.py
# @Brief   : 378. 有序矩阵中第 K 小的元素
# @Method  : https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/solution/you-xu-ju-zhen-zhong-di-kxiao-de-yuan-su-by-leetco/


class Solution:
    def check(self, matrix, mid, k):
        rows = len(matrix)
        cols = len(matrix[0])
        i = rows-1
        j = 0
        count = 0
        while i >= 0 and j < cols:
            if matrix[i][j] <= mid:
                count += i+1
                j += 1
            else:
                i -= 1
        return count >= k

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        low = matrix[0][0]
        high = matrix[-1][-1]
        while low < high:
            mid = (low+high) // 2
            if self.check(matrix, mid, k):
                high = mid
            else:
                low = mid+1
        return low
