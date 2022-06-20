# 최솟값 찾기 gold 1
# https://www.acmicpc.net/problem/11003
from collections import deque

d = deque()
n, l = list(map(int, input().split()))
nums = list(map(int, input().split()))

left = n - l
right = n

d.appendleft(min(nums[left:]))
right -= 1
if left > 0:
    left -= 1
past = -1

while right > 0:
    if past == d[0]:
        d.appendleft(min(nums[left:right]))
    else:
        d.appendleft(min(nums[left], d[0]))
    right -= 1
    if left > 0:
        left -= 1
    past = nums[right]

print(*d, sep=' ')