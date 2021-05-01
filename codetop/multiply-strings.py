'''
@File  : multiply-strings.py
@Author: Swift
@Date  : 2021/5/1 19:21
@Link  : https://leetcode-cn.com/problems/multiply-strings/
@Desc  : 43. 字符串相乘
@Method: https://leetcode-cn.com/problems/multiply-strings/solution/zi-fu-chuan-xiang-cheng-by-leetcode-solution/
'''

class Solution:

    def addStrings(self, num1: str, num2: str) -> str:
        i, j, add = len(num1) - 1, len(num2) - 1, 0
        res = []
        while i >= 0 or j >= 0 or add != 0:
            x = int(num1[i]) if i >= 0 else 0
            y = int(num2[j]) if j >= 0 else 0
            total = x + y + add
            res.append(str(total % 10))
            add = total // 10
            i -= 1
            j -= 1
        return "".join(res[::-1])

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        res = "0"
        length1 = len(num1)
        length2 = len(num2)
        for i in range(length2-1, -1, -1):
            temp = ["0"] * (length2-i-1)
            add = 0
            for j in range(length1-1, -1, -1):
                item = int(num2[i]) * int(num1[j]) + add
                temp.append(str(item%10))
                add = item//10
            if add > 0:
                temp.append(str(add))
            temp = "".join(temp[::-1])
            res = self.addStrings(res, temp)
        return res