'''
@File  : two-sum.py
@Author: Swift
@Date  : 2020/12/22 15:35
@Link  : https://leetcode-cn.com/problems/two-sum/
@Desc  : 1. 两数之和
@Method: 
'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for idx, item in enumerate(nums):
            another = target - item
            if another in d:
                return [d[another], idx]
            d[item] = idx
        return []