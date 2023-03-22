# 단축키 지정 silver 1
# https://www.acmicpc.net/problem/1283
# python    31256 kb	44 ms

def solution():
    N = int(input())
    hotkeys = [False] * 26
    for _ in range(N):
        string = input()
        result = string
        words = string.split()
        has_hotkey = False
        # 1. 모든 단어의 첫글자
        for i in range(len(words)):
            alphabet = words[i][0]
            if hotkeys[ord(alphabet.lower()) - ord('a')]: pass
            else:
                hotkeys[ord(alphabet.lower()) - ord('a')] = True
                has_hotkey = True
                idx = 0
                for cnt in range(i):
                    idx += len(words[cnt]) + 1
                result = string[:idx] + '[' + string[idx] + ']'
                if len(string) - 1 != idx:
                    result += string[idx+1:]
                break
        # 2. 
        if not has_hotkey:
            for i in range(len(string)):
                alphabet = string[i]
                if alphabet == ' ' or hotkeys[ord(alphabet.lower()) - ord('a')]: pass
                else:
                    hotkeys[ord(alphabet.lower()) - ord('a')] = True
                    result = string[:i] + '[' + string[i] + ']'
                    if len(string) - 1 != i:
                        result += string[i+1:]
                    break
        print(result)

solution()
