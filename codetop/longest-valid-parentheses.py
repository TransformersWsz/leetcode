'''
@File  : longest-valid-parentheses.py
@Author: Swift
@Date  : 2020/1/5 16:04
@Link  : https://leetcode-cn.com/problems/longest-valid-parentheses/
@Desc  : 32. 最长有效括号
@Method: https://leetcode-cn.com/problems/longest-valid-parentheses/comments/
'''

class Solution:
    def get_longest_zeros(self, arr):
        length = len(arr)
        dp = [0] * (length+1)
        res = 0
        for i in range(1, length+1):
            if arr[i-1] == 0:
                dp[i] = dp[i-1] + 1
                res = max(res, dp[i])
            else:
                dp[i] = 0
        return res

    def longestValidParentheses(self, s: str) -> int:
        length = len(s)
        arr = [1] * length
        stack = []
        for idx, c in enumerate(s):
            if stack and stack[-1][0] == "(" and c == ")":
                arr[stack[-1][1]] = 0
                arr[idx] = 0
                stack.pop(-1)
            else:
                stack.append((c, idx))
        res = self.get_longest_zeros(arr)
        return res


if __name__ == '__main__':
    obj = Solution()
    s = "(()(()"
    res = obj.longestValidParentheses(s)
    print(res)

