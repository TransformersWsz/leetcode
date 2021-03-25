'''
@File  : JZ65_矩阵中的路径.py
@Author: Swift
@Date  : 2021/3/25 14:26
@Link  : https://www.nowcoder.com/practice/69fe7a584f0a445da1b6652978de5c38?tpId=13&tqId=11218&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。
@Method:
'''

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param matrix string字符串
# @param rows int整型
# @param cols int整型
# @param str string字符串
# @return bool布尔型
#
class Solution:
    def construct(self, matrix, rows, cols):
        arr = [[None]*cols for _ in range(rows)]
        for idx, c in enumerate(matrix):
            arr[idx//cols][idx%cols] = c
        return arr


    def hasPath(self, matrix, rows, cols, word):
        arr = self.construct(matrix, rows, cols)
        return arr
        # write code here

if __name__ == '__main__':
    s = Solution()
    matrix = "ABCESFCSADEE"
    rows, cols = 3, 4
    word = "ABCCED"
    arr = s.construct(matrix, rows, cols)
    print(arr)