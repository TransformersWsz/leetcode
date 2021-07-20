#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/20 2:29 AM
# @Author  : Swift
# @File    : convert-sorted-array-to-binary-search-tree.py
# @Brief   : 108. 将有序数组转换为二叉搜索树


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recur(self, nums):
        length = len(nums)
        if length == 0:
            return None
        mid = length//2
        root = TreeNode(nums[mid])
        root.left = self.recur(nums[:mid])
        root.right = self.recur(nums[mid+1:])
        return root

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        root = self.recur(nums)
        return root