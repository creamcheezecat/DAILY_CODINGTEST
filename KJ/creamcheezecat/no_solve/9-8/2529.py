""" 
https://www.acmicpc.net/problem/2529
부등호
"""

import sys
input = sys.stdin.readline

K = int(input())
sign = list(input().split())

visited = [False]*10
max_ans = ""
min_ans = ""

def check(i,j,k):
    if k == "<":
        return i < j
    else:
        return i > j
    
def dfs(depth,s):
    global max_ans,min_ans
    
    if(depth == K + 1):
        if len(min_ans) == 0:
            min_ans = s
        else:
            max_ans = s
        return
    
    for i in range(10):
        if not visited[i]:
            if(depth == 0 or check(s[-1], str(i),sign[depth-1])):
                visited[i] = True
                dfs(depth+1,s+str(i))
                visited[i] = False

dfs(0,"")
print(max_ans)
print(min_ans)