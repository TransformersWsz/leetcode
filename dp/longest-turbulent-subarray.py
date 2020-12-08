'''
@File  : longest-turbulent-subarray.py
@Author: Swift
@Date  : 2020/12/8 10:42
@Link  : https://leetcode-cn.com/problems/longest-turbulent-subarray/
@Desc  : 最长湍流子数组
@Method: https://leetcode-cn.com/problems/longest-turbulent-subarray/solution/zui-chang-tuan-liu-zi-shu-zu-by-leetcode/
'''


class Solution:
    def maxTurbulenceSize(self, arr):
        res = 1 if len(arr) > 0 else 0
        start_idx = 0
        for i in range(1, len(arr)):
            if i==len(arr)-1 or (arr[i]-arr[i-1])*(arr[i+1]-arr[i]) >= 0:
                if arr[i]-arr[i-1] != 0:
                    res = max(res, i-start_idx+1)
                start_idx = i
        return res


if __name__ == '__main__':
    obj = Solution()
    arr = []
    num = obj.maxTurbulenceSize(arr)
    print(num)


