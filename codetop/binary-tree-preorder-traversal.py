# -*- coding: utf-8 -*-

"""
@File  : binary-tree-preorder-traversal.py
@Author: swift
@Date  : 2021/02/20 23:51
@Link  : https://leetcode-cn.com/problems/binary-tree-preorder-traversal/
@Desc  : 144. 二叉树的前序遍历
@Method: 
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def preorder(root, res):
            if not root:
                return
            res.append(root.val)
            preorder(root.left, res)
            preorder(root.right, res)

        res = []
        preorder(root, res)
        return res
