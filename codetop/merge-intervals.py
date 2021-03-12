'''
@File  : merge-intervals.py
@Author: Swift
@Date  : 2021/3/11 21:13
@Link  : https://leetcode-cn.com/problems/merge-intervals/
@Desc  : 56. 合并区间
@Method: https://leetcode-cn.com/problems/merge-intervals/solution/he-bing-qu-jian-by-leetcode-solution/
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = []
        for item in intervals:
            if not res or res[-1][1] < item[0]:
                res.append(item)
            else:
                res[-1][1] = max(res[-1][1], item[1])
        return res

