'''
@File  : JZ59_按之字形顺序打印二叉树.py
@Author: Swift
@Date  : 2021/3/27 12:46
@Link  : https://www.nowcoder.com/practice/91b69814117f4e8097390d107d2efbe0?tpId=13&tqId=11212&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
@Method: 
'''


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def reverse(self, q, layer):
        tmp = []
        if layer % 2 == 1:
            for node in q:
                tmp.append(node.val)
        else:
            for node in q:
                tmp.insert(0, node.val)
        return tmp

    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        res = []
        layer = 1
        q = [pRoot]
        while q:
            res.append(self.reverse(q, layer))
            length = len(q)
            for _ in range(length):
                root = q.pop(0)
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            layer += 1
        return res