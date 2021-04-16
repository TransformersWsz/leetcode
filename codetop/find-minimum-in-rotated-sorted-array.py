'''
@File  : find-minimum-in-rotated-sorted-array.py
@Author: Swift
@Date  : 2021/4/16 12:12
@Link  : https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/
@Desc  : 153. 寻找旋转排序数组中的最小值
@Method: 
'''

class Solution:
    def findMin(self, nums):
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low+high) // 2
            if nums[mid] < nums[high]:
                high = mid
            else:
                low = mid+1
        return nums[high]
