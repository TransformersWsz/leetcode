'''
@File  : reorder-list.py
@Author: Swift
@Date  : 2021/3/29 15:32
@Link  : https://leetcode-cn.com/problems/reorder-list/
@Desc  : 143. 重排链表
@Method: 
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return

        mid = self.middleNode(head)
        l1 = head
        l2 = mid.next
        mid.next = None
        l2 = self.reverseList(l2)
        self.mergeList(l1, l2)

    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp
        return prev

    def mergeList(self, l1: ListNode, l2: ListNode):
        while l1 and l2:
            l1_tmp = l1.next
            l2_tmp = l2.next

            l1.next = l2
            l1 = l1_tmp

            l2.next = l1
            l2 = l2_tmp


def traverse(head):
    while head:
        print(head.val)
        head = head.next

def construct_ll(arr):
    guard = ListNode(0)
    prev = guard
    for item in arr:
        node = ListNode(item)
        prev.next = node
        prev = node
    return guard.next


if __name__ == '__main__':
    solution = Solution()
    arr = [1,2,3,4,5,6,7]
    head = construct_ll(arr)
    # traverse(head)
    solution.reorderList(head)
    traverse(head)