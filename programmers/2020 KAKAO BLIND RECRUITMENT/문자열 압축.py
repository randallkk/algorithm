from math import sqrt


def solution(s):
    answer = 0
    maxLen = 0
    lenCandid = findDivisors(len(s))

    for zipLen in range(len(s)//2):
        zippedLen = zipStr(s, zipLen)
        if maxLen < zippedLen:
            maxLen = zippedLen
    return answer

def zipStr(s, zipLen):
    zippedLen = 0

    return zippedLen

def findDivisors(num):
    divisors = []
    for candid in range((sqrt(num+1))):
        
    return divisors