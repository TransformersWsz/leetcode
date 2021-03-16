'''
@File  : JZ16_合并两个排序的链表.py
@Author: Swift
@Date  : 2021/3/16 17:59
@Link  : https://www.nowcoder.com/practice/d8b6b4358f774294a89de2a6ac4d9337?tpId=13&tqId=11169&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
@Method: 
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        guard = ListNode(0)
        prev = guard
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                prev.next = pHead1
                pHead1 = pHead1.next
            else:
                prev.next = pHead2
                pHead2 = pHead2.next
            prev = prev.next
        if pHead1:
            prev.next = pHead1
        if pHead2:
            prev.next = pHead2
        return guard.next