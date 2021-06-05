
from typing import List


import collections
import math


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        accum = length*(length+1)//2
        for item in nums:
            accum -= item
        return accum



if __name__ == '__main__':
    solution = Solution()
    A = [2,0]
    res = solution.missingNumber(A)
    print(res)
