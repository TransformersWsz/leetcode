'''
@File  : string-compression.py
@Author: Swift
@Date  : 2021/5/18 22:09
@Link  : https://leetcode-cn.com/problems/string-compression/
@Desc  : 443. 压缩字符串
@Method: 
'''
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        anchor = write = 0
        for cur, c in enumerate(chars):
            if cur+1 == len(chars) or chars[cur+1] != c:
                chars[write] = chars[anchor]
                write += 1
                count = cur+1 - anchor
                if count > 1:
                    for digit in str(count):
                        chars[write] = digit
                        write += 1
                anchor = cur + 1
        return write