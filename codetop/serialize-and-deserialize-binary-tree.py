'''
@File  : serialize-and-deserialize-binary-tree.py
@Author: Swift
@Date  : 2021/4/30 17:56
@Link  : https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/
@Desc  : 297. 二叉树的序列化与反序列化
@Method: 
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "null"
        return str(root.val) + "," + str(self.serialize(root.left)) + "," + str(self.serialize(root.right))

    def dfs(self, s):
        val = s.pop(0)
        if val == "null":
            return None
        node = TreeNode(val)
        node.left = self.dfs(s)
        node.right = self.dfs(s)
        return node

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        s = data.split(",")
        root = self.dfs(s)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))