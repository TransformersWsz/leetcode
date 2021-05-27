
from typing import List


import collections
import math


class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        prefix = [0]
        for v in A:
            prefix.append(prefix[-1] + v)
        que = collections.deque()
        res = math.inf
        for i in range(len(prefix)):
            while que and prefix[i] - prefix[que[0]] >= K:
                res = min(res, i - que[0])
                que.popleft()
            while que and prefix[i] <= prefix[que[-1]]:
                que.pop()
            que.append(i)
        return res if res != math.inf else -1



if __name__ == '__main__':
    solution = Solution()
    A = [10, -5, 15]
    K = 15
    res = solution.shortestSubarray(A, K)
    print(res)
