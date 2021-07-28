'''
@File  : word-search.py
@Author: Swift
@Date  : 2021/3/8 22:57
@Link  : https://leetcode-cn.com/problems/word-search/
@Desc  : 79. 单词搜索
@Method: https://leetcode-cn.com/problems/word-search/solution/dan-ci-sou-suo-by-leetcode-solution/
'''

# -*- coding:utf-8 -*-
class Solution:
    def dfs(self, i, j, k, visited, board, word):
        if board[i][j] == word[k]:
            if k == len(word)-1:
                return True
            visited[i][j] = True
            direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            result = False
            for di, dj in direction:
                newi = i + di
                newj = j + dj
                if 0 <= newi < len(board) and 0 <= newj < len(board[0]) and not visited[newi][newj]:
                    if self.dfs(newi, newj, k+1, visited, board, word):
                        result = True
                        break
            visited[i][j] = False
            return result
        else:
            return False

    def exist(self, board, word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = [ [False]*cols for _ in range(rows) ]
        for i in range(rows):
            for j in range(cols):
                if self.dfs(i, j, 0, visited, board, word):
                    return True
        return False



if __name__ == '__main__':
    solution = Solution()
    data = [1,1,1,1,1, 2,3,3,3,9]
    k = 3
    res = solution.search(data, 1)
    print(res)