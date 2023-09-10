""" 
https://www.acmicpc.net/problem/5719
거의 최단 경로
5719
"""

import sys
input = sys.stdin.readline

while(True):
    N,M = map(int,input().split()) # N : 도시 수 M : 도로 수
    
    if(N == 0 and M == 0):
        break
    
    S,D = map(int,input().split()) # S : 시작 점 D : 도착 점
    
    graph = [[float("inf") for _ in range(N+1)] for _ in range(N+1)]
    for _ in range(M):
        U,V,P = map(int,input().split()) # U 에서 V 까지 가는 도로의 길이
        graph[U][V] = P
        
# 잘 모르겠다 .... 두번쨰 ?