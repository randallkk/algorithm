# 쇠막대기 silver 3
# https://www.acmicpc.net/problem/10799

answer = 0
arrangement = input().split('()')
rods = 0    # 현재 쇠막대기 개수

for i in range(len(arrangement)):
    closed = arrangement[i].count(')')
    rods += len(arrangement[i]) - closed * 2    # open = len(arrangement[i]) - closed / rods += open - closed
    answer += rods + closed # 현재 쇠막대기 개수에 이번 회차에 닫힌 것 더해주기

print(answer)