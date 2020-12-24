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
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        fake_head = ListNode(0, head)
        q = fake_head
        p = head
        idx = 0
        while p:
            if idx == m-1:
                for _ in range(n-m):
                    tmp = p.next
                    if tmp:
                        p.next = tmp.next
                        tmp.next = q.next
                        q.next = tmp
                break
            q = p
            p = p.next
            idx += 1
        return fake_head.next
