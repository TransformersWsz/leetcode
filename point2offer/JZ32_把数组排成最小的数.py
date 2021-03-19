'''
@File  : JZ32_把数组排成最小的数.py
@Author: Swift
@Date  : 2021/3/19 14:56
@Link  : https://www.nowcoder.com/practice/8fecd3f8ba334add803bf2a06af1b993?tpId=13&tqId=11185&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
@Method: 
'''

import functools


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def sort_rule(x, y):    # [30, 3], min=303
            a, b = x + y, y + x    # "330" > "303", 不能直接x>y
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                return 0

        strs = [str(num) for num in nums]
        res = sorted(strs, key=functools.cmp_to_key(sort_rule))

        return ''.join(res)
