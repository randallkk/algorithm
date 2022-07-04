# 탑 gold 5
# https://www.acmicpc.net/problem/2493
import heapq

n = int(input())
towers = list(map(int, input().split()))
receptors = [0 for _ in range(n)]
towerhq = [(-towers[i], i) for i in range(n)]
heapq.heapify(towerhq)
candid = []

for i in range(n):
    laser = -towerhq[i][0]
    idx = towerhq[i][1]
    candid.append(idx)
    for j in range(i):
        candid = []
        if laser > -towerhq[j][0]:
            candid.append(towerhq[i][1] + 1)
    if candid:
        receptors.append(min(candid))
    else:
        receptors.append(0)

print(*receptors, sep=' ')
