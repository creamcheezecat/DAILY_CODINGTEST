""" 
https://www.acmicpc.net/problem/1963
수소 경로
1963
"""

import sys
import math
from collections import deque
input = sys.stdin.readline

def isPrimeNumber(x):
    if x < 2:
        return False
    
    end = int(math.sqrt(x))
    for i in range(2, end + 1):
        if x % i == 0:
            return False
    return True

def bfs():
    q = deque()
    q.append([a, 0])

    # 방문여부
    visited = [0 for i in range(10000)]
    visited[a] = 1

    while q:
        now, cnt = q.popleft()
        # now를 숫자에서 문자로 변환
        strNow = str(now)

        # 빼낸 값이 end면 cnt 리턴 
        if now == b:
            return cnt

        for i in range(4):
            # 각 자리에 0 ~ 9를 넣어가며 소수인지 확인
            for j in range(10):
                temp = int(strNow[:i] + str(j) + strNow[i+1:])

                # 방문 X, 소수 O, 1000이상인 숫자
                if visited[temp] == 0 and isPrimeNumber(temp) and temp >= 1000:
                    visited[temp] = 1
                    q.append([temp, cnt + 1])
    
# 한번에 한자리 수 밖에 바꿀수없다.
# a,b 둘다 4 자리 수 이다.
# 무조건 소수 일 수 밖에 없다.

T = int(input())
for _ in range(T):
    a,b = map(int,input().split())
    
    result = bfs()
    print(result if result != None else "Impossible" )