'''
@File  : kth-smallest-element-in-a-bst.py
@Author: Swift
@Date  : 2021/4/29 13:59
@Link  : https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/
@Desc  : 230. 二叉搜索树中第K小的元素
@Method: 
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.nodes = []

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.nodes.append(root.val)
        self.inorder(root.right)

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.inorder(root)
        return self.nodes[k - 1]