# -*- coding: utf-8 -*-

"""
@File  : fan-zhuan-lian-biao-lcof.py
@Author: swift
@Date  : 2021/02/10 23:10
@Link  : https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/
@Desc  : 剑指 Offer 24. 反转链表
@Method: 
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = None
        while head:
            tmp = head.next
            head.next = new_head
            new_head = head
            head = tmp
        return new_head