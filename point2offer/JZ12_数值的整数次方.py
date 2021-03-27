'''
@File  : JZ12_数值的整数次方.py
@Author: Swift
@Date  : 2021/3/27 12:34
@Link  : https://www.nowcoder.com/practice/1a834e5e3e1a4b7ba251417554e07c00?tpId=13&tqId=11165&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
@Method: 
'''

# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        if base == 0:
            return 0
        if exponent == 0:
            return 1
        flag = 1
        if exponent < 0:
            flag = -1
            exponent = abs(exponent)
        res = 1
        for _ in range(exponent):
            res = res * base
        return res if flag else 1/res


if __name__ == '__main__':
    s = Solution()
    res = s.Power(2, -3)
    print(res)