# -*- coding: utf-8 -*-

"""
@File  : remove-nth-node-from-end-of-list.py
@Author: swift
@Date  : 2021/02/26 1:16
@Link  : 
@Desc  :
@Method: 
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n: int) -> ListNode:
        if not head:
            return None
        guard = ListNode(0)
        guard.next = head
        prev = guard
        latter = head.next
        for _ in range(n - 1):
            latter = latter.next
        while latter:
            head = head.next
            latter = latter.next
            prev = prev.next
        prev.next = head.next
        return guard.next


if __name__ == '__main__':
    arr = []
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    solution = Solution()
    head = solution.removeNthFromEnd(node1, 2)
    while head:
        print(head.val)
        head = head.next