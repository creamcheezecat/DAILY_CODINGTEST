""" 
https://www.acmicpc.net/problem/1493<br/>
박스 채우기<br/>
1493
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

len, wid, hei = map(int,input().split()) # 박스 크기
N = int(input()) # 큐브 갯수
cubes = []
for _ in range(N): # 큐브 종류와 갯수 2^i 만큼 크기 증가
    cubes.append(list(map(int,input().split())))

def fun(l, w, h, c):
    if l == 0 and w == 0 and h == 0:
        return 0

    if c < 0:
        return float('inf')

    cube_len = 2 ** cubes[c][0]
    max_count = min(l // cube_len, w // cube_len, h // cube_len)
    max_count = min(max_count, cubes[c][1])  # 사용 가능한 큐브 수 고려

    # 현재 크기의 큐브를 넣어보기
    
    for i in range(max_count, -1, -1):
        if l >= i * cube_len and w >= i * cube_len and h >= i * cube_len:
            boxes = fun(l - i * cube_len, w - i * cube_len, h - i * cube_len, c - 1)
            if boxes != float('inf'):
                return boxes + i
    
    return float('inf')

sol = fun(len, wid, hei, N - 1)
if sol == float('inf'):
    print(-1)
else:
    print(sol)

# def fun(l,w, h ,c, s):
#     if l == 0 and w == 0 and h == 0 :
#         return
    
#     if c < 0:
#         return
    
#     if(cubes[c][1] > 0 ):
#         cube_len = 2 ** cubes[c][0]
#         if cube_len <= l and cube_len <= w and cube_len <= h:
#             l -= cube_len
#             w -= cube_len
#             h -= cube_len
#             s += 1
#     else:
#         c -= 1
    
#     fun(l,w,h,c,s)

# sol = 0
# fun(len,wid,hei,N-1,sol)
# print(sol)