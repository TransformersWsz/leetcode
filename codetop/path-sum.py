# -*- coding: utf-8 -*-

"""
@File  : path-sum.py
@Author: swift
@Date  : 2021/02/22 14:12
@Link  : https://leetcode-cn.com/problems/path-sum/
@Desc  : 112. 路径总和
@Method: 
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, tgt):
        if not root:
            return False
        else:
            if not root.left and not root.right and tgt - root.val == 0:
                return True
            left = self.dfs(root.left, tgt - root.val)
            right = self.dfs(root.right, tgt - root.val)
            return left or right

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        res = self.dfs(root, targetSum)
        return res