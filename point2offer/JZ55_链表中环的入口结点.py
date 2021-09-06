'''
@File  : JZ55_链表中环的入口结点.py
@Author: Swift
@Date  : 2021/4/9 23:49
@Link  : https://www.nowcoder.com/practice/253d2c59ec3e4bc68da16833f79a38e4?tpId=13&tqId=11208&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
@Method: 
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead:
            return None
        slow = pHead
        fast = pHead
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                entry = pHead
                while entry != slow:
                    entry = entry.next
                    slow = slow.next
                return entry
        return None