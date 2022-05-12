import re

def solution(s):
    answer = 0
    eng_words = {"zero": "0", "one": "1","two": "2", "three": "3", "four": "4", "five": "5", 
    "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    for key in eng_words.keys():
        s = re.sub(key, eng_words[key], s)
    answer = int(s)
    return answer