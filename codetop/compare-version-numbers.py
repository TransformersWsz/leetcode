'''
@File  : compare-version-numbers.py
@Author: Swift
@Date  : 2021/4/20 12:04
@Link  : https://leetcode-cn.com/problems/compare-version-numbers/
@Desc  : 165. 比较版本号
@Method: 
'''

class Solution:
    def str2int(self, s):
        num = 0
        for c in s:
            num = num*10 + int(c)
        return num

    def compareVersion(self, version1: str, version2: str) -> int:
        l1 = version1.split(".")
        l2 = version2.split(".")
        if len(l1) < len(l2):
            gap = len(l2) - len(l1)
            l1 += ["0"] * gap
        else:
            gap = len(l1) - len(l2)
            l2 += ["0"] * gap

        for num1, num2 in zip(l1, l2):
            num1 = self.str2int(num1)
            num2 = self.str2int(num2)
            if num1 > num2:
                return 1
            elif num1 == num2:
                pass
            else:
                return -1
        return 0