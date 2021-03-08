# -*- coding: utf-8 -*-

"""
@File  : balanced-binary-tree.py
@Author: swift
@Date  : 2021/02/07 22:53
@Link  : https://leetcode-cn.com/problems/balanced-binary-tree/
@Desc  : 110. 平衡二叉树
@Method: 
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def depth(root):
            if not root:
                return 0
            else:
                return 1 + max(depth(root.left), depth(root.right))

        if not root:
            return True
        left = depth(root.left)
        right = depth(root.right)
        if abs(left - right) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        return False