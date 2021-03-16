'''
@File  : JZ1_二维数组中的查找.py
@Author: Swift
@Date  : 2021/3/16 17:49
@Link  : https://www.nowcoder.com/practice/abc3fe2ce8e146608e868a70efebf62e?tpId=13&tqId=11154&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
@Method: 
'''


# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        if not array:
            return False
        # write code here
        rows = len(array)
        cols = len(array[0])
        i = rows - 1
        j = 0
        while i >= 0 and j <= cols - 1:
            if array[i][j] == target:
                return True
            elif target > array[i][j]:
                j += 1
            else:
                i -= 1

        return False
