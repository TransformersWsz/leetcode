'''
@File  : binary-tree-right-side-view.py
@Author: Swift
@Date  : 2020/12/24 11:36
@Link  : https://leetcode-cn.com/problems/binary-tree-right-side-view/
@Desc  : 199. 二叉树的右视图
@Method: 
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            res.append(queue[-1].val)
            length = len(queue)
            for i in range(length):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res
