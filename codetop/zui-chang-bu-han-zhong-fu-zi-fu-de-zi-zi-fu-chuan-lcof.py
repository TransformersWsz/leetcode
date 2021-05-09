'''
@File  : zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof.py
@Author: Swift
@Date  : 2021/5/9 21:34
@Link  : https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/
@Desc  : 剑指 Offer 48. 最长不含重复字符的子字符串
@Method: 
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last, res = 0, 0
        d = {}
        for idx, c in enumerate(s):
            if c in d:
                last = max(last, d[c])
            res = max(res, idx-last+1)
            d[c] = idx + 1
        return res