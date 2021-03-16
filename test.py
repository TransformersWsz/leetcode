#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param array int整型一维数组
# @return int整型一维数组
#
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


if __name__ == '__main__':
    solution = Solution()
    arr = [1, 2, 3, 3, 3]
    res = solution.GetNumberOfK(arr, 3)
    print(res)