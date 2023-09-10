""" 
https://www.acmicpc.net/problem/10217
KCM Travel
10217
"""

import sys
input = sys.stdin.readline
from collections import deque
import heapq

    
# 인천은 언제나 1번 도시 LA 는 언제나 N 번 도시
# LA 에 도착하는 가장 짧은 소요 시간 (비용 안에)
# 도착 못하면 Poor KCM 출력

def dijkstra():
    distance = [[float("inf")] * (M + 1) for _ in range(N + 1)]
    distance[1][0] = 0
    
    que = deque([(0, 0, 1)])
    #heap = [(0, 0, 1)]  # 거리 / 비용 / 시작 도시

    while que:
        dist, totalcost, node = que.popleft()

        if distance[node][totalcost] < dist:
            continue

        for _dist,_cost, next_node in graph[node]:
            after_cost = _cost + totalcost
            after_dist = _dist + dist
            
            if after_cost <= M and after_dist < distance[next_node][after_cost]:
                for i in range(after_cost, M + 1):
                    if after_dist < distance[next_node][i]:
                        distance[next_node][i] = after_dist
                    else:
                        break
                que.append([(after_dist,after_cost,next_node)])
                
    result = distance[N][M]
    if result == float('inf'):
        print("Poor KCM")
    else:
        print(result)
    
            
        """ for next_node, cost, weight in graph[node]:
            next_dist = dist + weight

            if totalcost + cost <= M and next_dist < distance[next_node][totalcost + cost]:
                distance[next_node][totalcost + cost] = next_dist
                heapq.heappush(heap, (next_dist, totalcost + cost, next_node))

    return min(distance[N]) """

T = int(input())


for _ in range(T):
    N, M, K = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(K):
        u, v, c, d = map(int, input().split())  # 출발 / 도착 / 비용 / 시간
        graph[u].append((v, c, d))

    dijkstra()
    

# 틀린 코드

""" T = int(input())

N,M,K = map(int,input().split()) # N : 공항의 수 M : 지원 비용 K : 티켓의 수
graph = [[] for _ in range(N + 1)]
for _ in range(K):
    u,v,c,d = map(int,input().split()) # /u 출발 /v 도착 /c 비용 /d 시간
    graph[u].append((v, c, d)) """

""" def dijkstra():
    distance = [float("inf")] * (N + 1)
    distance[1] = 0
    heap = [(0,0, 1)] # 비용 / 거리 / 시작 도시

    while heap:
        totalcost, dist, node = heapq.heappop(heap)

        if totalcost > M:
            continue

        for next_node, cost ,weight in graph[node]:
            next_dist = dist + weight
            if next_dist < distance[next_node]:
                distance[next_node] = next_dist
                totalcost += cost
                heapq.heappush(heap, (totalcost ,next_dist, next_node))

    return distance

result = dijkstra()
if result[N] == 0 or result[N] == float('inf'):
    print("Poor KCM")
else:
    print(result[N]) """