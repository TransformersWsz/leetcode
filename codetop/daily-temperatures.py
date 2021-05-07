'''
@File  : daily-temperatures.py
@Author: Swift
@Date  : 2021/5/7 14:26
@Link  : https://leetcode-cn.com/problems/daily-temperatures/
@Desc  : 739. 每日温度
@Method:
'''

class Solution:
    def dailyTemperatures(self, T):
        stack = []
        res = [0] * len(T)
        for idx, item in enumerate(T):
            if not stack:
                stack.append(idx)
            else:
                if T[stack[-1]] >= item:
                    stack.append(idx)
                else:
                    while stack and T[stack[-1]] < item:
                        top = stack.pop()
                        res[top] = idx - top
                    stack.append(idx)
        return res


if __name__ == '__main__':
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    solution = Solution()
    res = solution.dailyTemperatures(T)
    print(res)