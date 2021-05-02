'''
@File  : remove-duplicates-from-sorted-array.py
@Author: Swift
@Date  : 2021/5/2 14:54
@Link  : https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/
@Desc  : 26. 删除有序数组中的重复项
@Method: 
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 1:
            return length
        left, right, temp = 0, 0, nums[0]
        while right < length:
            if nums[right] != temp:
                left += 1
                nums[left] = nums[right]
                temp = nums[right]
            right += 1
        return left+1