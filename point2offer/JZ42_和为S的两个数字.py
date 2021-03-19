'''
@File  : JZ42_和为S的两个数字.py
@Author: Swift
@Date  : 2021/3/19 15:16
@Link  : https://www.nowcoder.com/practice/390da4f7a00f44bea7c2f3d19491311b?tpId=13&tqId=11195&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
@Method: 
'''


# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, target):
        # write code here
        if not array:
            return []
        length = len(array)
        res = [array[-1] + 1, array[-1] + 1]
        i = 0
        j = length - 1
        while i < j:
            if target == array[i] + array[j]:
                if res[0] * res[1] > array[i] * array[j]:
                    res = [array[i], array[j]]

                i += 1
                j -= 1
            elif target > array[i] + array[j]:
                i += 1
            else:
                j -= 1
        return [] if res == [array[-1] + 1, array[-1] + 1] else res