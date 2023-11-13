""" 
https://www.acmicpc.net/problem/1135
뉴스 전하기
1135
"""

import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

N = int(input())

S = list(map(int,input().split()))

graph = [[] for _ in range(N)]
visited = [False] *(N)
dp = [0] *(N)

for i in range(N):
    if i==0:
        continue
    graph[i].append(S[i])
    graph[S[i]].append(i)


def dfs(x):
    visited[x]=True
    elem = [] # DP값을 담을 리스트
    for i in graph[x]:
        if not visited[i]:
            dfs(i)
            elem.append(dp[i])
    if not elem: # 리프노드면 끝냄
        return
    elem.sort(reverse=True)
    max_num = 0
    for i in range(len(elem)):
        check = elem[i] + (i+1)
        if check>max_num:
            max_num=check

    dp[x] = max_num

dfs(0)
print(max(dp))