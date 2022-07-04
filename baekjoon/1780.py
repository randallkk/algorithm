# 종이의 개수 silver 2
# https://www.acmicpc.net/problem/1780
import sys

input = sys.stdin.readline

minus, zero, plus = 0, 0, 0


def cut(n, x, y):
    global minus, zero, plus
    if not n:
        return False
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != paper[x][y]:
                sliced = n // 3
                cut(sliced, x, y)
                cut(sliced, x, y + sliced)
                cut(sliced, x, y + 2 * sliced)
                cut(sliced, x + sliced, y)
                cut(sliced, x + sliced, y + sliced)
                cut(sliced, x + sliced, y + 2 * sliced)
                cut(sliced, x + 2 * sliced, y)
                cut(sliced, x + 2 * sliced, y + sliced)
                cut(sliced, x + 2 * sliced, y + 2 * sliced)
                return False
    if paper[x][y] == "-1":
        minus += 1
    elif paper[x][y] == "0":
        zero += 1
    elif paper[x][y] == "1":
        plus += 1


n = int(input())
paper = [input().rstrip().split() for _ in range(n)]
cut(n, 0, 0)
print(minus)
print(zero)
print(plus)