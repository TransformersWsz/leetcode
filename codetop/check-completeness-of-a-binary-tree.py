# -*- coding: utf-8 -*-

"""
@File  : check-completeness-of-a-binary-tree.py
@Author: swift
@Date  : 2021/02/21 0:28
@Link  : https://leetcode-cn.com/problems/check-completeness-of-a-binary-tree/
@Desc  : 958. 二叉树的完全性检验
@Method: https://leetcode-cn.com/problems/check-completeness-of-a-binary-tree/solution/er-cha-shu-de-wan-quan-xing-jian-yan-by-leetcode/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        q = [(root, 1)]
        i = 0
        while i < len(q):
            node, idx = q[i]
            i += 1
            if node.left:
                q.append((node.left, 2*idx))
            if node.right:
                q.append((node.right, 2*idx+1))
        return q[-1][1] == len(q)