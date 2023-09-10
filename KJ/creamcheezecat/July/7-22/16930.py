""" 
https://www.acmicpc.net/problem/16930
달리기
16930
"""

import sys
input = sys.stdin.readline
from collections import deque

# NxM 체육간  . 빈칸 # 는 벽
# 매초 마다 한 방향을 1 ~ K 칸 이동
# 최소 시간

# BFS
def bfs(x1, y1, x2, y2):
  queue = deque()
  # 시작점 삽입, 방문 처리
  queue.append((x1, y1))
  graph[x1][y1] = 0

  while queue:
    x, y = queue.popleft()
    # 끝점에 도착했으면 종료
    if(x == x2 and y == y2):
      return graph[x2][y2]
    # 상하좌우 탐색
    for i in range(4):
      for j in range(1, k + 1):
        nx = x + dx[i] * j
        ny = y + dy[i] * j
        # 범위 내이고
        if(0 <= nx < n and 0 <= ny < m):
          # 방문하지 않은 빈칸이면
          if(graph[nx][ny] == '.'):
            # 삽입, 방문 처리
            queue.append((nx, ny))
            graph[nx][ny] = graph[x][y] + 1
          elif(graph[nx][ny] == '#'):
            break
        else: break
  return -1

n, m, k = map(int, input().split())  # 세로, 가로, 1초에 이동가능한 최대 칸
# n * m (.: 빈칸 #: 벽)
graph = [list(input()) for _ in range(n)]
x1, y1, x2, y2 = map(int, input().split())  # 시작점, 끝점
visited = [[0] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(x1-1, y1-1, x2-1, y2-1))


""" N,M,K = map(int , input().split())

board = []
#visited = [[False for _ in range(N)] for _ in range(M)]
for _ in range(N):
    board.append(input().rstrip())
    
startx, starty, endx, endy = map(int , input().split())

def bfs():
    q = deque()
    q.append((startx - 1, starty - 1, 0))  # x, y, 이동횟수
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[starty - 1][startx - 1] = True
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        x, y, cnt = q.popleft()
        
        if x == endx - 1 and y == endy - 1:
            return cnt
        
        for i in range(4):
            for k in range(1, K + 1):
                nx = x + dx[i] * k
                ny = y + dy[i] * k

                if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx]:
                    if board[ny][nx] == '#':
                        break  # 벽을 만나면 해당 방향으로의 추가적인 이동을 중단합니다.
                    elif visited[ny][nx] == False:
                        visited[ny][nx] = True
                        q.append((nx, ny, cnt + 1))
                    
                    
                else:
                    break  # 범위를 벗어나거나 이미 방문한 위치라면 해당 방향으로의 추가적인 이동을 중단합니다.
    
    return -1

print(bfs()) """