'''
@File  : sliding-window-maximum.py
@Author: Swift
@Date  : 2021/3/9 16:42
@Link  : https://leetcode-cn.com/problems/sliding-window-maximum/
@Desc  : 239. 滑动窗口最大值
@Method: 
'''

class Solution:
    def maxSlidingWindow(self, nums, k: int):
        queue = []
        res = []
        for idx, item in enumerate(nums):
            while queue and nums[queue[-1]] < item:
                queue.pop()
            queue.append(idx)
            if idx-queue[0]+1 > k:
                queue.pop(0)
            if idx+1 >= k:
                res.append(nums[queue[0]])
        return res


if __name__ == '__main__':
    solution = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    res = solution.maxSlidingWindow(nums, k)
    print(res)

