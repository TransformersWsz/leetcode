'''
@File  : reverse-nodes-in-k-group.py
@Author: Swift
@Date  : 2020/12/21 11:40
@Link  : https://leetcode-cn.com/problems/reverse-nodes-in-k-group/
@Desc  : 25. K 个一组翻转链表
@Method: https://leetcode-cn.com/problems/reverse-nodes-in-k-group/solution/k-ge-yi-zu-fan-zhuan-lian-biao-by-leetcode-solutio/
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head, tail):
        prev = None
        p = head
        while prev != tail:
            tmp_next = p.next
            p.next = prev
            prev = p
            p = tmp_next
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        first = ListNode(val=0, next=head)
        prev = first
        while head != None:
            tail = prev
            for _ in range(k):
                tail = tail.next
                if tail == None:
                    return first.next
            tmp_next = tail.next
            head, tail = self.reverse(head, tail)
            prev.next = head
            tail.next = tmp_next
            prev = tail
            head = tail.next
        return first.next