# -*- coding: utf-8 -*-

"""
@File  : path-sum-ii.py
@Author: swift
@Date  : 2021/02/02 23:57
@Link  : https://leetcode-cn.com/problems/path-sum-ii/
@Desc  : 113. 路径总和 II
@Method: 
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def dfs(root, tmp_sum, tmp_path, tgt, res):
            if not root:
                return
            tmp_sum += root.val
            if tmp_sum == tgt and not root.left and not root.right:
                res.append(tmp_path + [root.val])
            else:
                dfs(root.left, tmp_sum, tmp_path + [root.val], tgt, res)
                dfs(root.right, tmp_sum, tmp_path + [root.val], tgt, res)

        res = []
        dfs(root, 0, [], targetSum, res)
        return res
