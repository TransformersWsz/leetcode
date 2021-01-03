'''
@File  : search-a-2d-matrix-ii.py
@Author: Swift
@Date  : 2021/1/3 22:25
@Link  : https://leetcode-cn.com/problems/search-a-2d-matrix-ii/
@Desc  : 240. 搜索二维矩阵 II
@Method: https://leetcode-cn.com/problems/search-a-2d-matrix-ii/comments/
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        if rows == 0:
            return False
        cols = len(matrix[0])
        i = rows-1
        j = 0
        while i >= 0 and j <= cols-1:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                i = i-1
            else:
                j += 1
        return False

