'''
@File  : JZ28_数组中出现次数超过一半的数字.py
@Author: Swift
@Date  : 2021/3/17 16:48
@Link  : https://www.nowcoder.com/practice/e8a1b01a2df14cb2b228b30ee6a92163?tpId=13&tqId=11181&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
@Method: 
'''


# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        res = 0
        count = 0
        for item in numbers:
            if count == 0:
                res = item
            count += 1 if item == res else -1

        count = 0
        for item in numbers:
            if res == item:
                count += 1
        return res if count > len(numbers) // 2 else 0