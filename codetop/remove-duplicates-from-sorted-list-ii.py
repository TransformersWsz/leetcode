'''
@File  : remove-duplicates-from-sorted-list-ii.py
@Author: Swift
@Date  : 2021/4/25 18:53
@Link  : https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/
@Desc  : 82. 删除排序链表中的重复元素 II
@Method: 
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy_head = ListNode(0)
        dummy_head.next = head
        last2 = dummy_head
        last1 = head
        while head:
            if head.val != last1.val:
                if last1.next == head:
                    last2 = last1
                else:
                    last2.next = head
                last1 = head
            head = head.next
        if last1.next:
            last2.next = None
        return dummy_head.next
