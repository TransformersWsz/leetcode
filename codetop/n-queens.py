'''
@File  : n-queens.py
@Author: Swift
@Date  : 2021/3/8 16:36
@Link  : https://leetcode-cn.com/problems/n-queens/
@Desc  : 51. N 皇后
@Method: https://leetcode-cn.com/problems/n-queens/solution/nhuang-hou-by-leetcode-solution/
'''


class Solution:
    def __init__(self):
        self.res = []
        self.column = set()
        self.dia1 = set()
        self.dia2 = set()

    def back_trace(self, row, n, tmp):
        for col in range(n):
            if col in self.column or col+row in self.dia1 or row-col in self.dia2:
                continue
            self.column.add(col)
            self.dia1.add(col+row)
            self.dia2.add(row-col)
            if row == n-1:
                self.res.append(tmp+[col])
            else:
                self.back_trace(row+1, n, tmp+[col])
            self.column.remove(col)
            self.dia1.remove(col+row)
            self.dia2.remove(row-col)

    def gen_board(self, n):
        boards = []
        for l in self.res:
            tmp = [ "."*n for _ in range(n) ]
            for idx, item in enumerate(l):
                _row = ["."]*n
                _row[item] = "Q"
                tmp[idx] = "".join(_row)
            boards.append(tmp)
        return boards

    def solveNQueens(self, n: int):
        self.back_trace(0, n, [])
        boards = self.gen_board(n)
        return boards


if __name__ == '__main__':
    solution = Solution()
    boards = solution.solveNQueens(4)
    print(boards)
