'''
@File  : diameter-of-binary-tree.py
@Author: Swift
@Date  : 2021/1/4 20:54
@Link  : https://leetcode-cn.com/problems/diameter-of-binary-tree/
@Desc  : 543. 二叉树的直径
@Method: https://leetcode-cn.com/problems/diameter-of-binary-tree/solution/er-cha-shu-de-zhi-jing-by-leetcode-solution/
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 1

        def depth(root):
            if not root:
                return 0
            l = depth(root.left)
            r = depth(root.right)
            self.res = max(self.res, l + r + 1)
            return 1 + max(l, r)

        depth(root)
        return self.res - 1