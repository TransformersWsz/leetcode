'''
@File  : reverse-linked-list-ii.py
@Author: Swift
@Date  : 2020/12/24 14:07
@Link  : https://leetcode-cn.com/problems/reverse-linked-list-ii/
@Desc  : 92. 反转链表 II
@Method: 
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def rl(self, head, tail):
        prev = None
        cur = head
        end_node = tail.next
        while cur != end_node:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return tail, head

    def find_kth_node(self, head, k):
        p = head
        for i in range(k - 1):
            p = p.next
        return p

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        q = self.find_kth_node(dummy, left)
        qhead = q.next
        p = self.find_kth_node(dummy, right+1)
        phead = p.next
        newh, newt = self.rl(qhead, p)
        q.next = newh
        newt.next = phead
        return dummy.next