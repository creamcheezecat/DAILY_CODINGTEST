""" 
https://www.acmicpc.net/problem/10282
해킹
10282
"""

import sys ,heapq
input = sys.stdin.readline

def hacking(n, start):
    dist = [sys.maxsize] * (n+1)
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        time, computer = heapq.heappop(q)
        for ntime, ncom in arr[computer]:
            total = time + ntime
            if dist[ncom] > total:
                dist[ncom] = total
                heapq.heappush(q, (total, ncom))
    result_time = 0
    result_com = 0
    for x in dist:
        if x != sys.maxsize:
            result_com += 1
            result_time = max(result_time, x)
    return [result_com, result_time]


T = int(input())
for _ in range(T):
    n, d, c = map(int, input().split())
    arr = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        arr[b].append((s, a))
    print(*hacking(n, c))