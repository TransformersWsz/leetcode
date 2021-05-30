'''
@File  : search-a-2d-matrix.py
@Author: Swift
@Date  : 2021/5/29 15:41
@Link  : https://leetcode-cn.com/problems/search-a-2d-matrix/
@Desc  : 74. 搜索二维矩阵
@Method: 
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        i, j = rows-1, 0
        while i >= 0 and j < cols:
            if target == matrix[i][j]:
                return True
            elif target > matrix[i][j]:
                j += 1
            else:
                i -= 1
        return False