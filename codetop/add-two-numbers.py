'''
@File  : add-two-numbers.py
@Author: Swift
@Date  : 2021/4/15 18:08
@Link  : https://leetcode-cn.com/problems/add-two-numbers/
@Desc  : 2. 两数相加
@Method: 
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        prev = head
        mod = 0
        add = 0
        while l1 and l2:
            s = l1.val + l2.val + add
            mod = s % 10
            add = s // 10
            node = ListNode(mod)
            prev.next = node
            prev = prev.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            s = l1.val + add
            mod = s % 10
            add = s // 10
            node = ListNode(mod)
            prev.next = node
            prev = prev.next
            l1 = l1.next
        if add > 0 and not l2:
            node = ListNode(add)
            prev.next = node
            add = 0

        while l2:
            s = l2.val + add
            mod = s % 10
            add = s // 10
            node = ListNode(mod)
            prev.next = node
            prev = prev.next
            l2 = l2.next
        if add > 0 and not l1:
            node = ListNode(add)
            prev.next = node

        return head.next