""" 
https://www.acmicpc.net/problem/14226
이모티콘
14226
"""

import sys
input = sys.stdin.readline
from collections import deque

# 화면에 이미 이모티콘 1개

# 클립보드에 있는 이모티콘 화면에 붙여넣기 (화면에 있는거 + 클립보드 있는거)
# 화면에 있는 이모티콘 하나 삭제
# 위 두가지 연산이 1초

# 화면에 S개 가 있을떄까지 걸리는 시간의 최솟값 출력


S = int(input())

def bfs():
    q = deque()
    q.append([1, 0, 0])  # 화면에 이모티콘이 1개, 클립보드에는 0개, 시간은 0초로 시작
    visited = set()  # 방문한 (화면에 있는 이모티콘 개수, 클립보드에 있는 이모티콘 개수)를 저장하는 집합

    while q:
        scr, clip, time = q.popleft()

        if scr == S:
            return time

        # 붙여넣기 연산
        if (scr, scr) not in visited:
            visited.add((scr, scr))
            q.append([scr, scr, time + 1])

        # 삭제 연산
        if scr > 0 and (scr - 1, clip) not in visited:
            visited.add((scr - 1, clip))
            q.append([scr - 1, clip, time + 1])

        # 복사 연산
        if clip > 0 and (scr + clip, clip) not in visited:
            visited.add((scr + clip, clip))
            q.append([scr + clip, clip, time + 1])

print(bfs())
    