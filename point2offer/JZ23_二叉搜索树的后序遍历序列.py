'''
@File  : JZ23_二叉搜索树的后序遍历序列.py
@Author: Swift
@Date  : 2021/3/29 16:24
@Link  : https://www.nowcoder.com/practice/a861533d45854474ac791d90e447bafd?tpId=13&tqId=11176&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 
@Method: 
'''


# -*- coding:utf-8 -*-
class Solution:
    def recur(self, arr, start, root):
        if start >= root:
            return True

        i = start
        while i < root:
            if arr[i] > arr[root]:
                break
            i += 1

        for j in range(i, root):
            if arr[j] < arr[root]:
                return False
        return self.recur(arr, start, i - 1) and self.recur(arr, i, root - 1)

    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence or len(sequence) == 0:
            return False
        return self.recur(sequence, 0, len(sequence) - 1)


