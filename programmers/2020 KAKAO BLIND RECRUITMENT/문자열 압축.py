import re


def solution(s: str):
    minlen = 10e9
    repeat_unit = 1
    while repeat_unit < len(s)/2 -1:
        zipped_s = zipstr(s, repeat_unit + 1)
        if minlen > len(zipped_s):
            minlen = len(zipped_s)
        repeat_unit += 1
    return minlen


def zipstr(s: str, unit: int):
    print('s',s,', unit',unit)
    zippedstr = ''
    repeated = 1
    for i in range(len(s)//unit - 1):
        this = s[i*unit:(i+1)*unit]
        next = s[(i+1)*unit:(i+2)*unit]
        print('this',this)
        print('next',next)
        if this == next:
            repeated += 1
        else:
            zippedstr += (str(repeated) + this)
            repeated = 1
    if len(s)%unit != 0:
        tail = s[-(len(s)%unit):]
        zippedstr += tail
    zippedstr = zippedstr.replace('1','')
    print('zippedstr', zippedstr)
    return zippedstr


print(solution("abcabcdede"))