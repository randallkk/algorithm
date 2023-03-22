# 회전 초밥 gold 4
# https://www.acmicpc.net/problem/15961
# python3 시간초과..........
# pypy3 143928 KB	1848 ms

from collections import defaultdict

n, d, k, c = map(int, input().split())

maxtype = 0         # answer
belt = [int(input()) for _ in range(n)]
plates = defaultdict(int)

# 쿠폰으로 먹을 수 있는 초밥을 더해준다.
plates[c] += 1

# sushi와 plates 초기화 (초기 window 설정)
for i in range(-k, 0):
    plates[belt[i]] += 1
maxtype = len(plates)

# sliding window
for plateIdx in range(n-1):
    plates[belt[plateIdx-k]] -= 1
    if not plates[belt[plateIdx-k]]:
        del(plates[belt[plateIdx-k]])
    if not plates[belt[plateIdx]]:
        maxtype = max(maxtype, len(plates))
        if maxtype == d: break
    plates[belt[plateIdx]] += 1
print(maxtype)


'''from collections import deque

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

print(maxtype)'''