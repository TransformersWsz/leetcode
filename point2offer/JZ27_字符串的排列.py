'''
@File  : JZ27_字符串的排列.py
@Author: Swift
@Date  : 2021/3/28 15:13
@Link  : https://www.nowcoder.com/practice/fe6b651b66ae47d7acce78ffdd9a96c7?tpId=13&tqId=11180&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则按字典序打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
@Method: 
'''

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.res = []

    def dfs(self, l, start):
        if start == len(l):
            tmp = "".join(l)
            if tmp not in self.res:
                self.res.append("".join(l))
        else:
            length = len(l)
            for i in range(start, length):
                l[start], l[i] = l[i], l[start]
                self.dfs(l, start+1)

                l[i], l[start] = l[start], l[i]

    def Permutation(self, s):
        l = list(s)
        self.dfs(l, 0)
        return self.res


if __name__ == '__main__':
    solution = Solution()
    s = "abc"
    res = solution.Permutation(s)
    print(res)