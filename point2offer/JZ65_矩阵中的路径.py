#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param matrix char字符型二维数组
# @param word string字符串
# @return bool布尔型
#
class Solution:
    def dfs(self, matrix, i, j, k, word, visited):
        if matrix[i][j] == word[k]:
            if k == len(word) - 1:
                return True
            visited[i][j] = True
            direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            flag = False
            for pair in direction:
                newi, newj = i + pair[0], j + pair[1]
                if 0 <= newi < len(matrix) and 0 <= newj < len(matrix[0]) and not visited[newi][newj]:
                    if self.dfs(matrix, newi, newj, k + 1, word, visited):
                        flag = True
                        break
            visited[i][j] = False
            return flag
        else:
            return False

    def hasPath(self, matrix, word):
        # write code here
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        visited = [[False] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if self.dfs(matrix, i, j, 0, word, visited):
                    return True
        return False

if __name__ == '__main__':
    solution = Solution()
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    res = solution.hasPath(board, "ABCB")
    print(res)