""" 
https://www.acmicpc.net/problem/14466
소가 길을 건너간 이유6
14466
"""

import sys
from collections import defaultdict , deque
input = sys.stdin.readline

di, dj = [1, -1, 0, 0], [0, 0, 1, -1]  

def bfs(sti, stj, idx):  
    global result  
    visited = [[0] * N for _ in range(N)]  
    q = deque()  
    q.append((sti, stj))  
    no_road = [[0] * (N) for _ in range(N)]  
    visited[sti][stj] = 1  
    while q:  
        si, sj = q.popleft()  
        for i in range(4):  
            ni, nj = si + di[i], sj + dj[i]  
            if 0<= ni <N and 0<= nj < N and visited[ni][nj] == 0 and not (ni, nj) in road[(si, sj)] :  
                if arr[ni][nj] == 1:  
                    no_road[ni][nj] = 1  

                q.append((ni, nj))  
                visited[ni][nj] = 1  

    for ci, cj in cow[idx+1:]:  
        if not no_road[ci][cj]:  
            result += 1  

N, K, R =map(int, input().split())  

arr = [[0] * N for _ in range(N)]  
road = defaultdict(list)  
cow = []  
result = 0  
for _ in range(R):  
    a, b, c, d = map(int, input().split())  
    road[(a-1, b-1)].append((c-1, d-1))  
    road[(c-1, d-1)].append((a-1, b-1))  
for _ in range(K):  
    a, b = map(int, input().split())  
    arr[a-1][b-1] = 1  
    cow.append((a-1,b-1))  

for i, j in enumerate(cow):  
    bfs(j[0], j[1], i)  

print(result)