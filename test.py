'''
@File  : longest-substring-without-repeating-characters.py
@Author: Swift
@Date  : 2020/12/19 22:18
@Link  : https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
@Desc  : 3. 无重复字符的最长子串
@Method:
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, res = 0, 0
        d = {}
        for idx in range(len(s)):
            if s[idx] in d:
                i = max(d[s[idx]], i)
            res = max(res, idx-i)
            d[s[idx]] = idx
        return res


if __name__ == '__main__':
    obj = Solution()
    s = "pwwkew"
    res = obj.lengthOfLongestSubstring(s)
    print(res)