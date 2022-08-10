# 회전 초밥 gold 4
# https://www.acmicpc.net/problem/15961

from collections import deque

n, d, k, c = map(int, input().split())
belt = []
maxtype = 1

for _ in range(n):
    belt.append(int(input()))

ate = deque(belt[n-k:n])

for i in range(n-k-1, -k, -1):
    sushiTypes = set(ate)
    sushiTypes.add(c)
    ate.pop()
    ate.appendleft(belt[i])
    if len(sushiTypes) > maxtype:
        maxtype = len(sushiTypes)
    if maxtype == d:
        break

print(maxtype)