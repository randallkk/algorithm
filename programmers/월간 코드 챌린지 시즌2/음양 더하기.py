def solution(absolutes, signs):
    real_numbers = []
    for i, sign in zip(absolutes,signs):
        if sign:
            real_numbers.append(i)
        else: 
            real_numbers.append(i * -1)
    answer = sum(real_numbers)
    return answer