'''
@File  : binary-tree-inorder-traversal.py
@Author: Swift
@Date  : 2020/12/21 22:02
@Link  : https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
@Desc  : 94. 二叉树的中序遍历
@Method: 
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def recursive(self, root, res):
        if root == None:
            return;
        self.recursive(root.left, res)
        res.append(root.val)
        self.recursive(root.right, res)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.recursive(root, res)
        return res
