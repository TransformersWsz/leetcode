'''
@File  : JZ57_二叉树的下一个结点.py
@Author: Swift
@Date  : 2021/4/2 14:22
@Link  : https://www.nowcoder.com/practice/9023a0c988684a53960365b889ceaf5e?tpId=13&tqId=11210&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
@Method: 
'''

# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return None
        if pNode.right:
            tmp = pNode.right
            while tmp:
                result = tmp
                tmp = tmp.left
            return result
        else:
            while pNode:
                if pNode.next:
                    if pNode.next.left == pNode:
                        return pNode.next
                    pNode = pNode.next
                else:
                    return None
