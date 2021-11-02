import time

def solve(n, k):
    start = time.time()
    answer = 0
    while True:
        if n == 1:
            break
        if n % k == 0:
            n /= k
        else:
            n -= 1
        answer += 1
    end = time.time()
    print('solve:', answer)
    print("Time:", end-start)

if __name__=="__main__":
    n, k = map(int, input().split())
    solve(n, k)