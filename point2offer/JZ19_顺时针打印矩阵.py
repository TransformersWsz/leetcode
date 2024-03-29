'''
@File  : JZ19_顺时针打印矩阵.py
@Author: Swift
@Date  : 2021/3/16 18:00
@Link  : https://www.nowcoder.com/practice/9b4c81a02cd34f76be2659fa0d54342a?tpId=13&tqId=11172&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
@Method: 
'''

# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        if not matrix:
            return []
        rows = len(matrix)
        cols = len(matrix[0])
        left, right, top, bottom = 0, cols-1, 0, rows-1
        res = []
        while True:
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top += 1
            if top > bottom:
                break

            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right -= 1
            if left > right:
                break

            for i in range(right, left-1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            if top > bottom:
                break

            for i in range(bottom, top-1, -1):
                res.append(matrix[i][left])
            left += 1
            if left > right:
                break
        return res