'''
@File  : binary-tree-zigzag-level-order-traversal.py
@Author: Swift
@Date  : 2020/12/22 15:52
@Link  : https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/
@Desc  : 103. 二叉树的锯齿形层序遍历
@Method: 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = [root]
        layer_num = 0
        while queue:
            tmp = []
            length = len(queue)
            for idx in range(length):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if layer_num%2 == 1:
                tmp = tmp[::-1]
            res.append(tmp)
            layer_num += 1
        return res
