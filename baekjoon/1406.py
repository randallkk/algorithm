# 에디터 silver 2
# https://www.acmicpc.net/problem/1406
import sys
from collections import deque

_string = input()
m = int(input())

operations = []

for _ in range(m):
    operations.append(sys.stdin.readline().rstrip())


def solution1(_string, operations):
    stack = deque(_string)
    queue = deque()
    for operation in operations:
        try:
            if operation[0] == "L":
                queue.appendleft(stack.pop())
            elif operation[0] == "D":
                stack.append(queue.popleft())
            elif operation[0] == "B":
                stack.pop()
            elif operation[0] == "P":
                stack.append(operation[2])
        except IndexError:
            pass
    return "".join(stack) + "".join(queue)

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        self.pos = None

    def append(self, data):
        node = Node(data, self.tail, None)
        self.tail = node
        self.count += 1
        self.pos =

    def insertleft(self, node, pos):

    def deleteleft(self, pos):


def solution2(_string, operations):
    for operation in operations:


print(solution1(_string, operations))
print(solution2(_string, operations))
