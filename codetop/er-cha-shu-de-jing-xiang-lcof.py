'''
@File  : er-cha-shu-de-jing-xiang-lcof.py
@Author: Swift
@Date  : 2021/5/6 17:42
@Link  : https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/
@Desc  : 剑指 Offer 27. 二叉树的镜像
@Method: 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        l = root.left
        r = root.right
        root.left = r
        root.right = l
        self.mirrorTree(root.left)
        self.mirrorTree(root.right)
        return root