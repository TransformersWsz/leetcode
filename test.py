'''
@File  : JZ23_二叉搜索树的后序遍历序列.py
@Author: Swift
@Date  : 2021/3/29 16:24
@Link  :
@Desc  :
@Method:
'''

class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        #找到跟节点
        root = sequence[- 1]
        i = 0
        #找到左子树和右子树的分界点
        while i < len(sequence) - 1:
            if sequence[i] > root:
                break
            i += 1
        for j in range(i,len(sequence)-1):
            if sequence[j] < root:
                return False
        left = True
        right = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[:i])
        if i < len(sequence) - 1:
            right = self.VerifySquenceOfBST(sequence[i:len(sequence) - 1])
        return left and right

print("dsad")