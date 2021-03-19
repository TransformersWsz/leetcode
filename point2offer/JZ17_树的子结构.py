'''
@File  : JZ17_树的子结构.py
@Author: Swift
@Date  : 2021/3/19 14:46
@Link  : https://www.nowcoder.com/practice/6e196c44c7004d15b1610b9afca8bd88?tpId=13&tqId=11170&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
@Method: https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/solution/mian-shi-ti-26-shu-de-zi-jie-gou-xian-xu-bian-li-p/
'''


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def is_contain(self, A, B):
        if not B:
            return True
        if not A or A.val != B.val:
            return False
        return self.is_contain(A.left, B.left) and self.is_contain(A.right, B.right)

    def HasSubtree(self, A, B):
        if not A or not B:
            return False
        if A:
            return self.is_contain(A, B) or self.HasSubtree(A.left, B) or self.HasSubtree(A.right, B)