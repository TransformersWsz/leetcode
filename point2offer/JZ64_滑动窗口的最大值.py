'''
@File  : JZ64_滑动窗口的最大值.py
@Author: Swift
@Date  : 2021/4/9 23:51
@Link  : https://www.nowcoder.com/practice/1624bc35a45c42c0bc17d17fa0cba788?tpId=13&tqId=11217&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
@Desc  : 给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。窗口大于数组长度的时候，返回空
@Method: 
'''


# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if not num or not size or size > len(num):
            return []

        queue = []
        res = []
        for idx, item in enumerate(num):
            while queue and num[queue[-1]] < item:
                queue.pop()
            queue.append(idx)
            if idx - queue[0] + 1 > size:
                queue.pop(0)
            if idx + 1 >= size:
                res.append(num[queue[0]])
        return res