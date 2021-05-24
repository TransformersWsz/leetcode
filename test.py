
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def get_len(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count

    def get_last_k_node(self, head, k):
        cur = head
        forward = head
        for _ in range(k):
            if forward:
                forward = forward.next

        while forward:
            cur = cur.next
            forward = forward.next
        return cur

    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head

        length = self.get_len(head)
        k = k % length
        if k == 0:
            return head
        new_tail_node = self.get_last_k_node(head, k + 1)
        new_head_node = new_tail_node.next
        temp = self.get_last_k_node(head, 1)
        temp.next = head
        new_tail_node.next = None
        return new_head_node


def construct(arr):
    dummy_head = ListNode(0)
    prev = dummy_head
    for item in arr:
        node = ListNode(item)
        prev.next = node
        prev = node
    return dummy_head.next

def traverse(head):
    while head:
        print(head.val)
        head = head.next

if __name__ == '__main__':
    solution = Solution()
    arr = [1,2]
    k = 2
    head = construct(arr)
    new_head = solution.rotateRight(head, k)
    traverse(new_head)