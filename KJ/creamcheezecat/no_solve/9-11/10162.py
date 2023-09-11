""" 
https://www.acmicpc.net/problem/10162
전자레인지
10162
"""

import sys
input = sys.stdin.readline

T = int(input())

if T % 10 != 0:
    print(-1)
else:
    A = B = C = 0
    A = T // 300
    B = (T % 300) // 60
    C = (T % 300) % 60 // 10
    print(A, B, C)