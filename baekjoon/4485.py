# 녹색 옷 입은 애가 젤다지? gold 4
# https://www.acmicpc.net/problem/4485

from heapq import *

INF = int(1e9)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
hq = []
heapify(hq)
tc = 0
n = int(input())
while n:
    tc += 1
    cave = []
    dist = [[INF]*n for _ in range(n)]
    for _ in range(n):
        cave.append(list(map(int, input().split())))
    # 시작 노드에 대해서 초기화
    dist[0][0] = cave[0][0]
    heappush(hq, (dist[0][0], 0, 0))       # dist, x, y
    while hq:
        d, x, y = heappop(hq)
        if dist[x][y] < d: continue     # 현재 노드가 이미 처리된 적 있는 노드라면(hq라 앞에 나온 거리가 무조건 짧기 때문에 갱신이 필요 없다.)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
            if dist[nx][ny] > d + cave[nx][ny]: 
                dist[nx][ny] = d + cave[nx][ny]
                heappush(hq, (dist[nx][ny], nx, ny))
    print("Problem %d: %d" %(tc, dist[n-1][n-1]))
    n = int(input())
