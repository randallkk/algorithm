# 좋은 단어 silver 4
# https://www.acmicpc.net/problem/3986
import sys

input = sys.stdin.readline

answer = 0
n = int(input())
for _ in range(n):
    word = input().rstrip()
    length = -1
    if len(word) % 2 == 1:
        continue
    while True:
        if length == len(word):
            break
        length = len(word)
        word = word.replace("AA", '').replace("BB", '')
    if not word:
        answer += 1
print(answer)


# ABABABABA
