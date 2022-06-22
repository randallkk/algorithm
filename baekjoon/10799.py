# 쇠막대기 silver 3
# https://www.acmicpc.net/problem/10799

answer = 0
arrangement = input().split('()')
rods = 0    # 현재

for i in range(len(arrangement)):
    rods += len(arrangement[i]) - arrangement[i].count(')') * 2
    answer += rods

print(answer)


