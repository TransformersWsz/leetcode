'''
@File  : odd-even-linked-list.py
@Author: Swift
@Date  : 2021/4/17 16:00
@Link  : https://leetcode-cn.com/problems/odd-even-linked-list/
@Desc  : 328. 奇偶链表
@Method: 
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummyoddHead = ListNode(0)
        prevodd = dummyoddHead
        dummyevenHead = ListNode(0)
        preveven = dummyevenHead
        step = 1
        while head:
            if step%2 == 1:
                prevodd.next = head
                prevodd = prevodd.next
            else:
                preveven.next = head
                preveven = preveven.next
            step += 1
            head = head.next
        preveven.next = None
        prevodd.next = dummyevenHead.next
        return dummyoddHead.next
