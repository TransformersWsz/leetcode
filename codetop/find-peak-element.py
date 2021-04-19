'''
@File  : find-peak-element.py
@Author: Swift
@Date  : 2021/4/19 13:36
@Link  : https://leetcode-cn.com/problems/find-peak-element/
@Desc  : 162. 寻找峰值
@Method: 
'''

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        while low < high:
            mid = (low+high) // 2
            if nums[mid] > nums[mid+1]:
                high = mid
            else:
                low = mid+1
        return low
