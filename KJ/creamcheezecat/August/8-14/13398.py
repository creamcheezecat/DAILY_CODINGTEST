""" 
https://www.acmicpc.net/problem/13398
연속 합2
13398
"""

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
dp = [[0] * N for _ in range(2)]
# dp[0][i] : 특정 원소를 제거하지 않은 경우
# dp[1][i] : 특정 원소를 제거한 경우

dp[0][0] = arr[0] # 1개는 반드시 선택해야 한다.

if N > 1:
    ans = -1e9
    for i in range(1, N):
        # 아무런 원소를 제거하지 않았을 때, (이전까지의 연속합 + i번쨰 원소) 와 (i번째 원소)를 비교하여 큰 경우를 대입
        dp[0][i] = max(dp[0][i - 1] + arr[i], arr[i])
        # 특정 원소를 제거하는 경우 => 1. i번째 원소를 제거하는 경우 2. i번째 이전에서 이미 특정 원소를 제거하여 i번째 원소를 선택하는 경우
        # 1의 경우 dp[0][i - 1] 2의 경우 dp[1][i-1] + arr[i]
        dp[1][i] = max(dp[0][i - 1], dp[1][i-1] + arr[i])
        # dp 진행 중 가장 큰 값으로 갱신
        ans = max(ans, dp[0][i], dp[1][i])
    print(ans)
else: # N이 1인 경우는 반드시 선택을 해야하므로 dp[0][0] 출력
    print(dp[0][0])