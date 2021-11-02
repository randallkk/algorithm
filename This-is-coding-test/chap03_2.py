def solve():
    n, m, k = map(int, input().split())
    nums = map(int, input().split())
    desc = sorted(nums, reverse=1)
    first = desc[0]
    second = desc[1]
    answer = 0
    i = 0
    while m > 0:
        m -= 1
        if i == k:
            i = 0
            answer += second
        else:
            i += 1
            answer += first
    print(answer)
    
def greedy():
    n, m, k = map(int, input().split())
    nums = map(int, input().split())
    desc = sorted(nums, reverse=1)
    first = desc[0]
    second = desc[1]
    answer = (k * first + second) * (m // (k+1)) + (m % (k+1)) * first
    print(answer)

if __name__ == "__main__":
    solve()
    greedy()