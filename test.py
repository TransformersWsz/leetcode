
from typing import List


import collections
import math


class Solution:
    def __init__(self):
        self.count = 0

    def dfs(self, isConnected, i, isVisited):
        for j in range(len(isConnected[i])):
            if not isVisited[j] and isConnected[i][j]:
                isVisited[j] = True
                self.dfs(isConnected, j, isVisited)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        num = len(isConnected)
        isVisited = [False] * num
        for i in range(num):
            if not isVisited[i]:
                self.dfs(isConnected, i, isVisited)
                self.count += 1
        return self.count


if __name__ == '__main__':
    solution = Solution()
    isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    res = solution.findCircleNum(isConnected)
    print(res)
