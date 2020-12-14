'''
@File  : filling-bookcase-shelves.py
@Author: Swift
@Date  : 2020/12/11 17:07
@Link  : https://leetcode-cn.com/problems/filling-bookcase-shelves/
@Desc  : 填充书架
@Method: https://blog.csdn.net/qq_17550379/article/details/94341514
'''


class Solution:
    def minHeightShelves(self, books, shelf_width):
        n = len(books)
        mem = [float("inf")] * (n + 1)
        mem[0] = 0

        for i in range(1, n + 1):
            w, h = 0, 0
            for j in range(i - 1, -1, -1):
                w += books[j][0]
                h = max(h, books[j][1])
                if w > shelf_width:
                    break
                mem[i] = min(mem[i], mem[j] + h)
        return mem[-1]


if __name__ == '__main__':
    obj = Solution()
    books = [[2, 1], [3, 3]]
    shelf_width = 4
    res = obj.minHeightShelves(books, shelf_width)
    print(res)
