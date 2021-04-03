'''
@File  : JZ44_翻转单词顺序列.py
@Author: Swift
@Date  : 2021/3/26 21:32
@Link  : https://www.nowcoder.com/practice/12d959b108cb42b1ab72cef4d36af5ec?tpId=13&tqId=11196&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！
@Method: 
'''


# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if not s or len(s) <= 1:
            return s
        length = len(s)
        left, right = 0, 0
        tmp = []
        while right < length:
            if (s[right] == " " and s[left] != " ") or (s[right] != " " and s[left] == " "):
                tmp.append(s[left:right])
                left = right
            right += 1
        tmp.append(s[left:right])
        return "".join(tmp[::-1])
