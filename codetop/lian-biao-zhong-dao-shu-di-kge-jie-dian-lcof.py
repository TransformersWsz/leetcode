# -*- coding: utf-8 -*-

"""
@File  : lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof.py
@Author: swift
@Date  : 2021/02/16 0:50
@Link  : https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/
@Desc  : 剑指 Offer 22. 链表中倒数第k个节点
@Method: https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/solution/mian-shi-ti-22-lian-biao-zhong-dao-shu-di-kge-j-11/ (双指针)
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        former = head
        latter = head
        i = 0
        while i < k:
            latter = latter.next
            i += 1

        while latter:
            former = former.next
            latter = latter.next
        return former