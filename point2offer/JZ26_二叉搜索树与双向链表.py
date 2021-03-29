'''
@File  : JZ26_二叉搜索树与双向链表.py
@Author: Swift
@Date  : 2021/3/29 17:00
@Link  : https://www.nowcoder.com/practice/947f6eb80d944a84850b0538bf0ec3a5?tpId=13&tqId=11179&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
@Method: 
'''


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
#
# @param pRootOfTree TreeNode类
# @return TreeNode类
#
class Solution:
    def __init__(self):
        self.order = []

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.order.append(root)
        self.inorder(root.right)

    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return None
        self.inorder(pRootOfTree)
        if len(self.order) == 1:
            self.order[0].right = None
            return self.order[0]

        for idx, node in enumerate(self.order):
            if idx == 0:
                self.order[idx].right = self.order[idx + 1]
            if 1 <= idx <= len(self.order) - 2:
                node.left = self.order[idx - 1]
                node.right = self.order[idx + 1]
            if idx == len(self.order) - 1:
                self.order[idx].left = self.order[idx - 1]
                self.order[idx].right = None

        return self.order[0]

