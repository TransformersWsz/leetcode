'''
@File  : er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof.py
@Author: Swift
@Date  : 2021/4/18 12:29
@Link  : https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/
@Desc  : 剑指 Offer 54. 二叉搜索树的第k大节点
@Method: 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = []

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.res.append(root.val)
        self.inorder(root.right)

    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.inorder(root)
        return self.res[-k]
