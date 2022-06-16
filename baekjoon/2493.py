# 탑 gold 5
# https://www.acmicpc.net/problem/2493

n = int(input())
towers = list(map(int, input().split()))
receptors = [0]

for i in range(1, n):
    laser = towers[i]
    for idx in range(i-1, -1, -1):
        if laser < towers[idx]:
            receptors.append(idx + 1)
            break
    if len(receptors) != i+1:
        receptors.append(0)

print(*receptors, sep=' ')
