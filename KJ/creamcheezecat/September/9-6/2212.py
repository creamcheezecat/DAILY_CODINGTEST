""" 
https://www.acmicpc.net/problem/2212
사회망 서비스
2212
"""

import sys
input = sys.stdin.readline
import sys

n = int(input())
k = int(input())
pos = sorted(list(map(int, input().split())))

if k >= n:
    print(0)
    sys.exit()

dist = []
for i in range(1, n):
    dist.append(pos[i] - pos[i-1])

dist.sort(reverse=True)
for _ in range(k-1):
    dist.pop(0)

print(sum(dist))