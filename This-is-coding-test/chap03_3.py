import time

def solve():
    start = time.time()
    n, m = map(int, input().split())
    maxcard = 0
    for i in range(n):
        card = sorted(map(int, input().split()))[0]
        if maxcard < card:
            maxcard = card 
    end = time.time()
    print("solve", maxcard)
    print("Time:", end-start)

if __name__=="__main__":
    solve()