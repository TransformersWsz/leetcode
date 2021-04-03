'''
@File  : JZ40_数组中只出现一次的数字.py
@Author: Swift
@Date  : 2021/4/3 22:05
@Link  : https://www.nowcoder.com/practice/389fc1c3d3be4479a154f63f495abff8?tpId=13&tqId=11193&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
@Method: 
'''


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param array int整型一维数组
# @return int整型一维数组
#
class Solution:
    def FindNumsAppearOnce(self, array):
        # write code here
        ab = 0
        for item in array:
            ab = ab ^ item
        sep = 1
        while sep & ab == 0:
            sep = sep << 1

        a, b = 0, 0
        for item in array:
            if item & sep:
                a = a ^ item
            else:
                b = b ^ item
        return [a, b] if a < b else [b, a]
