#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/7 5:46 PM
# @Author  : Swift
# @File    : diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof.py
# @Brief   : 剑指 Offer 21. 调整数组顺序使奇数位于偶数前面

class Solution:
    def exchange(self, nums):
        low = 0
        high = len(nums) - 1
        while low < high:
            while low < high and nums[low]%2 == 1:
                low += 1
            while low < high and nums[high]%2 == 0:
                high -= 1
            if low < high:
                nums[low], nums[high] = nums[high], nums[low]
                low += 1
                high -= 1
        return nums


if __name__ == '__main__':
    nums = [1,2,3,4]
    obj = Solution()
    res = obj.exchange(nums)
    print(res)
