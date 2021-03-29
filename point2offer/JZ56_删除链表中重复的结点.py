'''
@File  : JZ56_删除链表中重复的结点.py
@Author: Swift
@Date  : 2021/3/29 19:58
@Link  : https://www.nowcoder.com/practice/fc533c45b73a41b0b44ccba763f866ef?tpId=13&tqId=11209&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
@Method:
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead:
            return None
        guard = ListNode(float("-inf"))
        guard.next = pHead
        pHead = pHead.next
        guard.next.next = None

        last1 = guard
        last2 = last1.next
        while pHead:
            if pHead.val == last2.val:
                pHead = pHead.next
                while pHead and pHead.val == last2.val:
                    pHead = pHead.next
            else:
                last1 = last2
            last2 = pHead
            last1.next = last2
            if pHead:
                pHead = pHead.next

        return guard.next


def construct_ll(arr):
    guard = ListNode(0)
    prev = guard
    for item in arr:
        node = ListNode(item)
        prev.next = node
        prev = node
    return guard.next


def traverse(head):
    while head:
        print(head.val)
        head = head.next


if __name__ == '__main__':
    arr = [1, 2, 3, 3]
    head = construct_ll(arr)
    solution = Solution()
    head = solution.deleteDuplication(head)
    traverse(head)