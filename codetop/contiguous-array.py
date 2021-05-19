'''
@File  : contiguous-array.py
@Author: Swift
@Date  : 2021/5/19 1:38
@Link  : https://leetcode-cn.com/problems/contiguous-array/
@Desc  : 525. 连续数组
@Method: https://leetcode-cn.com/problems/contiguous-array/solution/lian-xu-shu-zu-by-leetcode/#comment
'''

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {}
        d[0] = -1
        max_len, count = 0, 0
        for idx, val in enumerate(nums):
            count += 1 if val == 1 else -1
            if count in d:
                max_len = max(max_len, idx-d[count])
            else:
                d[count] = idx
        return max_len