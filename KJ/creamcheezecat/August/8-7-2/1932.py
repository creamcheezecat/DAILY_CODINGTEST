""" 
https://www.acmicpc.net/problem/2293
동전 1
2293
"""

import sys
input = sys.stdin.readline

N , K= map(int,input().split())

coins = []
for _ in range(N):
    coins.append(int(input()))
    
dp = [0 for _ in range(K+1)]

dp[0] = 1

for i in range(N):
    for j in range(coins[i],K+1):
        dp[j] = dp[j] + dp[j-coins[i]]
        

print(dp[K])