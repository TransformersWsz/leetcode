
from typing import List


import collections
import math

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for item in num:
            while k and stack and stack[-1] > item:
                stack.pop()
                k -= 1
            stack.append(item)
        if k:
            stack = stack[:-k]
        stack = "".join(stack).lstrip("0")
        return stack if stack else "0"


if __name__ == '__main__':
    solution = Solution()
    nums = "1234567890"
    k = 9
    res = solution.removeKdigits(nums,k)
    print(res)
