# -*- coding: utf-8 -*-

"""
@File  : sum-root-to-leaf-numbers.py
@Author: swift
@Date  : 2021/02/07 23:02
@Link  : https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/
@Desc  : 129. 求根到叶子节点数字之和
@Method: 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def sum_current_leaf(current_node, ancestor_sumval, res):
            if not current_node:
                return
            if not current_node.left and not current_node.right:
                res.append(ancestor_sumval*10 + current_node.val)
            else:
                sum_current_leaf(current_node.left, ancestor_sumval*10+current_node.val, res)
                sum_current_leaf(current_node.right, ancestor_sumval*10+current_node.val, res)

        if not root:
            return 0
        res = []
        sum_current_leaf(root, 0, res)
        return sum(res)
