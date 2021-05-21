'''
@File  : candy.py
@Author: Swift
@Date  : 2021/5/21 13:57
@Link  : https://leetcode-cn.com/problems/candy/
@Desc  : 135. 分发糖果
@Method: 
'''

class Solution:
    def candy(self, ratings: List[int]) -> int:
        length = len(ratings)
        ret = [1]*length
        for i in range(length):
            if i > 0 and ratings[i] > ratings[i-1]:
                ret[i] = ret[i-1] + 1

        for i in range(length-1, -1, -1):
            if i < length-1 and ratings[i] > ratings[i+1]:
                ret[i] = max(ret[i], ret[i+1]+1)

        return sum(ret)