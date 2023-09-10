""" 
https://www.acmicpc.net/problem/2643
색종이 올려 놓기
2643
"""

import sys
input = sys.stdin.readline

# 새로 올려놓은 색종이는 맨 위의 색종이보다 크지 않아야한다
# 새로 올려 놓은 색종이와 맨 위의 색종이의 변들은 서로 평행 해야한다
# 색종이는 90도 돌릴 수 있다.
# => 두변중 큰변의 길이를 기주능로 역으로 정렬하면 나머지 한변만 비교하면 된다.

N = int(input())

paper = []
for _ in range(N):
    width = list(map(int, sys.stdin.readline().split()))
    paper.append(sorted(width))
    
paper.sort()

dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if paper[i][1] >= paper[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))