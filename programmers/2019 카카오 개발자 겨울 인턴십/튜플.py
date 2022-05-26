from collections import Counter

def solution(s):
    answer = []
    s = s[2:len(s)-2].replace("},{", ",")   # re.findall('\d+', s)
    cnt = Counter(s.split(","))
    answer = [int(element) for element, count in cnt.most_common()]
    return answer

print(solution("{{20,111},{111}}"))