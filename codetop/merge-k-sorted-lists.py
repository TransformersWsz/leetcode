# -*- coding: utf-8 -*-

"""
@File  : merge-k-sorted-lists.py
@Author: swift
@Date  : 2021/02/20 23:41
@Link  : https://leetcode-cn.com/problems/merge-k-sorted-lists/
@Desc  : 23. 合并K个升序链表
@Method: https://leetcode-cn.com/problems/merge-k-sorted-lists/solution/he-bing-kge-pai-xu-lian-biao-by-leetcode-solutio-2/ （归并合并）
"""



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, listA, listB):
        if not listA or not listB:
            return listA if listA else listB
        head = ListNode(0)
        first = head
        while listA and listB:
            if listA.val <= listB.val:
                head.next = listA
                listA = listA.next
            else:
                head.next = listB
                listB = listB.next
            head = head.next
        head.next = listA if listA else listB
        return first.next

    def mergeKLists(self, lists: list) -> ListNode:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        low = 0
        high = len(lists)
        mid = (low + high) // 2
        left = self.mergeKLists(lists[low:mid])
        right = self.mergeKLists(lists[mid:high])
        return self.mergeTwoLists(left, right)


def traverse(head):
    while head:
        print(head.val)
        head = head.next


if __name__ == '__main__':
    list00 = ListNode(1)
    list01 = ListNode(4)
    list02 = ListNode(5)
    list00.next = list01
    list01.next = list02

    list10 = ListNode(1)
    list11 = ListNode(3)
    list12 = ListNode(4)
    list10.next = list11
    list11.next = list12

    list20 = ListNode(2)
    list21 = ListNode(6)
    list20.next = list21

    lists = [list00, list10, list20]
    solution = Solution()
    head = solution.mergeKLists(lists)
    traverse(head)
