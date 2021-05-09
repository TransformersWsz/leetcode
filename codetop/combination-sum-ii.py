'''
@File  : combination-sum-ii.py
@Author: Swift
@Date  : 2021/5/9 20:51
@Link  : https://leetcode-cn.com/problems/combination-sum-ii/
@Desc  : 40. 组合总和 II
@Method: https://leetcode-cn.com/problems/combination-sum-ii/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-m-3/
'''


class Solution:
    def __init__(self):
        self.res = []

    def dfs(self, candidates, target, start, temp):
        if target == 0:
            self.res.append(temp)
        else:
            if target > 0:
                length = len(candidates)
                for idx in range(start, length):
                    if idx > start and candidates[idx] == candidates[idx - 1]:
                        pass
                    else:
                        self.dfs(candidates, target - candidates[idx], idx + 1, temp + [candidates[idx]])

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.dfs(candidates, target, 0, [])
        return self.res
