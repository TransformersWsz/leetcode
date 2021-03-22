'''
@File  : JZ41_和为S的连续正数序列.py
@Author: Swift
@Date  : 2021/3/22 23:00
@Link  : https://www.nowcoder.com/practice/c451a3fd84b64cb19485dad758a55ebe?tpId=13&tqId=11194&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
@Method: 
'''

# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):

        dp = [0]*(tsum+1)
        for item in range(1, tsum+1):
            dp[item] = dp[item-1]+item
        res = []
        i = 1
        j = 1
        while i <= tsum:
            if dp[i]-dp[j-1] == tsum:
                if i-j >= 1:
                    res.append(list(range(j,i+1)))
                j += 1
            elif dp[i]-dp[j-1] > tsum:
                j += 1
            else:
                i += 1
        return res