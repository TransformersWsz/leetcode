'''
@File  : majority-element.py
@Author: Swift
@Date  : 2021/1/4 15:12
@Link  : https://leetcode-cn.com/problems/majority-element/
@Desc  : 169. 多数元素
@Method: 
'''

class Solution:
    def majorityElement(self, nums):
        me = nums[0]
        count = 1
        length = len(nums)
        for i in range(1, length):
            if nums[i] == me:
                count += 1
            else:
                if count == 0:
                    me = nums[i]
                    count += 1
                else:
                    count -= 1
        return me


if __name__ == '__main__':
    obj = Solution()
    nums = [2,2,1,1,1,2,2]
    res = obj.majorityElement(nums)
    print(res)
