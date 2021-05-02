'''
@File  : basic-calculator-ii.py
@Author: Swift
@Date  : 2021/5/2 13:18
@Link  : https://leetcode-cn.com/problems/basic-calculator-ii/
@Desc  : 227. 基本计算器 II
@Method:
'''

class Solution:
    def simple(self, l):
        flag = 1
        res = 0
        for c in l:
            if c == "-":
                flag = -1
            elif c == "+":
                flag = 1
            else:
                res += flag * c
        return res

    def merge(self, s):
        s = s.split()
        s = "".join(s)
        l = []
        for c in s:
            if not l or c in "+-*/":
                l.append(c)
            elif c in "0123456789":
                if l[-1] in "+-*/":
                    l.append(c)
                else:
                    l[-1] += c
            else:
                pass
        return l

    def calculate(self, s: str) -> int:
        simple_l = []
        l = self.merge(s)
        for item in l:
            if item in "+-*/":
                simple_l.append(item)
            elif item.isdigit():
                if not simple_l:
                    simple_l.append(int(item))
                else:
                    if simple_l[-1] == "*":
                        simple_l.pop()
                        former = simple_l.pop()
                        simple_l.append(int(former) * int(item))
                    elif simple_l[-1] == "/":
                        simple_l.pop()
                        former = simple_l.pop()
                        simple_l.append(int(former) // int(item))
                    else:
                        simple_l.append(int(item))
        return self.simple(simple_l)


if __name__ == '__main__':
    solution = Solution()
    s = " 3 + 2*2 "
    res = solution.calculate(s)
    print(res)