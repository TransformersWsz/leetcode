'''
@File  : longest-common-prefix.py
@Author: Swift
@Date  : 2021/5/4 19:25
@Link  : https://leetcode-cn.com/problems/longest-common-prefix/
@Desc  : 14. 最长公共前缀
@Method: 
'''

import functools

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or len(strs) == 0:
            return ""

        def rule(x, y):
            if len(x) > len(y):
                return 1
            elif len(x) < len(y):
                return -1
            else:
                return 0

        strs.sort(key=functools.cmp_to_key(rule))
        length = len(strs)
        prefix = ""
        s = strs[0]
        flag = 1
        for c in s:
            prefix += c
            i = 1
            while i < length:
                if strs[i][:len(prefix)] == prefix:
                    pass
                else:
                    flag = 0
                    break
                i += 1
            if flag == 0:
                return prefix[:-1]
        return prefix