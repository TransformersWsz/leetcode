'''
@File  : JZ3_从尾到头打印链表.py
@Author: Swift
@Date  : 2021/3/16 17:53
@Link  : https://www.nowcoder.com/practice/d0267f7f55b3412ba93bd35cfa8e8035?tpId=13&tqId=11156&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
@Method: 
'''

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        res = []
        while listNode:
            res.insert(0, listNode.val)
            listNode = listNode.next
        return res