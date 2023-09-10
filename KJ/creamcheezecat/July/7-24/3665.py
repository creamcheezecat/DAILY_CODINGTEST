""" 
https://www.acmicpc.net/problem/3665
최종 순위
3665
"""

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input()) # 팀 수
    teams = list(map(int,input().split()))
    M = int(input()) # 작년과 순위가 바뀐 쌍
    changes = []
    indegree = [0] * (N+1)  # 진입차수를 기록할 리스트
    for _ in range(M):
        changes.append(list(map(int,input().split())))
        
# 전혀 모르겠다.
        
    