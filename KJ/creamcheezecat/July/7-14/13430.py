""" 
https://www.acmicpc.net/problem/13430<br/>
합 구하기<br/>
13430
"""
import sys
input = sys.stdin.readline

MOD = 1000000007

def mul(A, B):
    ret = [[0] * 55 for _ in range(55)]
    for i in range(k + 2):
        for j in range(k + 2):
            for a in range(k + 2):
                ret[i][j] = (ret[i][j] + (A[i][a] * B[a][j])) % MOD
    for i in range(55):
        for j in range(55):
            A[i][j] = ret[i][j]

k, n = map(int, input().split())

ans = [[0] * 55 for _ in range(55)]
arr = [[0] * 55 for _ in range(55)]

for i in range(k + 2):
    ans[i][i] = 1
    for j in range(i + 1):
        arr[i][j] = 1

n -= 1

while n > 0:
    if n % 2 == 1:
        mul(ans, arr)
    mul(arr, arr)
    n //= 2

sum_val = 0
for i in range(k + 2):
    sum_val = (sum_val + ans[k + 1][i]) % MOD

print(sum_val)
# 메모리 초과
""" def fun(K, N):
    dp = [[0] * (N+1) for _ in range(K+1)]

    # 초기화
    for i in range(N+1):
        dp[0][i] = i

    # 점화식에 따라 계산
    for k in range(1, K+1):
        for n in range(1, N+1):
            dp[k][n] = sum(dp[k-1][:n+1])

    return dp[K][N] % 1000000007


k,n = map(int,input().split())
result = fun(k, n)
print(result) """


# 시간 초과
""" def fun(K,N):
    # 종료 조건
    if K == 0:
        return N
    result = 0
    for i in range(1,N+1):
        result += fun(K-1,i)
        
    return result

print(fun(k,n) % 1000000007) """