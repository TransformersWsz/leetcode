'''
@File  : JZ13_调整数组顺序使奇数位于偶数前面.py
@Author: Swift
@Date  : 2021/3/16 17:58
@Link  : https://www.nowcoder.com/practice/ef1f53ef31ca408cada5093c8780f44b?tpId=13&tqId=11166&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
@Method: 
'''


class Solution:
    def reOrderArray(self , array ):
        # write code here
        length = len(array)
        left = -1
        right = 0
        while right < length:
            if array[right]%2 == 1:
                temp = array[right]
                k = right
                while k > left:
                    array[k] = array[k-1]
                    k -= 1
                left += 1
                array[left] = temp
            right += 1
        return array