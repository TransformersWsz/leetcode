'''
@File  : minimum-absolute-difference-in-bst.py
@Author: Swift
@Date  : 2021/5/23 2:20
@Link  : https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/
@Desc  : 530. 二叉搜索树的最小绝对差
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
        self.res = []

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.res.append(root)
        self.inorder(root.right)

    def getMinimumDifference(self, root: TreeNode) -> int:
        self.inorder(root)
        length = len(self.res)
        gap = float('inf')
        for i in range(1, length):
            gap = min(gap, abs(self.res[i].val - self.res[i - 1].val))
        return gap
