import re

def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    new_id = re.sub('[^a-zA-Z0-9\-\_\.]','',new_id)
    new_id = re.sub('\.+','.',new_id).strip('.')
    print(new_id)
    if len(new_id) == 0:
        answer= "aaa"
    elif len(new_id) >= 16:
        answer = new_id[:15].strip('.')
    elif len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]
        answer = new_id
    print(answer)
    return answer