# -*- coding: utf-8 -*-

"""
@File  : intersection-of-two-linked-lists.py
@Author: swift
@Date  : 2021/02/13 23:39
@Link  : https://leetcode-cn.com/problems/intersection-of-two-linked-lists/
@Desc  : 160. 相交链表
@Method: https://leetcode-cn.com/problems/intersection-of-two-linked-lists/solution/tu-jie-xiang-jiao-lian-biao-by-user7208t/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        tmpA = headA
        tmpB = headB
        while tmpA != tmpB:
            tmpA = tmpA.next if tmpA else headB
            tmpB = tmpB.next if tmpB else headA

        return tmpA