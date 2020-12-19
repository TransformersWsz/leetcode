'''
@File  : create-maximum-number.py
@Author: Swift
@Date  : 2020/12/15 11:19
@Link  : https://leetcode-cn.com/problems/create-maximum-number/
@Desc  : 321. 拼接最大数
@Method: https://zhuanlan.zhihu.com/p/90906054
'''

class Solution:

    def get_max_num_subseq(self, arr, i):
        stack = []
        pop_num = len(arr) - i
        for item in arr:
            while stack and pop_num and stack[-1] < item:
                pop_num -= 1
                stack.pop()
            stack.append(item)
        return stack[:i]

    def merge(self, arr1, arr2, k):
        return [max(arr1, arr2).pop(0) for _ in range(k)]

    def maxNumber(self, nums1, nums2, k):
        res = [0] * k
        for i in range(k+1):
            if i <= len(nums1) and k-i <= len(nums2):
                tmp1 = self.get_max_num_subseq(nums1, i)
                tmp2 = self.get_max_num_subseq(nums2, k-i)
                temp = self.merge(tmp1, tmp2, k)

                res = max(res, temp)
        return res



if __name__ == '__main__':
    obj = Solution()
    nums1 = [3, 9]
    nums2 = [8, 9]
    k = 3
    res = obj.maxNumber(nums1, nums2, k)
    print(res)