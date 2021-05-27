'''
@File  : subtree-of-another-tree.py
@Author: Swift
@Date  : 2021/5/27 16:30
@Link  : https://leetcode-cn.com/problems/subtree-of-another-tree/
@Desc  : 572. 另一个树的子树
@Method: 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def is_same_tree(self, A, B):
        if not A and not B:
            return True
        if not A or not B:
            return False
        return A.val == B.val and self.is_same_tree(A.left, B.left) and self.is_same_tree(A.right, B.right)

    def isSubtree(self, A, B):
        if not A:
            return False
        return self.is_same_tree(A, B) or self.isSubtree(A.left, B) or self.isSubtree(A.right, B)