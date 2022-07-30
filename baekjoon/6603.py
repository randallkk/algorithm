# 로또 silver 2
# https://www.acmicpc.net/problem/6603
import sys
from itertools import combinations


input = sys.stdin.readline
while True:
    sk = input().rstrip()
    if len(sk) == 1:
        break
    k, *s = sk.split()

    for p in combinations(s, 6):
        print(" ".join(p))
    print()
