'''
@File  : diagonal-traverse.py
@Author: Swift
@Date  : 2021/4/18 12:26
@Link  : https://leetcode-cn.com/problems/diagonal-traverse/
@Desc  : 498. 对角线遍历
@Method: 
'''

class Solution:
    def findDiagonalOrder(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        arr = []
        for j in range(cols):
            temp = []
            newi, newj = 0, j
            while 0 <= newi < rows and 0 <= newj < cols:
                temp.append(mat[newi][newj])
                newi += 1
                newj -= 1
            arr.append(temp)

        for i in range(1, rows):
            temp = []
            newi, newj = i, cols - 1
            while 0 <= newi < rows and 0 <= newj < cols:
                temp.append(mat[newi][newj])
                newi += 1
                newj -= 1
            arr.append(temp)

        res = []
        for idx, l in enumerate(arr):
            if idx % 2 == 1:
                res += l
            else:
                res += l[::-1]
        return res


if __name__ == '__main__':
    mat = [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ]
    solution = Solution()
    res = solution.findDiagonalOrder(mat)
    print(res)