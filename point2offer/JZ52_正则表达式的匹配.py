'''
@File  : JZ52_正则表达式的匹配.py
@Author: Swift
@Date  : 2021/3/16 18:02
@Link  : https://www.nowcoder.com/practice/28970c15befb4ff3a264189087b99ad4?tpId=13&tqId=11205&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。 在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
@Method: 
'''



class Solution:
    def match_end(self, s, p, i, j):
        if i == 0:
            return False
        if p[j - 1] == ".":
            return True
        return s[i - 1] == p[j - 1]

    def match(self, s, p):
        # write code here
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] != "*":
                    if self.match_end(s, p, i, j):
                        dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j - 2]
                    if self.match_end(s, p, i, j - 1):
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
        return dp[m][n]