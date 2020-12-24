'''
@File  : number-of-islands-shen-du-you-xian-bian-li-dfs-or-.py
@Author: Swift
@Date  : 2020/12/24 11:43
@Link  : https://leetcode-cn.com/problems/number-of-islands/
@Desc  : 200. 岛屿数量
@Method: https://leetcode-cn.com/problems/number-of-islands/solution/number-of-islands-shen-du-you-xian-bian-li-dfs-or-/
'''


class Solution:
    def dfs(self, grid, i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1":
            grid[i][j] = "0"
            self.dfs(grid, i-1, j)
            self.dfs(grid, i+1, j)
            self.dfs(grid, i, j-1)
            self.dfs(grid, i, j+1)
        else:
            return None

    def numIslands(self, grid):
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    count += 1
        return count

if __name__ == '__main__':
    obj = Solution()
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    res = obj.numIslands(grid)
    print(res)