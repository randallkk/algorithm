answer = ""
numbers = [0 for _ in range(26)]

s = input()
for alphabet in s:
    numbers[ord(alphabet) - ord('a')] += 1

for number in numbers:
    answer += str(number)+' '

print(answer)