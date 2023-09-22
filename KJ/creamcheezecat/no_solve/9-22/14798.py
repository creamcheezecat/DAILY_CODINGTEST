""" 
https://www.acmicpc.net/problem/14798
알파벳 케이크
14798
"""

# 모르겠음

import sys
input = sys.stdin.readline

def solve_cake(R, C, cake):
    def valid(r, c):
        return 0 <= r < R and 0 <= c < C

    # 빈 칸을 채울 문자를 초기화합니다.
    current_char = 'A'

    for r in range(R):
        for c in range(C):
            # 빈 칸인 경우에만 처리합니다.
            if cake[r][c] == '?':
                # 왼쪽, 오른쪽, 위, 아래를 확인하여 현재 문자로 채울 수 있는지 확인합니다.
                neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
                can_fill = all(valid(nr, nc) and cake[nr][nc] != current_char for nr, nc in neighbors)

                # 현재 문자로 채울 수 있다면 채우고 다음 문자로 넘어갑니다.
                if can_fill:
                    cake[r][c] = current_char
                    current_char = chr(ord(current_char) + 1)

    return cake

# 테스트 케이스 수 입력
T = int(input())

for case in range(1, T + 1):
    R, C = map(int, input().split())
    cake = [list(input().strip()) for _ in range(R)]

    # 문제 해결 함수 호출
    result = solve_cake(R, C, cake)

    # 결과 출력
    print(f"Case #{case}:")
    for row in result:
        print("".join(row))