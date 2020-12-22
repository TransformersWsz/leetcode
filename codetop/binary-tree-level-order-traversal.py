'''
@File  : binary-tree-level-order-traversal.py
@Author: Swift
@Date  : 2020/12/22 15:29
@Link  : https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
@Desc  : 102. 二叉树的层序遍历
@Method: 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        res = []
        while queue:
            tmp = []
            length = len(queue)
            for _ in range(length):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)
        return res
