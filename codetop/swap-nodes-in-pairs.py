#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/7 5:35 PM
# @Author  : Swift
# @File    : swap-nodes-in-pairs.py
# @Brief   : 两两交换链表中的节点


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        fake_head = ListNode(0, head)
        i = 1
        q = fake_head
        p = head
        while p:
            if i%2 == 0:
                temp = p.next
                p.next = q.next
                q.next = p
                p.next.next = temp
                q = p.next
                p = temp
            else:
                p = p.next
            i += 1
        return fake_head.next
