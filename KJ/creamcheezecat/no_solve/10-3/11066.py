""" 
https://www.acmicpc.net/problem/11066
파일 합치기
11066
"""

import sys
input = sys.stdin.readline

MAX = sys.maxsize

T = int(input())

for _ in range(T):
    N = int(input())
    file = list(map(int,input().split()))
    dp = [[0] * N for _ in range(N)]
    sum = [0]
    for f in file:
        sum.append(sum[-1]+f)
        
    for d in range(1,N):
        for i in range(N-d):
            j = d + i
            dp[i][j] = MAX
            
            for k in range(i,j):
                dp[i][j] = min(dp[i][j],dp[i][k] + dp[k+1][j] + sum[j+1]-sum[i])
    
    print(dp[0][N-1])