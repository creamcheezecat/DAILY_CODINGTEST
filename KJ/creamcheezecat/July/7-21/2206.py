""" 
https://www.acmicpc.net/problem/2206
벽 부수고 이동하기
2206
"""

import sys
input = sys.stdin.readline
from collections import deque

# 0,0 에서 N-1 M-1 까지 가야한다
# 벽하나를 뿌실수 있다.
# 최단경로를 구하라

N,M = map(int,input().split()) # N 가로 M 세로

board = []
for _ in range(N):
    row = list(map(int, input().rstrip()))
    board.append(row)

def bfs():
    q = deque()
    q.append([0, 0, 0])  # x, y, 벽을 부순 횟수
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        n, m, wall = q.popleft()

        if n == N - 1 and m == M - 1:
            return visited[n][m][wall]

        for i in range(4):
            nx = dx[i] + n
            my = dy[i] + m

            if 0 <= nx < N and 0 <= my < M:
                if board[nx][my] == 0 and not visited[nx][my][wall]:
                    visited[nx][my][wall] = visited[n][m][wall] + 1
                    q.append([nx, my, wall])
                elif board[nx][my] == 1 and wall == 0:
                    visited[nx][my][wall + 1] = visited[n][m][wall] + 1
                    q.append([nx, my, wall + 1])

    return -1

result = bfs()
print(result)



""" def bfs():
    q = deque()
    q.append([0,0,0,1]) # x,y,벽 카운트, 이동횟수
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    sol = []
    while q:
        n,m,wall,cnt = q.popleft()
        
        if n == N-1 and m == M-1:
            sol.append(cnt)
        dx = [1,-1,0,0]
        dy = [0, 0,1,-1]
        
        for i in range(4):
            nx = dx[i] + n
            my = dy[i] + m
            
            if(0 <= nx < N and 0 <= my < M):
                if(board[nx][my] == 0 and not visited[nx][my]):
                    visited[nx][my] = 1
                    q.append([nx,my,wall,cnt +1])
                elif board[nx][my] == 1 and wall == 0:
                    visited[nx][my] = 1
                    q.append([nx,my,wall +1,cnt +1])
            
            
    return sol

reuslt = bfs()
if not reuslt :
    print(-1)
else:
    print(min(reuslt)) """