# 도서관 gold5
# https://www.acmicpc.net/problem/1461


n, m = map(int, input().split())
books = sorted(map(int, input().split()))

left = 0; right = 0

for book in books:
    if book < 0:
        left += 0
    else:
        right += 0

