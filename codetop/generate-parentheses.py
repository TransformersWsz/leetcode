'''
@File  : generate-parentheses.py
@Author: Swift
@Date  : 2021/4/16 16:33
@Link  : https://leetcode-cn.com/problems/generate-parentheses/
@Desc  : 22. 括号生成
@Method: 
'''

class Solution:
    def __init__(self):
        self.res = []

    def isLeagal(self, arr):
        stack = []
        for item in arr:
            if not stack:
                stack.append(item)
            else:
                if stack[-1] == "(" and item == ")":
                    stack.pop()
                else:
                    stack.append(item)
        return True if not stack else False

    def dfs(self, start, temp, n):
        if start == n:
            if self.isLeagal(temp):
                self.res.append("".join(temp))
        else:
            self.dfs(start + 1, temp + ["("], n)
            self.dfs(start + 1, temp + [")"], n)

    def generateParenthesis(self, n: int):
        self.dfs(0, [], n*2)
        return self.res


if __name__ == '__main__':
    solution = Solution()
    res = solution.generateParenthesis(3)
    print(res)
