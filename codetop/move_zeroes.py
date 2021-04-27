'''
@File  : move_zeroes.py
@Author: Swift
@Date  : 2021/4/28 0:29
@Link  : https://leetcode-cn.com/problems/move-zeroes/
@Desc  : 283. 移动零
@Method: https://leetcode-cn.com/problems/move-zeroes/solution/yi-dong-ling-by-leetcode-solution/
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, 0
        length = len(nums)
        while right < length:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1