'''
@File  : shu-zu-zhong-de-ni-xu-dui-lcof.py
@Author: Swift
@Date  : 2021/3/11 17:22
@Link  : https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/
@Desc  : 剑指 Offer 51. 数组中的逆序对
@Method: https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/solution/shu-zu-zhong-de-ni-xu-dui-by-leetcode-solution/
'''


class Solution:
    def merge_sort(self, nums, tmp, left, right):
        if left >= right:
            return 0
        mid = (left + right) // 2
        inv_count = self.merge_sort(nums, tmp, left, mid) + self.merge_sort(nums, tmp, mid + 1, right)
        i, j, pos = left, mid + 1, left
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                inv_count += j - mid - 1
                tmp[pos] = nums[i]
                i += 1
            else:
                tmp[pos] = nums[j]
                j += 1
            pos += 1

        for k in range(i, mid + 1):
            inv_count += j - mid - 1
            tmp[pos] = nums[k]
            pos += 1

        for k in range(j, right + 1):
            tmp[pos] = nums[k]
            pos += 1
        nums[left:right + 1] = tmp[left:right + 1]
        return inv_count

    def reversePairs(self, nums: List[int]) -> int:
        length = len(nums)
        tmp = [0] * length
        res = self.merge_sort(nums, tmp, 0, length - 1)
        return res
