# 두 용액 gold 5
# https://www.acmicpc.net/problem/2470

n = int(input())
solutions = sorted(map(int, input().split()))
pnt1 = 0; pnt2 = n-1
minattr = 1000000000
solA = 0; solB = 0

while pnt1 < pnt2:
    now = abs(solutions[pnt1] + solutions[pnt2])
    if now < minattr:
        minattr  = now
        solA = pnt1
        solB = pnt2
        if minattr == 0:
            break
    if abs(solutions[pnt1+1] + solutions[pnt2]) < abs(solutions[pnt1] + solutions[pnt2-1]):
        pnt1 += 1
    elif abs(solutions[pnt1+1] + solutions[pnt2]) > abs(solutions[pnt1] + solutions[pnt2-1]):
        pnt2 -= 1
    else:
        pnt1 += 1
        pnt2 -= 1
        
print(solA, solB)