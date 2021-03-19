'''
@File  : JZ24_二叉树中和为某一值的路径.py
@Author: Swift
@Date  : 2021/3/19 15:39
@Link  : https://www.nowcoder.com/practice/b736e784e3e34731af99065031301bca?tpId=13&tqId=11177&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 输入一颗二叉树的根节点和一个整数，按字典序打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
@Method: 
'''


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def dfs(self, root, tgt, res, tmp):
        if not root:
            return
        if not root.left and not root.right:
            if root.val == tgt:
                res.append(tmp + [root.val])
        else:
            self.dfs(root.left, tgt - root.val, res, tmp + [root.val])
            self.dfs(root.right, tgt - root.val, res, tmp + [root.val])

    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        res = []
        self.dfs(root, expectNumber, res, [])
        return res