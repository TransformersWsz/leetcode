'''
@File  : JZ53_表示数值的字符串.py
@Author: Swift
@Date  : 2021/4/7 11:54
@Link  : https://www.nowcoder.com/practice/e69148f8528c4039ad89bb2546fd4ff8?tpId=13&tqId=11206&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
@Method: 
'''

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param str string字符串
# @return bool布尔型
#
class Solution:
    def isNumeric(self , s ):
        # write code here
        hasE = False
        dot = False
        for idx, c in enumerate(s):
            if c >= '0' and c <= '9':
                pass
            elif c in ["+", "-"]:
                if idx != 0 and s[idx-1] not in ["E", "e"]:
                    return False
                if idx == len(s)-1 or s[idx+1] in ["E", "e"]:
                    return False
            elif c in ["E", "e"]:
                if hasE or idx in [0, len(s)-1]:
                    return False
                hasE = True
            elif c == ".":
                if hasE:
                    return False
                if dot:
                    return False
                if idx == len(s)-1:
                    return False
                dot = True
            else:
                return False
        return True