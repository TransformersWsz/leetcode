'''
@File  : spiral-matrix-ii.py
@Author: Swift
@Date  : 2021/4/17 14:52
@Link  : https://leetcode-cn.com/problems/spiral-matrix-ii/
@Desc  : 59. 螺旋矩阵 II
@Method: 
'''

class Solution:
    def traverse(self, arr):
        rows = len(arr)
        cols = len(arr[0])
        left, right, top, bottom = 0, cols-1, 0, rows-1
        count = 1
        while True:
            for col in range(left, right+1):
                arr[top][col] = count
                count += 1
            top += 1
            if top > bottom:
                break

            for row in range(top, bottom+1):
                arr[row][right] = count
                count += 1
            right -= 1
            if left > right:
                break

            for col in range(right, left-1, -1):
                arr[bottom][col] = count
                count += 1
            bottom -= 1
            if top > bottom:
                break

            for row in range(bottom, top-1, -1):
                arr[row][left] = count
                count += 1
            left += 1
            if left > right:
                break

    def generateMatrix(self, n: int):
        arr = [ [0]*n for _ in range(n) ]
        self.traverse(arr)
        return arr


if __name__ == '__main__':
    solution = Solution()
    arr = solution.generateMatrix(3)
    print(arr)