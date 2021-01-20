'''
@File  : validate-binary-search-tree.py
@Author: Swift
@Date  : 2021/01/20 23:42
@Link  : https://leetcode-cn.com/problems/validate-binary-search-tree/
@Desc  : 98. 验证二叉搜索树
@Method: https://leetcode-cn.com/problems/validate-binary-search-tree/solution/yan-zheng-er-cha-sou-suo-shu-by-leetcode-solution/ (中序遍历)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def mid_traverse(root, arr):
            if not root:
                return 
            mid_traverse(root.left, arr)
            arr.append(root.val)
            mid_traverse(root.right, arr)
        arr = []
        mid_traverse(root, arr)
        if len(arr) <= 1:
            return True
        else:
            for idx in range(1, len(arr)):
                if arr[idx-1] >= arr[idx]:
                    return False
            return True
