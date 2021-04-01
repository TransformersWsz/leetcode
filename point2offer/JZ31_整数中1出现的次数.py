'''
@File  : JZ31_整数中1出现的次数.py
@Author: Swift
@Date  : 2021/4/1 23:43
@Link  : https://www.nowcoder.com/practice/bd7f978302044eee894445e244c7eee6?tpId=13&tqId=11184&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
@Method: https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof/solution/zi-jie-ti-ku-jian-43-kun-nan-1n-zheng-shu-zhong-1-/
'''


# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        digit = 1
        count = 0
        high, low, cur = n // 10, 0, n % 10
        while high != 0 or cur != 0:
            if cur == 0:
                count += high * digit
            elif cur == 1:
                count += high * digit + low + 1
            else:
                count += (high + 1) * digit

            low += cur * digit
            cur = high % 10
            high = high // 10
            digit *= 10
        return count