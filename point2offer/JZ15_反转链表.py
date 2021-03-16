'''
@File  : JZ15_反转链表.py
@Author: Swift
@Date  : 2021/3/16 17:58
@Link  : https://www.nowcoder.com/practice/75e878df47f24fdc9dc3e400ec6058ca?tpId=13&tqId=11168&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 输入一个链表，反转链表后，输出新链表的表头。
@Method: 
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead:
            return None
        prev = None
        while pHead:
            tmp = pHead.next
            pHead.next = prev
            prev = pHead
            pHead = tmp
        return prev