'''
@File  : count-submatrices-with-all-ones.py
@Author: Swift
@Date  : 2020/12/7 23:27
@Link  : https://leetcode-cn.com/problems/count-submatrices-with-all-ones/
@Desc  : 统计全 1 子矩形
@Method: https://blog.csdn.net/weixin_45333934/article/details/107835404
'''

class Solution:

    def leftMaxOne(self, nums):
        row = len(nums)
        col = len(nums[0])
        arr = [ [0]*(col+1) for _ in range(row+1)]
        for i in range(1, row+1):
            for j in range(1, col+1):
                arr[i][j] = arr[i][j-1]+1 if nums[i-1][j-1]==1 else 0
        return arr

    def get_sum(self, mat):
        sum = 0
        for row in mat:
            for col in row:
                sum += col
        return sum

    def numSubmat(self, mat):
        dp = self.leftMaxOne(mat)
        res = 0
        sum_mat = self.get_sum(mat)
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                min_col = sum_mat
                for k in range(i, -1, -1):
                    if dp[k+1][j+1] == 0:
                        break
                    else:
                        min_col = min(min_col, dp[k+1][j+1])
                        res += min_col
        return res


if __name__ == '__main__':
    obj = Solution()
    mat = [[1, 0, 1],
           [1, 1, 0],
           [1, 1, 0]]
    res = obj.numSubmat(mat)
    print(res)