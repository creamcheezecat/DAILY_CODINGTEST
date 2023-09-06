""" 
https://www.acmicpc.net/problem/2533
사회망 서비스
2533
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


n = int(input())
c = [[] for i in range(n+1)]
dp = [[0,0] for i in range(n+1)]


for _ in range(n-1):
    a,b = map(int , input().split(" "))
    c[a].append(b)
    c[b].append(a)
    
visited = [0 for i in range(n+1)]
def dfs(start):
    global c
    global visited
    visited[start] = 1
    if len(c[start]) == 0:
        dp[start][1] = 1
        dp[start][0] = 0
    else:
        for i in c[start]:
            if visited[i] == 0:
                dfs(i)
                dp[start][1] += min(dp[i][0] , dp[i][1])
                dp[start][0] += dp[i][1]
        dp[start][1] += 1

dfs(1)
print(min(dp[1][0],dp[1][1]))