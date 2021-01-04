'''
@File  : spiral-matrix.py
@Author: Swift
@Date  : 2021/1/4 21:20
@Link  : https://leetcode-cn.com/problems/spiral-matrix/
@Desc  : 54. 螺旋矩阵
@Method: https://leetcode-cn.com/problems/spiral-matrix/comments/
'''


class Solution:
    def spiralOrder(self, matrix):
        if not matrix or len(matrix) == 0:
            return []
        l = 0
        r = len(matrix[0]) - 1
        u = 0
        d = len(matrix) - 1
        res = []
        while l <= r and u <= d:
            for i in range(l, r + 1):
                res.append(matrix[u][i])

            u += 1
            for i in range(u, d + 1):
                res.append(matrix[i][r])

            r -= 1
            i = r
            while i >= l and u <= d:
                res.append(matrix[d][i])
                i -= 1

            d -= 1
            i = d
            while i >= u and l <= r:
                res.append(matrix[i][l])
                i -= 1
            l += 1
        return res


if __name__ == '__main__':
    obj = Solution()
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    res = obj.spiralOrder(matrix)
    print(res)
