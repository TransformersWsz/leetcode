'''
@File  : JZ63_数据流中的中位数.py
@Author: Swift
@Date  : 2021/4/7 11:56
@Link  : https://www.nowcoder.com/practice/9be0172896bd43948f8a32fb954e1be1?tpId=13&tqId=11216&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。
@Method:
'''


# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.arr = []

    def Insert(self, num):
        # write code here
        if not self.arr or self.arr[-1] <= num:
            self.arr.append(num)
        else:
            self.arr.append(0)
            length = len(self.arr)
            i = length - 2
            while i >= 0:
                if num < self.arr[i]:
                    self.arr[i + 1] = self.arr[i]
                else:
                    break
                i -= 1
            self.arr[i + 1] = num

    def GetMedian(self):
        # write code here

        length = len(self.arr)
        if length % 2 == 1:
            return self.arr[length // 2]
        return (self.arr[length // 2 - 1] + self.arr[length // 2]) / 2


if __name__ == '__main__':
    arr = [5,2,3,4,1,6,7,0,8]
    solution = Solution()
    for num in arr:
        solution.Insert(num)
        print(solution.GetMedian())