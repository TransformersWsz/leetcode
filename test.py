#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/5 3:42 PM
# @Author  : Swift
# @File    : 123.py
# @Brief   :
# @Method  :


#
# Note: 类名、方法名、参数名已经指定，请勿修改
#
#
#
# @param rooms int整型二维数组 房间
# @param startPoint int整型一维数组 起始点
# @param endPoint int整型一维数组 终点
# @return int整型
#
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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
        q = self.find_kth_node(head, left - 1)
        qhead = q.next
        p = self.find_kth_node(head, right)
        phead = p.next
        newh, newt = self.rl(qhead, p)
        q.next = newh
        newt.next = phead
        return head


def construct(arr):
    dummy = ListNode(0)
    p = dummy
    for item in arr:
        node = ListNode(item)
        p.next = node
        p = node
    return dummy.next

def traverse(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    print(arr)


if __name__ == "__main__":

    solution = Solution()
    arr = [1, 2, 3, 4, 5]
    head = construct(arr)
    res = solution.reverseBetween(head, 2, 4)
    traverse(res)