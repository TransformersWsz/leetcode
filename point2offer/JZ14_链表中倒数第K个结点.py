'''
@File  : JZ14_链表中倒数第K个结点.py
@Author: Swift
@Date  : 2021/3/26 21:22
@Link  : https://www.nowcoder.com/practice/886370fe658f41b498d40fb34ae76ff9?tpId=13&tqId=11167&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 输入一个链表，输出该链表中倒数第k个结点。
@Method: 
'''


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pHead ListNode类
# @param k int整型
# @return ListNode类
#
class Solution:
    def FindKthToTail(self, pHead, k):
        # write code here
        if not pHead:
            return None
        klead = pHead
        for i in range(k):
            klead = klead.next
            if not klead and i != k - 1:
                return None

        while klead:
            klead = klead.next
            pHead = pHead.next
        return pHead


