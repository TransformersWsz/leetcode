# -*- coding: utf-8 -*-

"""
@File  : palindrome-linked-list.py
@Author: swift
@Date  : 2021/02/13 23:49
@Link  : https://leetcode-cn.com/problems/palindrome-linked-list/
@Desc  : 234. 回文链表
@Method: 
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return arr == arr[::-1]