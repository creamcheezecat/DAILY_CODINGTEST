""" 
https://www.acmicpc.net/problem/3665
최종순위
3665
"""

import sys
input = sys.stdin.readline
from collections import deque

# 위상 정렬
def topologicalSort(n, graph, inDegree, isLinked):
    q = deque()
    res = []
    
    for team in range(1, n+1):
        if inDegree[team] == 0:
            q.append(team)
    
    while q:
        team = q.popleft()
        res.append(team)
        
        for adj_team in graph[team]:
            # 해당 간선이 실제로 연결되어 있는
            # 유효한 간선인지를 isLinked로 판단하여
            # 만약 0이라면 해당 간선은 무시
            if isLinked[team][adj_team] == 0:
                continue
            
            inDegree[adj_team] -= 1
            
            if inDegree[adj_team] == 0:
                q.append(adj_team)
    
    return res
        

T = int(input())

for _ in range(T):
    n = int(input())
    rank_prev = [*map(int, input().split())]
    
    # 단방향 연결 그래프
    graph = [[] for _ in range(n+1)]
    
    # isLinked[a][b]는 a -> b 간선이 실제로
    # 연결이 되어있는 실재하는 간선인지에 대한
    # boolean 값을 의미
    isLinked = [[0]*(n+1) for _ in range(n+1)]
    
    # 진입 차수
    inDegree = [0]*(n+1)
    
    # 작년 순위에 대해, 가능한 모든 단방향 간선을
    # graph애 넣어주고, isLinked와 inDegree 갱신
    for idx1 in range(n-1):
        for idx2 in range(idx1+1, n):
            team1 = rank_prev[idx1]
            team2 = rank_prev[idx2]
            
            graph[team1].append(team2)
            isLinked[team1][team2] = 1
            inDegree[team2] += 1
    
    m = int(input())
    
    for _ in range(m):
        team_a, team_b = map(int, input().split())
        
        # 어떤 두 노드는 반드시 단방향 간선을 가지고 있음
        # 따라서 조건문을 a -> b인 경우, b -> a 인 경우 총
        # 두 갈래로 분기
        if isLinked[team_a][team_b]:
            # 만약 a와 b가 a -> b 간선으로 연결된 경우,
            # 상대적 순위 변동을 반영하기 위해
            # 반대 방향으로 간선을 넣어주고,
            # 원래의 방향의 isLinked는 false로 바꿔주고
            # inDegree는 1 감소시켜주고, 바꾼 방향에
            # 대한 isLinked는 1로, inDegree는 1 더해준다.
            # 이렇게 되면 원래 a -> b 방향의 간선은
            # isLinked와 inDegree에서 없애주는 작업을 처리
            # 해줬지만 graph 리스트에는 정보가 남아있게
            # 되는데, 이는 위상 정렬 함수 내부에서 
            # isLinked의 값으로 유효 간선 여부를 판단하여
            # 걸러낼 수 있음.
            graph[team_b].append(team_a)
            isLinked[team_a][team_b] = 0
            isLinked[team_b][team_a] = 1
            inDegree[team_b] -= 1
            inDegree[team_a] += 1
        elif isLinked[team_b][team_a]:
            graph[team_a].append(team_b)
            isLinked[team_b][team_a] = 0
            isLinked[team_a][team_b] = 1
            inDegree[team_a] -= 1
            inDegree[team_b] += 1
    
    res = topologicalSort(n, graph, inDegree, isLinked)
    
    # 사이클이 존재하는 경우 순위를 확정지을 수 없으므로
    # IMPOSSIBLE 출력. 다만 유의할 점이 있는데,
    # 작년 순위가 1, 2, 3, 4로 주어졌다고 치고,
    # 상대적 변동이 2 3, 3 4로 주어졌다고 치면,
    # 1팀의 진입차수가 0이지만 그래프에는 2-3-4 사이클이
    # 존재하는 상태이다. 따라서 위상 정렬 내부에서는 1을
    # 현재 순위 리스트에 넣은 다음, 2 3 4 중에서 진입 차수
    # 가 0인 것이 없으므로 그대로 종료한다.
    # 즉 이 경우에는 사이클이 있더라도 res의 길이가 1이 되는
    # 케이스이므로, 이런 경우까지 고려하여 IMPOSSIBLE을 출력하는
    # 조건으로 len(res) < n을 작성해준 것이다.
    # 참고로, 문제에서 설명하는 "?"의 경우는 존재하지 않는다.
    # 이미 작년의 순위를 제공한 순간, 모든 노드 사이의 단방향
    # 간선이 존재하기 때문이다.
    if len(res) < n:
        print("IMPOSSIBLE")
    else:
        print(*res, sep=" ")