""" 
https://www.acmicpc.net/problem/2339
석판자르기
2339
"""
# 문제 해결 실패

import sys
input = sys.stdin.readline

def is_valid(board, x1, y1, x2, y2):
    # 보석 결정체 개수 확인
    gem_count = 0
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if board[i][j] == 2:
                gem_count += 1
                if gem_count > 1:
                    return False
            if board[i][j] == 1:
                return False
    return gem_count == 1

def count_ways(board, x1, y1, x2, y2):
    # 해당 구간에서 자를 수 있는 모든 경우를 탐색
    ways = 0

    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if board[i][j] == 1:
                # 가로로 자를 때
                valid_vertical = True
                for k in range(x1, x2 + 1):
                    if k == i:
                        continue
                    if board[k][j] == 2:
                        valid_vertical = False
                        break
                if valid_vertical:
                    ways += 1

                # 세로로 자를 때
                valid_horizontal = True
                for k in range(y1, y2 + 1):
                    if k == j:
                        continue
                    if board[i][k] == 2:
                        valid_horizontal = False
                        break
                if valid_horizontal:
                    ways += 1

    return ways

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

result = count_ways(board, 0, 0, N - 1, N - 1)

if result == 0:
    print(-1)
else:
    print(result)