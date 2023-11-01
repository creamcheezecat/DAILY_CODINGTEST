""" 
https://www.acmicpc.net/problem/1765
닭싸움 팀 정하기
1765
"""

import sys
from collections import defaultdict
input = sys.stdin.readline

# v의 친구 관계 중 루트를 찾기 위한 함수
def find(v):
    if friends[v] < 0:
        return v

    friends[v] = find(friends[v])
    return friends[v]


# a와 b를 친구로 묶어주기 위한 함수
def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return

    friends[b] = a


# 두 번째 조건인 '내 원수의 원수도 내 친구이다'를 위해
# 원수의 원수와 친구 관계를 맺어주기 위한 함수
def findFriends(v):
    for enemy in enemies[v]:  # enemy: 내 원 수
        for friend in enemies[enemy]:  # friend: 내 원수의 원수
            union(v, friend)  # 나와 friend를 union 해준다.


if __name__ == '__main__':
    N = int(input())  # 학생의 수
    M = int(input())  # 인간관계 개수

    friends = [-1 for _ in range(N+1)]  # 친구 관계 배열
    enemies = [[] for _ in range(N+1)]  # 원수 관계 배열

    for _ in range(M):
        a, b, c = map(str, input().split())
        b, c = int(b), int(c)

        if a == 'F':
            union(b, c)  # 친구 관계인 경우 두 학생 유니온
        else:  # 원수 관계인 경우 원수 관계 배열에 추가
            enemies[b].append(c)
            enemies[c].append(b)

    # 모든 학생에 대하여 원수의 원수인 학생과 친구를 맺어준다
    for i in range(1, N+1):
        findFriends(i)

    print(friends.count(-1) - 1)