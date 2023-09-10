""" 
https://www.acmicpc.net/problem/1753
최단경로
1753
"""

import sys
input = sys.stdin.readline
import heapq

V, E = map(int,input().split()) # V 는 정점의 갯수 E 간선의 갯수
K = int(input())                # 시작 정점 번호

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start):
    distance = [float("inf")] * (V + 1)
    distance[start] = 0
    heap = [(0, start)]

    while heap:
        dist, node = heapq.heappop(heap)

        if distance[node] < dist:
            continue

        for next_node, weight in graph[node]:
            next_dist = dist + weight
            if next_dist < distance[next_node]:
                distance[next_node] = next_dist
                heapq.heappush(heap, (next_dist, next_node))

    return distance

result = dijkstra(K)

for i in range(1, V + 1):
    if result[i] == float("inf"):
        print("INF")
    else:
        print(result[i])



""" V, E = map(int,input().split()) # V 는 정점의 갯수 E 간선의 갯수
K = int(input())                # 시작 정점 번호
graph = [[float("inf") for _ in range(V+1)] for _ in range(V+1)]
for i in range(E):
    u,v,w = map(int,input().split()) # u 에서 v로 가는 가중치 w
    graph[u][v] = w



# 최단 경로를 구하는 시작점 자신은 0 으로 출력 
#                         경로가 존재않하면 INF

# 다익스트라 알고리즘 함수
def dijkstra(start):
    distance = [float("inf")] * (V + 1)
    distance[start] = 0
    visited = [False] * (V + 1)

    for _ in range(V):
        # 아직 방문하지 않은 정점 중 최단 거리가 가장 작은 정점 선택
        min_distance = float("inf")
        min_node = -1
        for i in range(1, V + 1):
            if not visited[i] and distance[i] < min_distance:
                min_distance = distance[i]
                min_node = i

        visited[min_node] = True

        # 선택한 정점을 기준으로 인접한 정점들의 최단 거리 갱신
        for i in range(1, V + 1):
            if graph[min_node][i] != float("inf"):
                distance[i] = min(distance[i], distance[min_node] + graph[min_node][i])

    return distance

result = dijkstra(K)

for i in range(1, V + 1):
    if result[i] == float("inf"):
        print("INF")
    else:
        print(result[i]) """