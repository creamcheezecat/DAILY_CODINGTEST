""" 
https://www.acmicpc.net/problem/14810
14810
"""

# 반례를 찾지못함

import sys
import math
input = sys.stdin.readline

# 함수를 정의하여 각 테스트 케이스를 처리
def max_exposed_surface_area(N, K, pancakes):
    # 팬케이크를 높이와 반지름을 기준으로 정렬
    pancakes.sort(key=lambda x: (x[0], x[1]), reverse=True)
    
    max_area = 0
    
    for i in range(N - K + 1):
        # 현재 팬케이크를 맨 아래로 놓았을 때 가능한 최대 노출 면적 계산
        area = math.pi * pancakes[i][0] * pancakes[i][0]  # 맨 아래 팬케이크의 윗면 노출 면적
        area += 2 * math.pi * pancakes[i][0] * pancakes[i][1]  # 맨 아래 팬케이크의 측면 노출 면적
        
        remaining_pancakes = pancakes[i+1:]
        
        # 다음으로 큰 팬케이크부터 K-1개의 팬케이크를 선택하여 노출 면적 계산
        remaining_pancakes.sort(key=lambda x: (x[0], x[1]), reverse=True)
        for j in range(K - 1):
            area += 2 * math.pi * remaining_pancakes[j][0] * remaining_pancakes[j][1]  # 측면 노출 면적
        
        max_area = max(max_area, area)
    
    return max_area

# 입력 처리 및 결과 출력
T = int(input())

for case in range(1, T + 1):
    N, K = map(int, input().split())
    pancakes = [list(map(int, input().split())) for _ in range(N)]
    
    result = max_exposed_surface_area(N, K, pancakes)
    
    print(f"Case #{case}: {result:.9f}")