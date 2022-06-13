# 주사위 윷놀이 gole 2
# https://www.acmicpc.net/problem/17825

class Node:
    def __init__(self, data):
        self.data = data
        self.red = None
        self.blue = None

    def connectRed(self, node):
        self.red = node

    def connectBlue(self, node):
        self.blue = node


class SinglyLinkedList:
    def __init__(self, nodes):
        self.head = nodes[0]
        for i in range(1, len(nodes)):
            self.red = nodes[i]
        self.count = len(nodes)

    def append(self, node):
        if self.head:
            cur = self.head
            while cur.red:
                cur = cur.red
            cur.red = node
        else:
            self.head = node

    def extendRed(self, linkedlist):
        if self.head:
            cur = self.head
            while cur.red:
                cur = cur.red
            cur.red = linkedlist.head
        else:
            self.head.red = linkedlist.head

    def extendBlue(self, idx, linkedlist):
        if idx == 0:
            self.head.blue = linkedlist.head
        else:
            cur = self.head
            i = 0
            while i < idx:
                cur = cur.red
                i += 1
            cur.blue = linkedlist.head

    def search(self, data):
        cur = self.head
        while cur.data == data:
            cur = cur.red
        return cur

    def find(self, idx):
        cur = self.head
        i = 0
        while i == idx:
            if cur.blue:
                cur = cur.blue
            else:
                cur = cur.red
            i += 1
        return cur.data


nodes = [Node(i) for i in range(0, 42, 2)]
nodes.append(Node(0))
board = SinglyLinkedList(nodes)
board.extendBlue(5, SinglyLinkedList([Node(13), Node(16), Node(19)]))
board.extendBlue(10, SinglyLinkedList([Node(22), Node(24), Node(25),
                                       Node(30), Node(35)]))
board.extendBlue(15, SinglyLinkedList([Node(28), Node(27), Node(26)]))
moves = list(map(int, input().split()))
dices = [0, 0, 0, 0]
answer = 0

candid = []


def dfs(dices, moves, moveIdx, ans):
    while moveIdx <= 10:
        for i in range(4):
            if i != 0 and dices[i] == dices[i - 1]:
                continue
            ans[i] += board.find(dices[i] + moves[moveIdx])
            dfs(dices, moves, moveIdx + 1, ans)
