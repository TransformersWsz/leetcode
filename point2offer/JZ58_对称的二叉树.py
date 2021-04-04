'''
@File  : JZ58_对称的二叉树.py
@Author: Swift
@Date  : 2021/4/4 18:32
@Link  : https://www.nowcoder.com/practice/ff05d44dfdb04e1d83bdbdab320efbcb?tpId=13&tqId=11211&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 请实现一个函数，用来判断一棵二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
@Method: 
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def recur(self, r1, r2):
        if not r1 and not r2:
            return True
        if not r1 or not r2:
            return False
        return r1.val == r2.val and self.recur(r1.left, r2.right) and self.recur(r1.right, r2.left)
    def isSymmetrical(self, pRoot):
        # write code here
        return self.recur(pRoot, pRoot)