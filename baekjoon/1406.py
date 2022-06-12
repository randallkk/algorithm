# 에디터 silver 2
# https://www.acmicpc.net/problem/1406
import sys

_string = list(input())
cursor = len(_string)
m = int(input())

operations = []

for _ in range(m):
    operations.append(sys.stdin.readline().rstrip())
print(operations)
for operation in operations:
    print(_string)
    next()
    if operation[0] == "L" and cursor > 0:
        cursor -= 1
    elif operation[0] == "D" and cursor < len(_string):
        cursor += 1
    elif operation[0] == "B" and cursor > 0:
        _string.delete()
        cursor -= 1
    elif operation[0] == "P":
        _string.insert(cursor, operation[2])
        cursor += 1

print("".join(_string))