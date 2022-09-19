# 네트워크 연결 gold 4
# https://www.acmicpc.net/problem/1922

from heapq import heapify, heappop


n = int(input())
m = int(input())
adjList = [[] for _ in range(n+1)]
parents = [i for i in range(n+1)]
hq = []
for _ in range(m):
    a, b, c = map(int, input().split())
    hq.append((c, a, b))
heapify(hq)

def kruskal(hq):
    def find(node):
        if parents[node] == node:
            return node
        parents[node] = find(parents[node])
        return parents[node]

    def union(nodeA, nodeB):
        aRoot = find(nodeA)
        bRoot = find(nodeB)
        if aRoot == bRoot: return False
        parents[bRoot] = aRoot
        return True

    dist = 0
    cnt = 0
    while hq:
        c, a, b = heappop(hq)
        if union(a, b) :
            dist += c
            cnt += 1
            if cnt == n-1: break
    return dist

print(kruskal(hq))