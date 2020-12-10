'''
@File  : max-dot-product-of-two-subsequences.py
@Author: Swift
@Date  : 2020/12/9 23:08
@Link  : https://leetcode-cn.com/problems/max-dot-product-of-two-subsequences/
@Desc  : 两个子序列的最大点积
@Method: 
'''

def init_dp(len1, len2):
    dp = [ [0]*(len2+1) for _ in range(len1+1) ]
    return dp

def corner_case(nums1, nums2):
    res = 0
    if max(nums1) < 0 and min(nums2) > 0:
        res = max(nums1) * min(nums2)
    elif min(nums1) > 0 and max(nums2) < 0:
        res = min(nums1) * max(nums2)
    return res

def maxDotProduct(nums1, nums2):
    res = corner_case(nums1, nums2)
    if res < 0:
        return res
    else:
        len1 = len(nums1)
        len2 = len(nums2)
        dp = init_dp(len1, len2)
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                if nums1[i-1]*nums2[j-1] > 0:
                    dp[i][j] = max(dp[i-1][j-1] + nums1[i-1]*nums2[j-1], dp[i][j-1], dp[i-1][j])
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[len1][len2]


if __name__ == '__main__':
    nums1 = [5, -4, -3]
    nums2 = [-4, -3, 0, -4, 2]
    res = maxDotProduct(nums1, nums2)
    print(res)