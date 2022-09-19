# 특정 거리의 도시 찾기 silver 2
# https://www.acmicpc.net/problem/18352

from collections import deque

INF = int(1e9)
answers = []
n, m, k, x = map(int, input().split())
adjList = [[] for _ in range(n+1)]
dist = [INF] * (n+1)
for _ in range(m):
    depart, arrive = map(int, input().split())
    adjList[depart].append(arrive)
queue = deque()
queue.append(x)
dist[x] = 0
while queue:
    cur = queue.popleft()
    for adj in adjList[cur]:
        if dist[adj] != INF: continue       # if not visited
        dist[adj] = dist[cur] + 1
        if dist[adj] == k:
            answers.append(adj)
            continue
        queue.append(adj)
answers.sort()
if answers:
    for node in answers:
        print(node)
else:
    print(-1)