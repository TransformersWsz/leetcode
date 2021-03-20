'''
@File  : JZ35_数组中的逆序对.py
@Author: Swift
@Date  : 2021/3/20 14:12
@Link  : https://www.nowcoder.com/practice/96bd6684e04a44eb80e6a68efc0ec6c5?tpId=13&tqId=11188&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P
@Method: 
'''

# -*- coding:utf-8 -*-
class Solution:
    def merge_sort(self, data,  left, right, tmp):
        if left >= right:
            return 0
        mid = (left+right)//2
        inverse_pairs = self.merge_sort(data, left, mid, tmp) + self.merge_sort(data, mid+1, right, tmp)
        i, j, pos = left, mid+1, left
        while i <= mid and j <= right:

            if data[i] <= data[j]:
                inverse_pairs += j-mid-1
                tmp[pos] = data[i]
                i += 1
            else:
                tmp[pos] = data[j]
                j += 1
            pos += 1

        for k in range(i, mid+1):
            tmp[pos] = data[k]
            pos += 1
            inverse_pairs += right - mid

        for k in range(j, right+1):
            tmp[pos] = data[k]
            pos += 1

        data[left:right+1] = tmp[left:right+1]
        return inverse_pairs


    def InversePairs(self, data):
        length = len(data)
        tmp = [0] * length
        res = self.merge_sort(data, 0, length-1, tmp)
        return res


if __name__ == '__main__':
    solution = Solution()
    data = [1,2,3,4,5,6,7,0]
    res = solution.InversePairs(data)
    print(res)