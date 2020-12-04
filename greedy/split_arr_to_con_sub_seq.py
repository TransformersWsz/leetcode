'''
@File  : split_arr_to_con_sub_seq.py
@Author: Swift
@Date  : 2020/12/4 21:29
@Link  : https://leetcode-cn.com/problems/split-array-into-consecutive-subsequences/
@Desc  : 分割数组为连续子序列
@Method: https://blog.csdn.net/peakmoment/article/details/105416544
'''


import collections

class Solution(object):

    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = collections.Counter(nums)
        tail = collections.Counter()
        for item in nums:
            if count[item] == 0:
                continue
            elif tail[item] > 0:
                count[item] -= 1
                tail[item] -= 1
                tail[item+1] += 1
            elif count[item+1] > 0 and count[item+2] > 0:
                count[item] -= 1
                count[item+1] -= 1
                count[item+2] -= 1
                tail[item+3] += 1
            else:
                return False
        return True


if __name__ == '__main__':
    obj = Solution()
    nums = [1, 2, 3, 4, 4, 5]
    res = obj.isPossible(nums)
    print(res)
