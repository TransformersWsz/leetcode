'''
@File  : JZ61_序列化二叉树.py
@Author: Swift
@Date  : 2021/4/9 0:56
@Link  : https://www.nowcoder.com/practice/cf7e25aa97c04cc1a68c8f040e71fb84?tpId=13&tqId=11214&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 请实现两个函数，分别用来序列化和反序列化二叉树
@Method: https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof/solution/jian-zhi-offer-37-xu-lie-hua-er-cha-shu-zgixr/
'''


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Serialize(self, root):
        # write code here
        if not root:
            return "null"
        return str(root.val) + "," + str(self.Serialize(root.left)) + "," + str(self.Serialize(root.right))

    def dfs(self, s):
        val = s.pop(0)
        if val == "null":
            return None
        root = TreeNode(int(val))
        root.left = self.dfs(s)
        root.right = self.dfs(s)
        return root

    def Deserialize(self, s):
        # write code here
        s = s.split(",")
        return self.dfs(s)
