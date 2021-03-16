'''
@File  : JZ8_跳台阶.py
@Author: Swift
@Date  : 2021/3/16 17:56
@Link  : https://www.nowcoder.com/practice/8c82a5b80378478f9484d87d1c5f12a4?tpId=13&tqId=11161&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
@Method: 
'''


# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number <= 2:
            return number
        a = 1
        b = 2
        for _ in range(3, number+1):
            c = b + a
            a = b
            b = c
        return c