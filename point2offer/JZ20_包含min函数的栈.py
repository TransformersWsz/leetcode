'''
@File  : JZ20_包含min函数的栈.py
@Author: Swift
@Date  : 2021/3/18 20:49
@Link  : https://www.nowcoder.com/practice/4c776177d2c04c2494f2555c9fcc1e49?tpId=13&tqId=11173&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
@Method: 
'''


# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, node):
        self.s1.append(node)
        if not self.s2 or self.s2[-1] > node:
            self.s2.append(node)

    def pop(self):
        peek = self.s1.pop()
        if peek == self.s2[-1]:
            self.s2.pop()

    def top(self):
        return self.s1[-1]

    def min(self):
        return self.s2[-1]