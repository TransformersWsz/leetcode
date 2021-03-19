'''
@File  : JZ39_平衡二叉树.py
@Author: Swift
@Date  : 2021/3/19 15:44
@Link  : https://www.nowcoder.com/practice/8b3b95850edb4115918ecebdf1b4d222?tpId=13&tqId=11192&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 输入一棵二叉树，判断该二叉树是否是平衡二叉树。在这里，我们只需要考虑其平衡性，不需要考虑其是不是排序二叉树。平衡二叉树（Balanced Binary Tree），具有以下性质：它是一棵空树或它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树。
@Method: 
'''


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def depth(self, root):
        if not root:
            return 0
        return 1 + max(self.depth(root.left), self.depth(root.right))

    def IsBalanced_Solution(self, root):
        # write code here
        if not root:
            return True
        if abs(self.depth(root.left) - self.depth(root.right)) <= 1:
            return self.IsBalanced_Solution(root.left) and self.IsBalanced_Solution(root.right)
        else:
            return False