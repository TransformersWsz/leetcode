'''
@File  : jump-game.py
@Author: Swift
@Date  : 2021/5/7 15:40
@Link  : https://leetcode-cn.com/problems/jump-game/
@Desc  : 55. 跳跃游戏
@Method: https://leetcode-cn.com/problems/jump-game/solution/tiao-yue-you-xi-by-leetcode-solution/
'''

class Solution:
    def canJump(self, nums) -> bool:
        length, right_most = len(nums), 0
        for i in range(length):
            if i <= right_most:
                right_most = max(right_most, i+nums[i])
                if right_most >= length-1:
                    return True
        return False