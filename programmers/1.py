def solution(atmos):
    day = -1
    mask = 0
    for micro, supermicro in atmos:
        atmos_status = check_atmos(micro, supermicro)
        day = check_days(day)
        if atmos_status != 0 and day == -1:
            mask += 1
            day = 1
        elif day == 3:
            day = -1
        if atmos_status == -1:
            day = -1
    return mask


def check_days(day):
    if day > 0:
        day += 1
    return day

def check_atmos(micro, supermicro):
    if micro >= 151 and supermicro >= 76:
        return -1
    elif micro >= 81 or supermicro >= 36:
        return 1
    else:
        return 0

print(solution(
    [[140, 90], [177, 75], [95, 45], [71, 31], [150, 30], [80, 35], [72, 33], [166, 81], [151, 75]]
))
