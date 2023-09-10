""" 
https://www.acmicpc.net/problem/1516
게임 개발
1516
"""

import sys
input = sys.stdin.readline
from collections import deque

# 건물을 짓는데 최소 시간
N = int(input())
building_info = [[0] for _ in range(N+1)]  # 건물 정보를 담을 리스트
indegree = [0] * (N+1)  # 진입차수를 기록할 리스트

# 건물 정보 입력 받기
for n in range(1, N+1):
    building = list(map(int, input().split()))
    building_info[n] = building[1:-1]  # 선행 건물들의 번호만 저장
    for pre_building in building_info[n]:
        indegree[n] += 1

def topological_sort(building, indegree):
    queue = deque()
    result = [0] * (N+1)

    # 초기 진입차수가 0인 노드들을 큐에 삽입
    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)
            result[i] = building[i][0]

    while queue:
        cur_node = queue.popleft()

        # 현재 노드와 연결된 노드들의 진입차수를 감소시키고, 최소 건설 시간을 업데이트
        for next_node in building[cur_node][1:]:
            indegree[next_node] -= 1
            result[next_node] = max(result[next_node], result[cur_node] + building[next_node][0])

            # 진입차수가 0인 노드들을 큐에 삽입
            if indegree[next_node] == 0:
                queue.append(next_node)

    return result

# 위상 정렬 수행
result = topological_sort(building_info, indegree)

# 결과 출력
for n in range(1, N+1):
    print(result[n])

""" building = []
builded = [0 for _ in range(501)]
for n in range(1,N+1):
    building = list(map(int,input().split()))
    if(len(builded)==2) :
        builded[n] = building[0]
    else:
        for i in range(len(building)):
            if i == 0 :
                totimer = building[i]
            elif i == len(building)-1:
                builded[n] = totimer
            else:
                totimer += builded[building[i]]
                
    print(builded[n])
 """