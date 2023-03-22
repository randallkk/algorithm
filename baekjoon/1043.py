# 거짓말 gold 4
# https://www.acmicpc.net/problem/1043
# python3 30840 KB	68 ms
# pypy3 114328 KB	116 ms

n, m = map(int, input().split())
ppl, *truthPpl = map(int, input().split())
truthPpl = set(truthPpl)
party = []
for _ in range(m):
    num, *participants = map(int, input().split())
    participants = set(participants)
    party.append(participants)

truthParty = [False] * m
updated = True
while updated:
    updated = False
    for i in range(m):
        if party[i] & truthPpl and not truthParty[i]:
            truthPpl.update(party[i])
            truthParty[i] = True
            updated = True
print(truthParty.count(False))
