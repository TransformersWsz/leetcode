'''
@File  : largest-number.py
@Author: Swift
@Date  : 2021/4/26 11:23
@Link  : https://leetcode-cn.com/problems/largest-number/
@Desc  : 179. 最大数
@Method: 
'''

import functools

class Solution:
    def largestNumber(self, nums):
        def rule(x, y):
            x, y = x+y, y+x
            if x > y:
                return 1
            elif x < y:
                return -1
            else:
                return 0
        s = [ str(item) for item in nums ]
        s.sort(key=functools.cmp_to_key(rule), reverse=True)
        res = "".join(s)
        return "0" if res[0]=='0' else res


if __name__ == '__main__':
    solution = Solution()
    nums = [3,30,34,5,9]
    res = solution.largestNumber(nums)
    print(res)
