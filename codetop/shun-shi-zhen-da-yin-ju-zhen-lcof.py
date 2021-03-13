'''
@File  : shun-shi-zhen-da-yin-ju-zhen-lcof.py
@Author: Swift
@Date  : 2021/3/13 21:41
@Link  : https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/
@Desc  : 剑指 Offer 29. 顺时针打印矩阵
@Method: https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/solution/mian-shi-ti-29-shun-shi-zhen-da-yin-ju-zhen-she-di/
'''

class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        rows = len(matrix)
        cols = len(matrix[0])
        left, right, top, bottom = 0, cols-1, 0, rows-1
        res = []
        while True:
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top += 1
            if top > bottom:
                break

            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right -= 1
            if left > right:
                break

            for i in range(right, left-1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            if top > bottom:
                break

            for i in range(bottom, top-1, -1):
                res.append(matrix[i][left])
            left += 1
            if left > right:
                break
        return res



if __name__ == '__main__':
    solution = Solution()
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    res = solution.spiralOrder(matrix)
    print(res)