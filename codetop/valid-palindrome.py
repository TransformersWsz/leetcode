'''
@File  : valid-palindrome.py
@Author: Swift
@Date  : 2021/5/4 19:34
@Link  : https://leetcode-cn.com/problems/valid-palindrome/
@Desc  : 125. 验证回文串
@Method: 
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [ c.lower() for c in s if c.isalnum() ]
        left, right = 0, len(s)-1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True