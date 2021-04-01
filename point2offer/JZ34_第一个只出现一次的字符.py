'''
@File  : JZ34_第一个只出现一次的字符.py
@Author: Swift
@Date  : 2021/4/1 23:16
@Link  : https://www.nowcoder.com/practice/1c82e8cf713b4bbeb2a5b31cf5b0417c?tpId=13&tqId=11187&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.（从0开始计数）
@Method: 
'''


# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        d = {}
        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1

        for idx, c in enumerate(s):
            if d[c] == 1:
                return idx

        return -1