answer = 0
n = int(input())
arr = input().split()
x = int(input())

arr = [int(a) for a in arr if int(a) < x]
arr.sort()

ai = 0
aj = len(arr) - 1
while ai < aj:
    if arr[aj] < x - arr[ai]:
        ai += 1
    elif arr[aj] == x - arr[ai]:
        ai += 1
        aj -= 1
        answer += 1
    elif arr[aj] > x - arr[ai]:
        aj -= 1

print(answer)
