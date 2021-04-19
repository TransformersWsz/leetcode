'''
@File  : string-to-integer-atoi.py
@Author: Swift
@Date  : 2021/4/19 12:09
@Link  : https://leetcode-cn.com/problems/string-to-integer-atoi/
@Desc  : 8. 字符串转换整数 (atoi)
@Method: 
'''

class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        num = 0
        s = s.strip()
        flag = None
        for idx, c in enumerate(s):
            if c in ["+", "-"]:
                if idx != 0:
                    break
                else:
                    if not flag:
                        flag = -1 if c == "-" else 1
            elif c in "0123456789":
                num = num*10 + int(c)
            else:
                break
        flag = 1 if not flag else flag
        num = flag*num
        if num > (1<<31)-1:
            num = (1<<31) - 1
        elif num < -1<<31:
            num = -1<<31
        else:
            pass
        return num

if __name__ == '__main__':
    solution = Solution()
    s = "21474836460"
    res = solution.myAtoi(s)
    print(res)