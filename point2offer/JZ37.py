'''
@File  : word-search.py
@Author: Swift
@Date  : 2021/3/8 22:57
@Link  : https://leetcode-cn.com/problems/word-search/
@Desc  : 79. 单词搜索
@Method: https://leetcode-cn.com/problems/word-search/solution/dan-ci-sou-suo-by-leetcode-solution/
'''

input_data = input().strip().split()
N, L = int(input_data[0]), int(input_data[1])
dp = [0] * (N + 1)
for idx in range(1, N + 1):
    dp[idx] = dp[idx - 1] + idx

res = (1, N+1)
i = 1
j = 1
while i <= N:
    if dp[i]-dp[j-1] >= N:
        while j <= i:
            if dp[i]-dp[j-1] == N and i-j+1 >= L:
                if res[1]-res[0] > i-j:
                    res = (j, i)
                    break
            j += 1
    i += 1

if res[1] == N+1:
    print("No")
else:
    for i in range(res[0], res[1]+1):
        print(i, end=" ")