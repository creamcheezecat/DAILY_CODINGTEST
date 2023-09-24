""" 
https://www.acmicpc.net/problem/15998
카카오머니
15998
"""

import sys
input = sys.stdin.readline

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
 
N = int(input())
M = -1
minb = 1000000000000000001   # b의 최댓값 10^18 + 1
total_money = 0
tf = True
for _ in range(N):
    a, b = map(int,input().split())
    # 현재금액 + a가 0보다 작을 때
    if a + total_money < 0:
        # b가 0이 아닐때 b에 지금까지 들어온 최솟값을 갱신해줌
        if b > 0 and b < minb:
            minb = b
 
        if M == -1:
            # 충전이 처음이라면 M에 그냥 b-a-현재금액 넣어준다
            M = b - a - total_money
        else:
            g = gcd(M, b - a - total_money)
            # 이미 M이 구해져있으면 M과 b-a-현재금액의 최대공약수를 구한 뒤
            # g가 지금까지 입력된 b의 최솟값보다 클때만 M = g로 갱신
            if g <= minb and minb != 1000000000000000001:
                tf = False
                break
            M = g
    else:
        # 현재금액 + a가 0보다 크면 충전할 필요는 없다
        # 대신 현재금액 + a가 b와 같아야지 유효한 로그이다.
        if a + total_money != b:
            tf = False
            break
    total_money = b
 
if not tf:
    print(-1)
else:
    if M == -1:
        # tf가 True인데 M이 -1이라면, 충전을 한번도 안 한 것이므로 아무 정수나 출력하면 된다.
        print(1)
    else:
        print(M)