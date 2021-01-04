'''
@File  : maximum-depth-of-binary-tree.py
@Author: Swift
@Date  : 2021/1/4 21:01
@Link  : https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
@Desc  : 104. 二叉树的最大深度
@Method: 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def depth(root):
            if not root:
                return 0
            l = depth(root.left)
            r = depth(root.right)
            return 1+max(l, r)
        return depth(root)