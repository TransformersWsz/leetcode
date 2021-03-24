'''
@File  : JZ22_从上往下打印二叉树.py
@Author: Swift
@Date  : 2021/3/23 13:05
@Link  : https://www.nowcoder.com/practice/7fe2212963db4790b57431d9ed259701?tpId=13&tqId=11175&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 从上往下打印出二叉树的每个节点，同层节点从左至右打印。
@Method: 
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        res = []
        q = [root]
        while q:
            length = len(q)
            for _ in range(length):
                root = q.pop(0)
                res.append(root.val)
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
        return res