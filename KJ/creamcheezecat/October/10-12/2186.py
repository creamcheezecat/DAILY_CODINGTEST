""" 
https://www.acmicpc.net/problem/2186
문자판
2186
"""

import sys
input = sys.stdin.readline

n, m, k = map(int,input().split())

map = [list(input().rstrip()) for _ in range(n)] #문자판 
word = input().rstrip() #만들어야 하는 단어

visited = [[[-1] * len(word) for _ in range(m)] for _ in range(n)] #방문 여부 판단 배열
#visited[y][x][idx] : 문자판(x,y)의 문자가 word의 idx번째 단어일때 존재하는 경로의 수를 나타냄 / -1로 초기화 되어있음

def dfs(y, x, idx):
    
    #전에 방문했던 곳이라면 / visited[y][x][idx] return = 이미 저장된 값을 return
    if visited[y][x][idx] != -1:
        return visited[y][x][idx]
    
    #문자판(x,y)의 문자가 word의 idx번째 문자와 다르면 = 필요한 문자가 아니라면 / 0 return
    if map[y][x] != word[idx]:
        return 0
    
    #word가 완성됬다면 / 1 return
    if idx == len(word)-1:
        return 1

    cnt = 0 #경로의 개수를 저장
    for i in range(-k, k+1): # (x,y)에서 갈 수 있는 경우의 수를 모두 탐색
        #i가 0이면 의미가 없기에 continue
        if not i: 
            continue
        
        #(x,y)에서 위아래로 갈 수 있는 모든 경우를 탐색
        if 0 <= y+i < n:
            cnt += dfs(y+i, x, idx+1)

        #(x,y)에서 좌우로 갈 수 있는 모든 경우를 탐색
        if 0 <= x+i < m:
            cnt += dfs(y, x+i, idx+1)
    visited[y][x][idx] = cnt #경로의 개수만큼 갱신

    return cnt #경로의 개수 return
    
    
res = 0 #최종 경로의 개수
for i in range(n):
    for j in range(m):
        #word의 시작단어부터 dfs를 시작
        if map[i][j] == word[0]:
            res += dfs(i,j,0)

print(res)