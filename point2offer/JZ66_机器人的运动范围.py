'''
@File  : JZ66_机器人的运动范围.py
@Author: Swift
@Date  : 2021/3/25 13:15
@Link  : https://www.nowcoder.com/practice/6e5207314b5241fb83f2329e89fdecc8?tpId=13&tqId=11219&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
@Method: 
'''


# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.count = 0

    def get_sum(self, n):
        res = 0
        while n:
            res += n % 10
            n = n // 10
        return res

    def dfs(self, arr, i, j, threshold):
        if 0 <= i < len(arr) and 0 <= j < len(arr[0]):
            if arr[i][j] == 1:
                if self.get_sum(i) + self.get_sum(j) <= threshold:
                    self.count += 1
                    arr[i][j] = 0
                    self.dfs(arr, i + 1, j, threshold)
                    self.dfs(arr, i - 1, j, threshold)
                    self.dfs(arr, i, j + 1, threshold)
                    self.dfs(arr, i, j - 1, threshold)
                else:
                    arr[i][j] = 0

    def movingCount(self, threshold, rows, cols):
        arr = [[1] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if arr[i][j] == 1:
                    self.dfs(arr, i, j, threshold)
        return self.count


if __name__ == '__main__':
    threshold = 10
    rows, cols = 1, 100
    s = Solution()
    res = s.movingCount(threshold, rows, cols)
    print(res)
