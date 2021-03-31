'''
@File  : JZ62_二叉搜索树的第k个结点.py
@Author: Swift
@Date  : 2021/3/31 16:31
@Link  : https://www.nowcoder.com/practice/ef068f602dde4d28aab2b210e859150a?tpId=13&tqId=11215&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 给定一棵二叉搜索树，请找出其中的第k小的TreeNode结点。
@Method: 
'''


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.inorder = []

    def dfs(self, pRoot):
        if not pRoot:
            return None
        self.dfs(pRoot.left)
        self.inorder.append(pRoot)
        self.dfs(pRoot.right)

    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        self.dfs(pRoot)
        if k <= 0 or k > len(self.inorder):
            return None
        return self.inorder[k - 1]
