# 회전하는 큐 silver 4
# https://www.acmicpc.net/problem/1021
from collections import deque

answer = 0
n, m = list(map(int, input().split()))
nums = deque(map(int, input().split()))
q = deque(i for i in range(1, n+1))
while nums:
    target = nums.popleft()
    pos = q[0]
    while True:
        if target == pos:
            q.popleft()
            break
        else:
            idx = q.index(target)
            if idx < n//2:
                q.rotate(idx)
                answer += idx
            else:
                q.rotate(idx-n)
                answer += idx-n
            q.popleft()
    n -= 1
print(answer)