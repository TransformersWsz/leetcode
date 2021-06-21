
from typing import List


import collections
import math


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res = None
        for item in nums:
            if nums[abs(item)] < 0:
                res = abs(item)
            else:
                nums[abs(item)] = -nums[abs(item)]

        for idx, item in enumerate(nums):
            nums[idx] = abs(item)
        return res


if __name__ == '__main__':
    solution = Solution()
    nums = [1,3,4,2,2]
    res = solution.findDuplicate(nums)
    print(res)
