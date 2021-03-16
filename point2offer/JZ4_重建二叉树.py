'''
@File  : JZ4_重建二叉树.py
@Author: Swift
@Date  : 2021/3/16 17:53
@Link  : https://www.nowcoder.com/practice/8a19cbe657394eeaac2f6ea9b0f6fcf6?tpId=13&tqId=11157&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
@Method: 
'''


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre:
            return None
        val = pre[0]
        root = TreeNode(val)
        idx = tin.index(val)
        root.left = self.reConstructBinaryTree(pre[1:idx + 1], tin[:idx])
        root.right = self.reConstructBinaryTree(pre[idx + 1:], tin[idx + 1:])
        return root
