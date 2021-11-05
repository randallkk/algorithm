def solve():
    n = map(int, input())
    route = input().split()
    x = 1
    y = 1
    for d in route:
        if d == 'L':
            if x > 1:
                x -= 1
        elif d == 'R':
            if x < 5:
                x += 1
        elif d == 'U':
            if y > 1:
                y -= 1
        elif d == 'D':
            if y < 5:
                y += 1
    print(y,x)

if __name__ == "__main__":
    solve()