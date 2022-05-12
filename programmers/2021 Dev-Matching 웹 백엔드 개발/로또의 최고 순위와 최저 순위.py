def solution(lottos, win_nums):
    answer = []
    match = 0
    unknown = 0
    for num in lottos:
        if num == 0:
            unknown += 1
            pass
        if num in win_nums:
            match += 1
    answer = [6 if match == 0 and unknown == 0 else 7- (match + unknown), 7-match if match > 1 else 6]
    return answer