""" 
https://www.acmicpc.net/problem/12886
돌 그룹
12886
"""

import sys
from collections import deque
input = sys.stdin.readline

a,b,c = map(int, input().split())
visited = [[False]*1501 for _ in range(1501)]
tot = a+b+c
def dfs():
    global a,b,c
    q = deque()
    q.append([a,b])
    visited[a][b] = True
    while q:
        a,b = q.popleft()
        c = tot-a-b
        if a==b==c: 
            return 1
        for na, nb in ((a,b),(a,c),(b,c)):
            if na < nb:
                nb -= na
                na += na
            elif na > nb:
                na -= nb
                nb += nb
            else: continue
            nc = tot-na-nb
            a = min(min(na,nb), nc)
            b = max(max(na, nb), nc)
            if not visited[a][b]:
                q.append((a,b))
                visited[a][b] = True
    return 0
if tot%3 != 0: print(0)
else:
    print(dfs())