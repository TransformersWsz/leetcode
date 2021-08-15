#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/8/16 1:31 AM
# @Author  : Swift
# @File    : middle-of-the-linked-list.py
# @Brief   : 876. 链表的中间结点
# @Method  :


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow