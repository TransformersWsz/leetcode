'''
@File  : matrix_cover.py
@Author: Swift
@Date  : 2021/3/16 17:38
@Link  : https://www.nowcoder.com/practice/72a5a919508a4251859fb2cfb987a0e6?tpId=13&tqId=11163&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 矩形覆盖
@Method: 
'''

# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        if number <= 2:
            return number
        return self.rectCover(number-1) + self.rectCover(number-2)
