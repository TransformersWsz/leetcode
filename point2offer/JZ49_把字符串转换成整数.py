'''
@File  : JZ49_把字符串转换成整数.py
@Author: Swift
@Date  : 2021/4/7 11:34
@Link  : https://www.nowcoder.com/practice/1277c681251b4372bdef344468e4f26e?tpId=13&tqId=11202&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0
@Method: 
'''

# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
    # write code here
        if not s:
            return 0
        s2n = {}
        for i in range(10):
            s2n[str(i)] = i
        f2n = {"+": 1, "-": -1}
        res = 0
        flag = 1
        if s[0] in f2n:
            if len(s) == 1:
                return 0
            flag = f2n[s[0]]
            s = s[1:]
        for c in s:
            if c in s2n:
                res = res*10 + s2n[c]
            else:
                return 0
        return flag*res

