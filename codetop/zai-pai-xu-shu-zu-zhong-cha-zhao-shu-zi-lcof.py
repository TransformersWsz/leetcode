'''
@File  : zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof.py
@Author: Swift
@Date  : 2021/5/6 19:58
@Link  : https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/
@Desc  : 剑指 Offer 53 - I. 在排序数组中查找数字 I
@Method: 
'''


class Solution:
    def findnoleethan(self, nums, target):
        low = 0
        high = len(nums) - 1
        res = len(nums)
        while low <= high:
            mid = (low + high) // 2
            if target <= nums[mid]:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res

    def findgreaterthan(self, nums, target):
        low = 0
        high = len(nums) - 1
        res = len(nums)
        while low <= high:
            mid = (low + high) // 2
            if target < nums[mid]:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res

    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        left = self.findnoleethan(nums, target)
        if left == length:
            return 0
        right = self.findgreaterthan(nums, target)

        return right - left if right >= left else 0
