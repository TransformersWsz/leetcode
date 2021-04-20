'''
@File  : next-permutation.py
@Author: Swift
@Date  : 2021/4/20 11:20
@Link  : https://leetcode-cn.com/problems/next-permutation/
@Desc  : 31. 下一个排列
@Method: https://leetcode-cn.com/problems/next-permutation/solution/xia-yi-ge-pai-lie-suan-fa-xiang-jie-si-lu-tui-dao-/
'''

class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        i = length-2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i >= 0:
            j = length-1
            while j > i and nums[i] >= nums[j]:
                j -= 1
            if j > i:
                nums[i], nums[j] = nums[j], nums[i]
        left, right = i+1, length-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


if __name__ == '__main__':
    solution = Solution()
    nums = [3,2,1]
    solution.nextPermutation(nums)
    print(nums)
