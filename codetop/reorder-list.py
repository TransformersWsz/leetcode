'''
@File  : reorder-list.py
@Author: Swift
@Date  : 2021/3/29 15:32
@Link  : https://leetcode-cn.com/problems/reorder-list/
@Desc  : 143. 重排链表
@Method: 
'''





# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, root):
        if not root:
            return None
        prev = None
        while root:
            temp = root.next
            root.next = prev
            prev = root
            root = temp
        return prev

    def get_mid_node(self, head):
        slow = head
        fast = head
        while fast:
            slow = slow.next
            fast = fast.next
            if not fast.next:
                return slow
            fast = fast.next
            if not fast.next:

                return slow.next

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head

        mid = self.get_mid_node(head)
        down = self.reverse(mid)
        up = head
        while down:
            temp_up = up.next
            temp_down = down.next
            up.next = down
            down.next = temp_up
            down = temp_down
            up = temp_up
        up.next = None


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
    arr = [1,2,3,4]
    head = construct_ll(arr)
    traverse(head)
    solution.reorderList(head)
    traverse(head)