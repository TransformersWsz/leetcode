'''
@File  : remove-all-adjacent-duplicates-in-string.py
@Author: Swift
@Date  : 2021/5/5 15:01
@Link  : https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string/
@Desc  : 1047. 删除字符串中的所有相邻重复项
@Method: 
'''

class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for c in S:
            if not stack or stack[-1] != c:
                stack.append(c)
            else:
                stack.pop()
        return "".join(stack)


if __name__ == '__main__':
    solution = Solution()
    S = "abbaca"
    res = solution.removeDuplicates(S)
    print(res)







