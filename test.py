# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
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

def cons_list(arr):
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
    arr = [1,1]
    solution = Solution()
    head = cons_list(arr)
    head = solution.deleteDuplicates(head)
    traverse(head)