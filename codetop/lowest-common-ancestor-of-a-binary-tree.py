'''
@File  : lowest-common-ancestor-of-a-binary-tree.py
@Author: Swift
@Date  : 2020/12/23 12:03
@Link  : https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
@Desc  : 236. 二叉树的最近公共祖先
@Method: https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/c-jing-dian-di-gui-si-lu-fei-chang-hao-li-jie-shi-/
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if not left:
            return right
        if not right:
            return left
        if left and right:
            return root