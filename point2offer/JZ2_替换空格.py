'''
@File  : JZ2_替换空格.py
@Author: Swift
@Date  : 2021/3/16 17:52
@Link  : https://www.nowcoder.com/practice/0e26e5551f2b489b9f58bc83aa4b6c68?tpId=13&tqId=11155&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
@Method: 
'''


class Solution:
    def replaceSpace(self, s):
        return s.replace(" ", "%20")
