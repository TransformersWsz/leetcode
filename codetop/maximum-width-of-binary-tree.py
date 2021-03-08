'''
@File  : maximum-width-of-binary-tree.py
@Author: Swift
@Date  : 2020/1/5 14:12
@Link  : https://leetcode-cn.com/problems/maximum-width-of-binary-tree/
@Desc  : 662. 二叉树最大宽度
@Method: 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:

        # bfs，队列中记录每个节点的root，pos，按层更新max_width
        if not root:
           return 0
        q = [(root, 0)]
        width = 1
        while q:
            temp = q[-1][1] - q[0][1] + 1
            width = max(width, temp)
            length = len(q)
            for _ in range(length):
                head, pos = q.pop(0)
                if head.left:
                    q.append((head.left, pos*2))
                if head.right:
                    q.append((head.right, pos*2+1))
        return width





