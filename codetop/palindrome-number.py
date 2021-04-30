'''
@File  : palindrome-number.py
@Author: Swift
@Date  : 2021/4/30 12:24
@Link  : https://leetcode-cn.com/problems/palindrome-number/
@Desc  : 9. 回文数
@Method: 
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = []
        while x != 0:
            temp.append(x%10)
            x = x//10
        return temp == temp[::-1]