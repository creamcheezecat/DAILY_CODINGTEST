""" 
https://www.acmicpc.net/problem/16930
달리기
16930
"""

import sys
input = sys.stdin.readline

from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M, K = map(int, input().split())  # N:세로 M:가로, K: step
D = [list(input()) for _ in range(N)]
sx, sy, ex, ey = map(int, input().split())
# 인덱스와 위치값을 맞춰주기 위해 모두 1씩 빼준다
sx -= 1
sy -= 1
ex -= 1
ey -= 1
check = [[float("inf")] * M for _ in range(N)]
q = deque()
q.append((sx, sy))
check[sx][sy] = 0

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        nk = 1
        while (
            nk <= K
            and 0 <= nx < N
            and 0 <= ny < M
            and D[nx][ny] != "#"
            and check[nx][ny] > check[x][y]
        ):
            if check[nx][ny] == float("inf"):
                q.append((nx, ny))
                check[nx][ny] = check[x][y] + 1
            nx += dx[i]
            ny += dy[i]
            nk += 1
if check[ex][ey] == float("inf"):
    print(-1)
else:
    print(check[ex][ey])