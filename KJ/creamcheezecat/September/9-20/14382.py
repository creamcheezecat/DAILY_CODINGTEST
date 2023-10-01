""" 
https://www.acmicpc.net/problem/14382
숫자세는 양
14382
"""

import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    n = int(input())
    if n == 0:
        print("Case #"+str(i+1)+": INSOMNIA")
        continue
    j = 1
    s = []
    while True:
        for k in set(str(n*j)):
            if int(k) not in s:
                s.append(int(k))
        if 0 in s and 1 in s and 2 in s and 3 in s and 4 in s and 5 in s and 6 in s and 7 in s and 8 in s and 9 in s:
            print("Case #"+str(i+1)+": "+str(n*j))
            break
        j += 1