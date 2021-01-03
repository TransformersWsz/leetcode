'''
@File  : first-missing-positive.py
@Author: Swift
@Date  : 2021/1/3 21:55
@Link  : https://leetcode-cn.com/problems/first-missing-positive/
@Desc  : 41. 缺失的第一个正数
@Method: https://leetcode-cn.com/problems/first-missing-positive/solution/tong-pai-xu-python-dai-ma-by-liweiwei1419/
'''

class Solution:
    def firstMissingPositive(self, nums):
        length = len(nums)
        for i in range(length):
            while 1 <= nums[i] <= length and nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

        for i in range(length):
            if nums[i] != i+1:
                return i+1
        return length+1


if __name__ == '__main__':
    obj = Solution()
    arr = [7,8,9,11,12]
    res = obj.firstMissingPositive(arr)
    print(res)