'''
@File  : test.py
@Author: Swift
@Date  : 2020/12/15 11:55
@Link  : 
@Desc  : 
@Method: 
'''


while True:
    N = int(input())
    arr = list(map(int, input().strip().split()))
    dp = arr[:]
    res = dp[0]
    for i in range(1, N):
        for j in range(i-1, -1, -1):
            if arr[i] > arr[j]:
                dp[i] = max(dp[j]+arr[i], dp[i])
                res = max(res, dp[i])
    print(res)

