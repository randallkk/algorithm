# 작업 gold 5
# https://www.acmicpc.net/problem/2056

from collections import deque


n = int(input())
priors = [-1]
costs = [-1]
edges = [[] for _ in range(n+1)]
time = [0]*(n+1)
for i in range(n):
    cost, priorNum, *priorJobs = map(int, input().split())
    costs.append(cost)
    priors.append(priorNum)
    for node in priorJobs:
        edges[node].append(i+1)

queue = deque()
for i in range(len(priors)):
    if priors[i] == 0:
        queue.append(i)
        time[i] = costs[i]

while queue:
    cur = queue.popleft()
    for adj in edges[cur]:
        priors[adj] -= 1
        time[adj] = max(time[adj], time[cur] + costs[adj])
        if priors[adj] == 0:
            queue.append(adj)

print(max(time))