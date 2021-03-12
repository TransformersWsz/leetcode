'''
@File  : minimum-window-substring.py
@Author: Swift
@Date  : 2021/3/11 15:39
@Link  : https://leetcode-cn.com/problems/minimum-window-substring/
@Desc  : 76. 最小覆盖子串
@Method: https://leetcode-cn.com/problems/minimum-window-substring/solution/tong-su-qie-xiang-xi-de-miao-shu-hua-dong-chuang-k/
'''

import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.defaultdict(int)
        for c in t:
            need[c] += 1
        need_len = len(t)

        i = 0
        res = (0, len(s)+1)
        for idx, item in enumerate(s):
            if need[item] > 0:
                need_len -= 1
            need[item] -= 1
            if need_len == 0:
                while True:
                    c = s[i]
                    if need[c] == 0:
                        break
                    need[c] += 1
                    i += 1
                if idx-i < res[1] - res[0]:
                    res = (i, idx)
                need[s[i]] += 1
                need_len += 1
                i += 1
        return "" if res[1] == len(s)+1 else s[res[0]:res[1]+1]







if __name__ == '__main__':
    solution = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    res = solution.minWindow(s, t)
    print(res)


