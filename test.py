
from typing import List


import collections
import math

class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        dp0 = [0]*length
        dp1 = [0]*length
        dp1[0] = nums[0]
        for i in range(1, length):
            dp0[i] = max(dp0[i-1], dp0[i-2]+nums[i])
            if i != length - 1:
                dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i])
            else:
                dp1[i] = dp1[i-1]
        return max(dp0[length - 1], dp1[length-1])


if __name__ == '__main__':
    solution = Solution()
    nums = [0]
    res = solution.rob(nums)
    print(res)
