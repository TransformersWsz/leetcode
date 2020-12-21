'''
@File  : 3sum.py
@Author: Swift
@Date  : 2020/12/20 21:14
@Link  : https://leetcode-cn.com/problems/3sum/
@Desc  : 15. 三数之和
@Method: https://leetcode-cn.com/problems/3sum/solution/hua-jie-suan-fa-15-san-shu-zhi-he-by-guanpengchn/
'''


class Solution:
    def threeSum(self, nums):
        res = []
        if len(nums) < 3:
            return res
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    right -= 1
        return res


if __name__ == '__main__':
    obj = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    res = obj.threeSum(nums)
    print(res)
