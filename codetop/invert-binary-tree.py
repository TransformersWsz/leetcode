# -*- coding: utf-8 -*-

"""
@File  : invert-binary-tree.py
@Author: swift
@Date  : 2021/02/24 22:55
@Link  : https://leetcode-cn.com/problems/invert-binary-tree/
@Desc  : 226. 翻转二叉树
@Method: 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root