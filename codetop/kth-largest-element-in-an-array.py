'''
@File  : kth-largest-element-in-an-array.py
@Author: Swift
@Date  : 2020/12/17 21:21
@Link  : https://leetcode-cn.com/problems/kth-largest-element-in-an-array/
@Desc  : 215. 数组中的第K个最大元素
@Method: 
'''


class Solution:

    def qsort(self, nums, k):
        low = 0
        high = len(nums)-1
        pivot = nums[low]
        while low < high:
            while low < high and pivot <= nums[high]:
                high -= 1
            if low < high:
                nums[low] = nums[high]

            while low < high and pivot >= nums[low]:
                low += 1
            if low < high:
                nums[high] = nums[low]
        nums[low] = pivot
        res = None
        if low == k-1:
            res = nums[low]
        elif low > k-1:
            res = self.qsort(nums[0:low], k)
        else:
            res = self.qsort(nums[low+1:len(nums)], k-low-1)
        return res


    def findKthLargest(self, nums, k):
        res = self.qsort(nums, len(nums)-k+1)
        return res


if __name__ == '__main__':
    obj = Solution()
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    res = obj.findKthLargest(nums, k)
    print(res)