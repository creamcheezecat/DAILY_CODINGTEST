""" 
https://www.acmicpc.net/problem/11964
Fruit Feast
11964
"""

import sys
from collections import deque
input = sys.stdin.readline

t, a, b = map(int, sys.stdin.readline().split())
result = a
check = [False] * 5000001
v = []

tmp = (a, False)
check[a] = True
q = deque([tmp])
v.append(a)

if not check[b]:
    tmp = (b, False)
    check[b] = True
    q.append(tmp)
    result = max(result, b)
    v.append(b)

while q:
    cv, ch = q[0]
    q.popleft()

    for i in range(len(v)):
        nv = v[i] + cv
        if nv <= t and not check[nv]:
            result = max(result, nv)
            check[nv] = True
            q.append((nv, ch))

        if not ch:
            nv = cv // 2 + v[i]
            if nv <= t and not check[nv]:
                result = max(result, nv)
                check[nv] = True
                q.append((nv, True))

print(result)