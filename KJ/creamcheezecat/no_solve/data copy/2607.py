""" 
https://www.acmicpc.net/problem/2607
비슷한 단어
2607
"""

import sys
input = sys.stdin.readline

N = int(input())
target_str = input().strip()
str_list = [input().strip() for _ in range(N - 1)]
ans = 0

for alpha_str in str_list:
    if abs(len(alpha_str) - len(target_str)) > 1 or \
            len(set(target_str).difference(set(alpha_str))) > 1: continue
    for t in target_str:
        if t in alpha_str: alpha_str = alpha_str.replace(t, "", 1)
	if len(alpha_str) <= 1:
        ans += 1

print(ans)