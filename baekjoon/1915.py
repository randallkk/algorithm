# 가장 큰 정사각형 gold 4
# https://www.acmicpc.net/problem/1915
# python3 63676 KB	968 ms
# pypy3 132528 KB	216 ms

n, m = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(n)]
dp = [[0] * m for _ in range(n)]

for j in range(m):
    if arr[0][j]:
        dp[0][j] = 1
for i in range(n):
    if arr[i][0]:
        dp[i][0] = 1

answer = max(dp[0])
for i in range(1, n):
    for j in range(1, m):
        if arr[i][j]:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
    answer = max(answer, max(dp[i]))
print(answer*answer)