# 물병 silver1
# https://www.acmicpc.net/problem/1052

answer = 0
n, k = map(int, input().split())
water = 0
def approx(num):
    e = 0
    while n > 2**e:
        e += 1

e = approx(n)
for _ in range(k-1):
    while n > 2**e:
        e -= 1
    water += 2**e
    