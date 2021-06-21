'''
@File  : find-all-duplicates-in-an-array.py
@Author: Swift
@Date  : 2021/5/30 17:40
@Link  : https://leetcode-cn.com/problems/find-all-duplicates-in-an-array
@Desc  : 442. 数组中重复的数据
@Method: https://leetcode-cn.com/problems/find-all-duplicates-in-an-array/solution/shu-zu-zhong-zhong-fu-de-shu-jian-dan-bi-utnm/
'''

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for item in nums:
            if nums[abs(item)-1] < 0:
                res.append(abs(item))
            nums[abs(item)-1] = -nums[abs(item)-1]
        return res