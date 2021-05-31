'''
@File  : two-sum-ii-input-array-is-sorted.py
@Author: Swift
@Date  : 2021/5/31 16:47
@Link  : https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/
@Desc  : 167. 两数之和 II - 输入有序数组
@Method: 
'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1