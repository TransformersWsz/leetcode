'''
@File  : shortest-subarray-with-sum-at-least-k.py
@Author: Swift
@Date  : 2021/5/27 16:36
@Link  : https://leetcode-cn.com/problems/shortest-subarray-with-sum-at-least-k/
@Desc  : 862. 和至少为 K 的最短子数组
@Method: https://leetcode-cn.com/problems/shortest-subarray-with-sum-at-least-k/solution/python3-dui-qian-zhui-he-zuo-di-zeng-zha-otmq/
'''


class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        prefix = [0]
        stack = []
        for v in A:
            prefix.append(prefix[-1] + v)

        res = length = len(prefix)
        for i in range(length):
            while stack and prefix[i] - prefix[stack[0]] >= K:
                res = min(res, i - stack[0])
                stack.pop(0)
            while stack and prefix[i] <= prefix[stack[-1]]:
                stack.pop()
            stack.append(i)
        return res if res != length else -1