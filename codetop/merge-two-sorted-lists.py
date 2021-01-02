'''
@File  : merge-two-sorted-lists.py
@Author: Swift
@Date  : 2021/1/2 23:23
@Link  : https://leetcode-cn.com/problems/merge-two-sorted-lists/
@Desc  : 21. 合并两个有序链表
@Method: 
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        p = head
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        if l1:
            p.next = l1
        if l2:
            p.next = l2
        return head.next