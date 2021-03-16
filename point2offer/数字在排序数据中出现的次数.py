'''
@File  : 数字在排序数据中出现的次数.py
@Author: Swift
@Date  : 2021/3/16 18:01
@Link  : https://www.nowcoder.com/practice/70610bf967994b22bb1c26f9ae901fa2?tpId=13&tqId=11190&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 统计一个数字在升序数组中出现的次数。
@Method: 
'''

# -*- coding:utf-8 -*-
class Solution:
    def find_nolessthan(self, data, target):
        low = 0
        high = len(data)-1
        res = -1
        while low < high:
            mid = (low+high)//2
            if target <= data[mid]:
                res = mid
                high = mid
            else:
                low = mid+1
        return res

    def binary_search(self, data, target):
        low = 0
        high = len(data) - 1
        res = -1
        while low <= high:
            mid = (low + high) // 2
            if target >= data[mid]:
                low = mid+1
            else:
                high = mid - 1
        return low

    def GetNumberOfK(self, data, k):
        right = self.binary_search(data, k+0.5)
        left = self.binary_search(data, k-0.5)
        return right-left