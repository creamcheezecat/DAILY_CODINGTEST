""" 
https://www.acmicpc.net/problem/15681
트리와 쿼리
15681
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, r, q = map(int, input().split())
tree = [[] for _ in range(n+1)]
count = [0]*(n+1)

for i in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    
def countPoint(x):
    count[x]=1
    for i in tree[x]:
        if not count[i]:
            countPoint(i)
            count[x] += count[i]
            
countPoint(r)

for i in range(q):
    u = int(input())
    print(count[u])