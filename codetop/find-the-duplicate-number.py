'''
@File  : find-the-duplicate-number.py
@Author: Swift
@Date  : 2021/6/21 17:47
@Link  : https://leetcode-cn.com/problems/find-the-duplicate-number/
@Desc  : 287. 寻找重复数
@Method:
'''


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res = None
        for item in nums:
            if nums[abs(item)] < 0:
                res = abs(item)
            else:
                nums[abs(item)] = -nums[abs(item)]

        for idx, item in enumerate(nums):
            nums[idx] = abs(item)
        return res