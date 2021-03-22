'''
@File  : JZ11_二进制中1的个数.py
@Author: Swift
@Date  : 2021/3/22 22:10
@Link  : https://www.nowcoder.com/practice/8ee967e43c2c4ec193b040ea7fbb10b8?tpId=13&tqId=11164&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 输入一个整数，输出该数32位二进制表示中1的个数。其中负数用补码表示。
@Method: 
'''

# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        ret = sum(1 for i in range(32) if n & (1 << i))
        return ret




if __name__ == '__main__':
    solution = Solution()
    res = solution.NumberOf1(7)
    print(res)
