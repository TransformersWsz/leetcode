'''
@File  : JZ25_复杂链表的复制.py
@Author: Swift
@Date  : 2021/3/18 22:23
@Link  : https://www.nowcoder.com/practice/f836b2c43afc4b35ad6adc41ec941dba?tpId=13&tqId=11178&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针random指向一个随机节点），请对此链表进行深拷贝，并返回拷贝后的头结点。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
@Method: 
'''


# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def dfs(self, pHead, visited):
        if not pHead:
            return None
        if pHead in visited:
            return visited[pHead]
        node = RandomListNode(pHead.label)
        visited[pHead] = node
        node.next = self.dfs(pHead.next, visited)
        node.random = self.dfs(pHead.random, visited)
        return node

    def Clone(self, pHead):
        # write code here
        visited = {}
        root = self.dfs(pHead, visited)
        return root