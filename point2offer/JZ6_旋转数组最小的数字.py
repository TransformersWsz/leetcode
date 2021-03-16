'''
@File  : JZ6_旋转数组最小的数字.py
@Author: Swift
@Date  : 2021/3/16 17:55
@Link  : https://www.nowcoder.com/practice/9f3231a991af4f55b95579b44b7a01ba?tpId=13&tqId=11159&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
@Method: 
'''

# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0
        low = 0
        high = len(rotateArray)-1
        while low < high:
            mid = (high + low) // 2
            if rotateArray[mid] < rotateArray[high]:
                high = mid
            elif rotateArray[mid] > rotateArray[high]:
                low = mid + 1
            else:
                high -= 1
        return rotateArray[low]