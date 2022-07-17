# 1959. 두 개의 숫자열 D2
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpoFaAS4DFAUq&categoryId=AV5PpoFaAS4DFAUq&categoryType=CODE&problemTitle=1959


from functools import reduce

def yield_prod(i, arr1, arr2):
    lambda arr1, arr2: arr1[j]*arr2[i+j] for j in range(n),

def solve(n, m, arr1, arr2):
    answer = 0
    if n > m:
        for i in range(n-m):
            reduce(max, , 0)
    elif n < m:
        for i in range(m-n):
            reduce(max, , 0)
    else:
        for tup in zip(arr1, arr2):
            answer += tup[0]*tup[1]
    return answer


t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print("#%d",solve(n, m, a, b) %(i+1))
