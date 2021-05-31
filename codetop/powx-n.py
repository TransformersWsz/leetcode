'''
@File  : powx-n.py
@Author: Swift
@Date  : 2021/5/31 16:36
@Link  : https://leetcode-cn.com/problems/powx-n
@Desc  : 50. Pow(x, n)
@Method: https://leetcode-cn.com/problems/powx-n/solution/powx-n-by-leetcode-solution/
'''

class Solution:
    def recur(self, x, n):
        if n == 0:
            return 1
        mul = self.recur(x, n//2)
        return mul*mul if n%2==0 else mul*mul*x

    def myPow(self, x: float, n: int) -> float:
        mul = self.recur(x, abs(n))
        return mul if n >= 0 else 1/mul