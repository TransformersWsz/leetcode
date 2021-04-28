'''
@File  : copy-list-with-random-pointer.py
@Author: Swift
@Date  : 2021/4/28 19:45
@Link  : https://leetcode-cn.com/problems/copy-list-with-random-pointer/
@Desc  : 138. 复制带随机指针的链表
@Method: 
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def dfs(self, head, visited):
        if not head:
            return None
        if head in visited:
            return visited[head]
        node = Node(head.val)
        visited[head] = node
        node.next = self.dfs(head.next, visited)
        node.random = self.dfs(head.random, visited)
        return node

    def copyRandomList(self, head: 'Node') -> 'Node':
        visited = {}
        new_head = self.dfs(head, visited)
        return new_head
