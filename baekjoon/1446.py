# 지름길 silver 1
# https://www.acmicpc.net/problem/1446

from heapq import heapify, heappop, heappush

INF = int(1e9)
N, D = map(int, input().split())
adjList = dict()
shortcutPoints = set()
for _ in range(N):
    start, end, length = map(int, input().split())
    shortcutPoints.add(start)
    shortcutPoints.add(end)
    if adjList.get(start):
        adjList[start].append((end, length))
    else:
        adjList[start] = [(end, length)]

shortcutPoints = dict().fromkeys(shortcutPoints, INF)
for key in shortcutPoints.keys():
    shortcutPoints[key] = key


hq = []
heapify(hq)
heappush(hq, (0, 0))
while hq:
    cur = heappop(hq)