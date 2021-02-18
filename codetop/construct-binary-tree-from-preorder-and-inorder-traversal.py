# -*- coding: utf-8 -*-

"""
@File  : construct-binary-tree-from-preorder-and-inorder-traversal.py
@Author: swift
@Date  : 2021/02/18 19:26
@Link  : https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
@Desc  : 105. 从前序与中序遍历序列构造二叉树
@Method: https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solution/cong-qian-xu-yu-zhong-xu-bian-li-xu-lie-gou-zao-9/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def recursive(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None
            root = TreeNode(preorder[pre_left])
            idx = inorder.index(preorder[pre_left])
            left_size = idx - in_left
            root.left = recursive(pre_left + 1, pre_left + left_size, in_left, idx - 1)
            root.right = recursive(pre_left + left_size + 1, pre_right, idx + 1, in_right)
            return root

        length = len(preorder)
        root = recursive(0, length - 1, 0, length - 1)
        return root
