import math


def solution(w, h):
    answer = 1
    long = max(w, h)
    short = min(w, h)
    lcm =  long * short // math.gcd(long, short)
    sliced = math.ceil(long / short) * short/lcm
    answer = w * h - sliced * lcm
    return answer