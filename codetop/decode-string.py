'''
@File  : decode-string.py
@Author: Swift
@Date  : 2021/5/3 19:57
@Link  : https://leetcode-cn.com/problems/decode-string/
@Desc  : 394. 字符串解码
@Method:
'''

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                temp = []
                while stack[-1] != "[":
                    temp.append(stack.pop())
                temp = "".join(temp[::-1])
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k += stack.pop()
                k = int(k[::-1])
                temp = "".join([temp]*k)
                stack.append(temp)
        return "".join(stack)


if __name__ == '__main__':
    solution = Solution()
    s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
    res = solution.decodeString(s)
    print(res)