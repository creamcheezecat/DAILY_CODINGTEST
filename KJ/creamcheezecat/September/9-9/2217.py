""" 
https://www.acmicpc.net/problem/2217
로프
2217
"""

import sys
input = sys.stdin.readline

N = int(input())
M = []
for i in range(N):
    M.append(int(input()))
    
M.sort(reverse=True)
result = []

for j in range(N):
    result.append(M[j] * (j + 1))

print(max(result))