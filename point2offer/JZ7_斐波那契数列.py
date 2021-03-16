'''
@File  : JZ7_斐波那契数列.py
@Author: Swift
@Date  : 2021/3/16 18:05
@Link  : https://www.nowcoder.com/practice/c6c7742f5ba7442aada113136ddea0c3?tpId=13&tqId=11160&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0，第1项是1）。
@Method: 
'''

# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        if n <= 1:
            return n
        a = 0
        b = 1
        for _ in range(2, n+1):
            c = b + a
            a = b
            b = c
        return c