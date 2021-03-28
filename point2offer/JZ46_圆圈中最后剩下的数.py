'''
@File  : JZ46_圆圈中最后剩下的数.py
@Author: Swift
@Date  : 2021/3/28 23:10
@Link  : https://www.nowcoder.com/practice/f78a359491e64a50bce2d89cff857eb6?tpId=13&tqId=11199&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 约瑟夫环问题
@Method: 
'''

# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n <= 0:
            return -1
        index = 0
        for i in range(2, n+1):
            index = (index+m)%i
        return index