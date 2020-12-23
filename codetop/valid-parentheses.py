'''
@File  : valid-parentheses.py
@Author: Swift
@Date  : 2020/12/23 22:55
@Link  : https://leetcode-cn.com/problems/valid-parentheses/
@Desc  : 20. 有效的括号
@Method: https://leetcode-cn.com/problems/valid-parentheses/solution/zhu-bu-fen-xi-tu-jie-zhan-zhan-shi-zui-biao-zhun-d/
'''

class Solution:
    def isValid(self, s: str) -> bool:
        d = {')': '(', ']': '[', '}': '{'}
        stack = []
        for c in s:
            if stack and c in d:
                if stack[-1] == d[c]:
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(c)
        return not stack

if __name__ == '__main__':
    obj = Solution()
    s = "()[]{}"
    res = obj.isValid(s)
    print(res)