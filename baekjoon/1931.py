# 회의실 배정 silver1
# https://www.acmicpc.net/problem/1931

import sys


answer = 0
meetings = []
input = sys.stdin.readline
for _ in range(int(input())):
    meetings.append(tuple(map(int, input().split())))
meetings.sort(key = lambda x: (x[1], x[0]))
# meetings.sort(key = lambda x: (x[0], x[1]-x[0]))
print(meetings)

assign = -1
for meeting in meetings:
    if assign <= meeting[0]:
        assign = meeting[1]
        answer += 1

print(answer)