'''
@File  : JZ9_变态跳台阶.py
@Author: Swift
@Date  : 2021/3/16 18:07
@Link  : https://www.nowcoder.com/practice/22243d016f6b47f2a6928b4313c85387?tpId=13&tqId=11162&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
@Method: 
'''

# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        if number <= 1:
            return number
        prev = 1
        for _ in range(2, number+1):
            cur = prev*2
            prev = cur
        return cur