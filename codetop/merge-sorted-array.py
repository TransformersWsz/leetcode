# -*- coding: utf-8 -*-

"""
@File  : merge-sorted-array.py
@Author: swift
@Date  : 2021/02/16 0:29
@Link  : https://leetcode-cn.com/problems/merge-sorted-array/
@Desc  : 88. 合并两个有序数组
@Method: 
"""


class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        def update_arr(nums1, item, idx):
            length = len(nums1)
            for i in range(length - 1, -1, -1):
                if i == idx:
                    nums1[i] = item
                    return
                else:
                    nums1[i] = nums1[i - 1]

        idx1 = 0
        idx2 = 0
        while idx2 < n and idx1 < m+idx2:
            if nums2[idx2] <= nums1[idx1]:
                update_arr(nums1, nums2[idx2], idx1)
                idx2 += 1
            idx1 += 1
        while idx2 < n:
            nums1[idx1] = nums2[idx2]
            idx1 += 1
            idx2 += 1


if __name__ == '__main__':
    nums1 = [2,0]
    m = 1
    nums2 = [1]
    n = 1
    solution = Solution()
    solution.merge(nums1, m, nums2, n)
    print(nums1)