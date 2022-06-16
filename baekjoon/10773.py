# 제로 silver 4
# https://www.acmicpc.net/problem/10773
import sys

account = []
k = int(input())
for _ in range(k):
    number = int(sys.stdin.readline())
    if number:
        account.append(number)
    else:
        account.pop()

print(sum(account))