# 로봇 프로젝트 gold 5
# https://www.acmicpc.net/problem/3649


while True:
    try:
        x = int(input()) * 10000000
        n = int(input())
        arr = []
        for _ in range(n):
            arr.append(int(input()))
        arr.sort()
        pnt1 = 0
        pnt2 = len(arr) - 1

        while pnt1 < pnt2:
            l = arr[pnt1]+arr[pnt2]
            if l > x:
                pnt2 -= 1
            elif l == x:
                break
            else:
                pnt1 += 1
        if l == x:
            print("yes", arr[pnt1], arr[pnt2])
        else:
            print("danger")
        x = input()
    except: break

# 1
# 4
# 9999998
# 1
# 2
# 9999999
# 2
# 7
# 19999997
# 3
# 6
# 19999998
# 7
# 3
# 9953257
# 2
# 8
# 19999997
# 5
# 6
# 19999998
# 7
# 5
# 5
# 9953257