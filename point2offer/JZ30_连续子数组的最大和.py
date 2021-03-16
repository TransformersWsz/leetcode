'''
@File  : JZ30_连续子数组的最大和.py
@Author: Swift
@Date  : 2021/3/16 18:00
@Link  : https://www.nowcoder.com/practice/459bd355da1549fa8a49e350bf3df484?tpId=13&tqId=11183&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。要求时间复杂度为 O(n).
@Method: 
'''

# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        length = len(array)
        dp = [0]*(length+1)
        res = float('-inf')
        for idx, item in enumerate(array):
            dp[idx+1] = max(dp[idx]+item, item)
            res = max(res, dp[idx+1])
        return res