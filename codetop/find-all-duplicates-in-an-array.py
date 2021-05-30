'''
@File  : find-all-duplicates-in-an-array.py
@Author: Swift
@Date  : 2021/5/30 17:40
@Link  : 
@Desc  : 
@Method: 
'''

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for item in nums:
            if nums[abs(item)-1] < 0:
                res.append(abs(item))
            nums[abs(item)-1] = -nums[abs(item)-1]
        return res