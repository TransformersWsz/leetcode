# -*- coding: utf-8 -*-

"""
@File  : binary-tree-maximum-path-sum.py
@Author: swift
@Date  : 2021/02/18 22:26
@Link  : https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/
@Desc  : 124. 二叉树中的最大路径和
@Method: https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/solution/er-cha-shu-zhong-de-zui-da-lu-jing-he-by-ikaruga/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = float("-inf")

    def maxPathSum(self, root) -> int:
        def maxGain(root):
            if not root:
                return 0
            left = max(maxGain(root.left), 0)
            right = max(maxGain(root.right), 0)
            total = root.val + left + right
            self.res = max(total, left+root.val, right+root.val, self.res)
            return max(left, right)+root.val
        maxGain(root)
        return self.res


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    solution = Solution()
    res = solution.maxPathSum(root)
    print(res)


