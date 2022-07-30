# Z silver 1
# https://www.acmicpc.net/problem/1074
import sys

n, r, c = map(int, input().split())

sys.setrecursionlimit(10 ** 7)


def drawZ(n, r, c):
    half = 2 ** (n - 1)
    if n == 0:
        return 0
    if r < half and c < half:
        return drawZ(n - 1, r, c)
    elif r < half <= c:
        return half * half + drawZ(n - 1, r - half, c)
    elif r >= half > c:
        return 2 * half * half + drawZ(n - 1, r - half, c)
    else:
        return 3 * half * half + drawZ(n - 1, r - half, c - half)


print(drawZ(n, r, c))
