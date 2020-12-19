'''
@File  : reverse-linked-list.py
@Author: Swift
@Date  : 2020/12/18 11:48
@Link  : https://leetcode-cn.com/problems/reverse-linked-list/
@Desc  : 206. 反转链表
@Method: 
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        return pre
