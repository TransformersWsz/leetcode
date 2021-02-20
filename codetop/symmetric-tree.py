# -*- coding: utf-8 -*-

"""
@File  : symmetric-tree.py
@Author: swift
@Date  : 2021/02/21 0:09
@Link  : 
@Desc  :
@Method: 
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def judge(self, arr):
        tmp = []
        for node in arr:
            if not node:
                tmp.append(None)
            else:
                tmp.append(node.val)
        return tmp == tmp[::-1]

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        q = [root]
        while q:
            length = len(q)
            for _ in range(length):
                head = q.pop(0)
                if head:
                    q.append(head.left if head.left else None)
                    q.append(head.right if head.right else None)
            if not self.judge(q):
                return False
        return True

