# -*- coding: utf-8 -*-

"""
@File  : remove-duplicates-from-sorted-list.py
@Author: swift
@Date  : 2021/02/22 14:14
@Link  : https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/
@Desc  : 83. 删除排序链表中的重复元素
@Method: 
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        prev = head
        cur = prev.next
        while cur:
            if cur.val == prev.val:
                prev.next = cur.next
                cur = prev.next
            else:
                prev = cur
                cur = cur.next
        return head