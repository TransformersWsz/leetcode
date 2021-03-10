'''
@File  : binary-tree-postorder-traversal.py
@Author: Swift
@Date  : 2021/3/10 22:15
@Link  : https://leetcode-cn.com/problems/binary-tree-postorder-traversal/
@Desc  : 145. 二叉树的后序遍历
@Method: https://leetcode-cn.com/problems/binary-tree-postorder-traversal/solution/die-dai-jie-fa-shi-jian-fu-za-du-onkong-jian-fu-za/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # root -> left -> right
        # right -> left -> root
        # left -> right -> root
        if not root:
            return []
        stack = []
        res = []
        while root or stack:
            if root:
                res.insert(0, root.val)
                stack.append(root)
                root = root.right
            else:
                root = stack.pop()
                root = root.left
        return res
