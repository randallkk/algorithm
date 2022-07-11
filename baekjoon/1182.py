# 부분수열의 합 silver 2
# https://www.acmicpc.net/problem/1182
from itertools import combinations

answer = 0
n, s = map( int, input().split())
arr = list(map(int, input().split()))
for i in range(len(arr)):
    sums = [sum(sub) for sub in combinations(arr, i+1)]
    answer += sums.count(s)

print(answer)
