'''
@File  : JZ54_字符流中第一个不重复的字符.py
@Author: Swift
@Date  : 2021/4/3 22:34
@Link  : https://www.nowcoder.com/practice/00de97733b8e4f97a3fb5c680ee10720?tpId=13&tqId=11207&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
@Method: 
'''

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.d = {}
        self.q = []
    # 返回对应char
    def FirstAppearingOnce(self):
        # write code here
        while self.q:
            front = self.q[0]
            if self.d[front] == 1:
                return front
            else:
                self.q.pop(0)
        return "#"

    def Insert(self, char):
        # write code here
        if char not in self.d:
            self.d[char] = 1
            self.q.append(char)
        else:
            self.d[char] += 1