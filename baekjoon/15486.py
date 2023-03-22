# 퇴사 2 gold 5
# https://www.acmicpc.net/problem/15486

import sys

# 1 ≤ N ≤ 1,500,000 이므로 O(k*n)까지만 허용할 듯...
def solution():
    input = sys.stdin.readline
    # input 받기
    n = int(input())
    schedules = [[] * (n+1) for _ in range(n+1)]     # (t, p)를 기록하는 list
    for date in range(1, n+1):
        t, p = map(int, input().split())
        if date+t-1 > n: continue
        schedules[date+t-1].append((p, date))        # schedules: 상담이 끝나는 날짜에 시작한 날짜(i)와 페이(p)를 기록한다.
    # dp 점화식
    dp = [0] * (n+1)
    for i in range(1, n+1):
        dp[i] = dp[i-1]
        for p, date in schedules[i]:
            dp[i] = max(dp[date-1] + p, dp[i])
    return dp[-1]

print(solution())

