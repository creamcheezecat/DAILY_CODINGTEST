""" 
https://www.acmicpc.net/problem/5585
거스름돈
5585
"""

import sys
input = sys.stdin.readline

N = 1000 - int(input())
coins = (500,100,50,10,5,1)
count = 0
for coin in coins:
    count += N//coin
    N%=coin
print(count)