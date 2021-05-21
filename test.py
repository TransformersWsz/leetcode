
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        length = len(ratings)
        ret = [1]*length
        for i in range(length):
            if i > 0 and ratings[i] > ratings[i-1]:
                ret[i] = ret[i-1] + 1

        for i in range(length-1, -1, -1):
            if i < length-1 and ratings[i] > ratings[i+1]:
                ret[i] = max(ret[i], ret[i+1]+1)

        return sum(ret)


if __name__ == '__main__':
    solution = Solution()
    obstacleGrid = [1,2,87,87,87,2,1]
    res = solution.candy(obstacleGrid)
    print(res)