'''
@File  : construct-binary-tree-from-inorder-and-postorder-traversal.py
@Author: Swift
@Date  : 2021/5/8 15:42
@Link  : https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
@Desc  : 106. 从中序与后序遍历序列构造二叉树
@Method: 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        item = postorder[-1]
        root = TreeNode(item)
        pivot = inorder.index(item)
        left_inorder = inorder[:pivot]
        right_inorder = inorder[pivot+1:]
        left_postorder = postorder[:len(left_inorder)]
        right_postorder = postorder[len(left_inorder):-1]
        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)
        return root
