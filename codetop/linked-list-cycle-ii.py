'''
@File  : linked-list-cycle-ii.py
@Author: Swift
@Date  : 2020/12/21 21:28
@Link  : https://leetcode-cn.com/problems/linked-list-cycle-ii/
@Desc  : 142. 环形链表 II
@Method: https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/huan-xing-lian-biao-ii-by-leetcode-solution/
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        s = set()
        while head:
            if head in s:
                return head
            s.add(head)
            head = head.next
        return None