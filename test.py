class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last, res = 0, 0
        d = {}
        for idx, c in enumerate(s):
            if c in d:
                last = max(last, d[c])
                # last = max(last, d[c])
            res = max(res, idx-last+1)
            d[c] = idx + 1
        return res


if __name__ == '__main__':
    solution = Solution()
    s = "abba"
    res = solution.lengthOfLongestSubstring(s)
    print(res)