'''
@File  : JZ18_二叉树的镜像.py
@Author: Swift
@Date  : 2021/3/17 16:10
@Link  : https://www.nowcoder.com/practice/a9d0ecbacef9410ca97463e4a5c83be7?tpId=13&tqId=11171&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 操作给定的二叉树，将其变换为源二叉树的镜像。
@Method: 
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pRoot TreeNode类
# @return TreeNode类
#
class Solution:
    def Mirror(self , pRoot ):
        # write code here
        if not pRoot:
            return None
        pRoot.left, pRoot.right = pRoot.right, pRoot.left
        self.Mirror(pRoot.left)
        self.Mirror(pRoot.right)
        return pRoot
