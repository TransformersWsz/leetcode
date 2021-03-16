'''
@File  : JZ10_矩形覆盖.py
@Author: Swift
@Date  : 2021/3/16 17:57
@Link  : https://www.nowcoder.com/practice/72a5a919508a4251859fb2cfb987a0e6?tpId=13&tqId=11163&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
@Method: 
'''


# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        if number <= 2:
            return number
        a = 1
        b = 2
        for _ in range(3, number + 1):
            c = b + a
            a = b
            b = c
        return c
