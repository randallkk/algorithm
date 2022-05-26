from itertools import combinations
import math


def solution(nums):
    answer = 0
    odd = []
    even = []
    for num in nums:
        if num % 2:
            odd.append(num)
        else:
            even.append(num)
    for i in odd:
        for j,k in list(combinations(even,2)):
            candid = i + j + k
            if isPrime(candid):
                answer += 1
                print("candid:",candid)
            print(i,j,k)
    for i,j,k in list(combinations(odd,3)):
        candid = i + j + k
        if isPrime(candid):
            answer += 1
            print("candid:",candid)
        print(i,j,k)

    return answer

def isPrime(candidate):
    for i in range(math.floor(math.sqrt(candidate))-1):
        if candidate % (i+2) == 0:
            print(i+2)
            return False
    return True

# print(solution([1,2,7,6,4]))
print(isPrime(15))