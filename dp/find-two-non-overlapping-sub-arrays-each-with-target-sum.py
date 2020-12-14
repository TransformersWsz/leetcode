'''
@File  : find-two-non-overlapping-sub-arrays-each-with-target-sum.py
@Author: Swift
@Date  : 2020/12/14 22:06
@Link  : https://leetcode-cn.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/
@Desc  : 1477. 找两个和为目标值且不重叠的子数组
@Method: 
'''

class Solution:
    def minSumOfLengths(self, arr, target):
        length = len(arr)
        dp = [2 * length] * (length + 1)
        res = 2 * length
        l, r, s = 0, 0, 0
        while r < length:
            dp[r + 1] = dp[r]
            s += arr[r]
            while s > target:
                s -= arr[l]
                l += 1

            if s == target:
                dp[r + 1] = min(dp[r], r - l + 1)
                res = min(res, dp[l] + r - l + 1)
            r += 1
        res = -1 if res == 2 * length else res
        return res




if __name__ == '__main__':
    obj = Solution()
    arr = [3, 3]
    target = 3
    res = obj.minSumOfLengths(arr, target)
    print(res)
