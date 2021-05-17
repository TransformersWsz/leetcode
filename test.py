from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def dfs(self, nums, temp, visited):
        if len(temp) == len(nums):
            self.res.append(temp)
        else:
            length = len(nums)
            for i in range(length):
                if visited[i] or (i > 0 and nums[i]==nums[i-1] and not visited[i-1]):
                    continue
                visited[i] = True
                self.dfs(nums, temp + [nums[i]], visited)
                visited[i] = False

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        visited = [False] * length
        nums.sort()
        self.dfs(nums, [], visited)
        return self.res


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 1, 2]
    res = solution.permuteUnique(nums)
    print(res)