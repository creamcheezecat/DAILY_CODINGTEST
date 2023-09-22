""" 
https://www.acmicpc.net/problem/14791
깔끔한 숫자
14791
"""

import sys
input = sys.stdin.readline

# 깔끔한 수인지 검사
def isTidy(n):
    return list(str(n)) == sorted(list(str(n)))

# 가장 가까운 깔끔한 수 구하기
def check(number):
    if isTidy(number):
        return number
    length = len(str(number))
    for i in range(1,length):
        a, b = divmod(number,10**i)
        target = str(a-1)+'9'*len(str(b))
        if isTidy(target):
            return int(target)

# 테스트케이스
t = int(input())
for i in range(1,t+1):
    number = int(input())
    print(f"Case #{i}:",check(number))