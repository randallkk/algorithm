def solve():
    n, m = map(int, input().split())
    maxcard = 0
    for i in range(n):
        card = sorted(map(int, input().split()))[0]
        if maxcard < card:
            maxcard = card 
    print(maxcard)

def answer_min():
    answer = 0
    print(answer)

if __name__=="__main__":
    solve()
    greedy()