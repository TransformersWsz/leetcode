'''
@File  : JZ33_丑数.py
@Author: Swift
@Date  : 2021/3/24 21:54
@Link  : https://www.nowcoder.com/practice/6aa9e04fc3794f68acf8778237ba065b?tpId=13&tqId=11186&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
@Method: https://leetcode-cn.com/problems/chou-shu-lcof/solution/mian-shi-ti-49-chou-shu-dong-tai-gui-hua-qing-xi-t/
'''

# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        dp = [1]*index
        a, b, c = 0, 0, 0
        for i in range(1, index):
            n1, n2, n3 = dp[a]*2, dp[b]*3, dp[c]*5
            dp[i] = min(n1, n2, n3)
            if dp[i] == n1:
                a += 1
            if dp[i] == n2:
                b += 1
            if dp[i] == n3:
                c += 1
        return dp[-1]

