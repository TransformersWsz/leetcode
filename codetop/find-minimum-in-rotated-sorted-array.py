'''
@File  : find-minimum-in-rotated-sorted-array.py
@Author: Swift
@Date  : 2021/4/16 12:12
@Link  : https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/
@Desc  : 153. 寻找旋转排序数组中的最小值
@Method: 
'''

class Solution:
    def findMin(self, rotateArray):
        low = 0
        high = len(rotateArray)-1
        while low < high:
            mid = (high + low) // 2
            if rotateArray[mid] < rotateArray[high]:
                high = mid
            elif rotateArray[mid] > rotateArray[high]:
                low = mid + 1
            else:
                high -= 1
        return rotateArray[low]
