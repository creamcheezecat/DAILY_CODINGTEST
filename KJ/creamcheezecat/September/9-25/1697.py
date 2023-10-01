""" 
https://www.acmicpc.net/problem/1697
숨바꼭질
1697
"""

import sys
input = sys.stdin.readline
from collections import deque

MAX = 10 ** 5

def dfs(dist, n , k):
    q = deque()
    q.append(n)
    
    while q:
        x = q.popleft()
        
        if x == k:
            print(dist[x])
            break
        
        for nx in (x - 1 , x + 1, x * 2):
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[x] + 1
                q.append(nx)
                
dist = [0] * (MAX + 1)
n,k = map(int, input().split())

dfs(dist,n,k)
